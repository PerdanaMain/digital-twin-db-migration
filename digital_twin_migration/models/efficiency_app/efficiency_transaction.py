"""
Define the Efficiency Data model
"""

import datetime
from enum import Enum
from uuid import uuid4

from sqlalchemy import BigInteger, Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates

from digital_twin_migration.database import db
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel
from digital_twin_migration.security.access_control import (
    Allow,
    Authenticated,
    RolePrincipal,
    UserPrincipal,
)


class EfficiencyDataPermission(Enum):
    CREATE = "create"
    READ = "read"
    EDIT = "edit"
    DELETE = "delete"


class EfficiencyTransaction(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    """The Efficiency Data model"""

    __tablename__ = "hl_tr_data"

    # ? Column Defaults
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    periode = Column(DateTime, nullable=False, default=db.func.now())
    sequence = Column(Integer)
    name = Column(String(300), nullable=False)
    jenis_parameter = Column(String(300), nullable=False)
    excel_id = Column(UUID(as_uuid=True), ForeignKey(
        "hl_ms_excel.id", ondelete="CASCADE"), nullable=False)
    created_by = Column(UUID(as_uuid=True), nullable=False)
    updated_by = Column(UUID(as_uuid=True), nullable=True)

    efficiency_transaction_details = relationship(
        "EfficiencyDataDetail", back_populates="efficiency_transaction", lazy="selectin")
    excel = relationship(
        "Excel", back_populates="efficiency_transactions", lazy="joined")

    @validates('sequence')
    def validate_daily_increment(self, key, value):
        if not value:
            self.sequence = self.get_daily_increment()
        return value

    def get_daily_increment(self):
        session = db.session
        today = datetime.date.today()

        # Get the highest daily increment for today
        max_increment = session.query(func.max(
            EfficiencyTransaction.daily_increment)).filter_by(created_at=today).scalar()

        if max_increment is None:
            return 1
        else:
            return max_increment + 1

    __mapper_args__ = {"eager_defaults": True}

    def __acl__(self):
        # basic_permissions = [CasePermission.READ]
        # self_permissions = [
        #     CasePermission.READ,
        #     CasePermission.EDIT,
        #     CasePermission.DELETE,
        # ]
        all_permissions = list(EfficiencyDataPermission)

        return [
            (Allow, Authenticated, all_permissions),
            (Allow, RolePrincipal("admin"), all_permissions),
        ]
