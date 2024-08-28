"""
Define an Abstract Base Class (ABC) for models
"""

from datetime import datetime
from functools import reduce
from typing import Any, TypeVar
from weakref import WeakValueDictionary

from sqlalchemy import Select, inspect, select
from sqlalchemy.orm import aliased

from digital_twin_migration.database import db


class MetaBaseModel(db.Model.__class__):
    """Define a metaclass for the BaseModel
    Implement `__getitem__` for managing aliases"""

    def __init__(cls, *args):
        super().__init__(*args)
        cls.aliases = WeakValueDictionary()

    def __getitem__(cls, key):
        try:
            alias = cls.aliases[key]
        except KeyError:
            alias = aliased(cls)
            cls.aliases[key] = alias
        return alias


class BaseModel:
    """Generalize __init__, __repr__ and to_json
    Based on the models columns"""

    print_filter = ()
    to_json_filter = ("password")

    def __repr__(self):
        """Define a base way to print models
        Columns inside `print_filter` are excluded"""
        return "%s(%s)" % (
            self.__class__.__name__,
            {
                column: value
                for column, value in self._to_dict().items()
                if column not in self.print_filter
            },
        )

    @property
    def json(self):
        """Define a base way to jsonify models
        Columns inside `to_json_filter` are excluded"""
        result = {}
        for column, value in self._to_dict().items():
            if column in self.to_json_filter:
                continue
            if isinstance(value, datetime):
                result[column] = value.strftime("%Y-%m-%d")
            elif isinstance(value, BaseModel):
                result[column] = value.json
            else:
                result[column] = value

        return result

    def _to_dict(self):
        """This would more or less be the same as a `to_json`
        But putting it in a "private" function
        Allows to_json to be overriden without impacting __repr__
        Or the other way around
        And to add filter lists"""
        return {
            column.key: getattr(self, column.key)
            for column in inspect(self.__class__).attrs
        }

    def save(self):
        db.session.add(self)
        return self

    def delete(self):
        db.session.delete(self)

    def add(self):
        db.session.add(self)
        return self

    def get_all(
        self, skip: int = 0, limit: int = 100, join_: set[str] | None = None
    ):
        """
        Returns a list of model instances.

        :param skip: The number of records to skip.
        :param limit: The number of record to return.
        :param join_: The joins to make.
        :return: A list of model instances.
        """
        query = self._query(join_)
        query = query.offset(skip).limit(limit)

        if join_ is not None:
            return self.all_unique(query)

        return self._all(query)

    def create(self, attributes: dict[str, Any] = None):
        """
        Creates the model instance.

        :param attributes: The attributes to create the model with.
        :return: The created model instance.
        """
        if attributes is None:
            attributes = {}
        model = self(**attributes)
        db.session.add(model)
        return model

    def create_bulk(self, models: list = None):
        if models is None:
            models = []

        db.session.add_all(models)

    def _query(
        self,
        join_: set[str] | None = None,
        order_: dict | None = None,
    ) -> Select:
        """
        Returns a callable that can be used to query the model.

        :param join_: The joins to make.
        :param order_: The order of the results. (e.g desc, asc)
        :return: A callable that can be used to query the model.
        """
        query = select(self)
        query = self._maybe_join(query, join_)
        query = self._maybe_ordered(query, order_)

        return query

    def _all(self, query: Select):
        """
        Returns all results from the query.

        :param query: The query to execute.
        :return: A list of model instances.
        """
        query = db.session.scalars(query)
        return query.all()

    async def _all_unique(self, query: Select):
        result = await db.session.execute(query)
        return result.unique().scalars().all()

    async def _first(self, query: Select):
        """
        Returns the first result from the query.

        :param query: The query to execute.
        :return: The first model instance.
        """
        query = await db.session.scalars(query)
        return query.first()

    async def _one_or_none(self, query: Select):
        """Returns the first result from the query or None."""
        query = await db.session.scalars(query)
        return query.one_or_none()

    async def _one(self, query: Select):
        """
        Returns the first result from the query or raises NoResultFound.

        :param query: The query to execute.
        :return: The first model instance.
        """
        query = await db.session.scalars(query)
        return query.one()

    async def _count(self, query: Select) -> int:
        """
        Returns the count of the records.

        :param query: The query to execute.
        """
        query = query.subquery()
        query = await db.session.scalars(select(db.func.count()).select_from(query))
        return query.one()

    async def _sort_by(
        self,
        query: Select,
        sort_by: str,
        order: str | None = "asc",
        model=None,
        case_insensitive: bool = False,
    ) -> Select:
        """
        Returns the query sorted by the given column.

        :param query: The query to sort.
        :param sort_by: The column to sort by.
        :param order: The order to sort by.
        :param model: The model to sort.
        :param case_insensitive: Whether to sort case insensitively.
        :return: The sorted query.
        """
        model = model or self

        order_column = None

        if case_insensitive:
            order_column = db.func.lower(getattr(model, sort_by))
        else:
            order_column = getattr(model, sort_by)

        if order == "desc":
            return query.order_by(order_column.desc())

        return query.order_by(order_column.asc())

    async def _get_by(self, query: Select, field: str, value: Any) -> Select:
        """
        Returns the query filtered by the given column.

        :param query: The query to filter.
        :param field: The column to filter by.
        :param value: The value to filter by.
        :return: The filtered query.
        """
        return query.where(getattr(self, field) == value)

    def _maybe_join(self, query: Select, join_: set[str] | None = None) -> Select:
        """
        Returns the query with the given joins.

        :param query: The query to join.
        :param join_: The joins to make.
        :return: The query with the given joins.
        """
        if not join_:
            return query

        if not isinstance(join_, set):
            raise TypeError("join_ must be a set")

        return reduce(self._add_join_to_query, join_, query)

    def _maybe_ordered(self, query: Select, order_: dict | None = None) -> Select:
        """
        Returns the query ordered by the given column.

        :param query: The query to order.
        :param order_: The order to make.
        :return: The query ordered by the given column.
        """
        if order_:
            if order_["asc"]:
                for order in order_["asc"]:
                    query = query.order_by(
                        getattr(self, order).asc())
            else:
                for order in order_["desc"]:
                    query = query.order_by(
                        getattr(self, order).desc())

        return query

    def _add_join_to_query(self, query: Select, join_: set[str]) -> Select:
        """
        Returns the query with the given join.

        :param query: The query to join.
        :param join_: The join to make.
        :return: The query with the given join.
        """
        return getattr(self, "_join_" + join_)(query)
