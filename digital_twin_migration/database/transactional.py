from enum import Enum
from functools import wraps

from digital_twin_migration.database import db


class Propagation(Enum):
    REQUIRED = "required"
    REQUIRED_NEW = "required_new"


class Transactional:
    def __init__(self, propagation: Propagation = Propagation.REQUIRED):
        self.propagation = propagation

    def __call__(self, function):
        @wraps(function)
        def decorator(*args, **kwargs):
            try:
                if self.propagation == Propagation.REQUIRED:
                    result = self._run_required(
                        function=function,
                        args=args,
                        kwargs=kwargs,
                    )
                elif self.propagation == Propagation.REQUIRED_NEW:
                    result = self._run_required_new(
                        function=function,
                        args=args,
                        kwargs=kwargs,
                    )
                else:
                    result = self._run_required(
                        function=function,
                        args=args,
                        kwargs=kwargs,
                    )
            except Exception as exception:
                db.session.rollback()
                raise exception

            return result

        return decorator

    def _run_required(self, function, args, kwargs) -> None:
        result = function(*args, **kwargs)
        db.session.commit()
        return result

    def _run_required_new(self, function, args, kwargs) -> None:
        db.session.begin()
        result = function(*args, **kwargs)
        db.session.commit()
        return result
