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
    periode = Column(DateTime, nullable=False,
                     default=func.now().op('AT TIME ZONE')('Asia/Jakarta'))
    sequence = Column(Integer, nullable=False)
    name = Column(String(300), nullable=False)
    jenis_parameter = Column(String(300), nullable=False)
    persen_threshold = Column(Integer, nullable=True, default=100)
    excel_id = Column(UUID(as_uuid=True), ForeignKey(
        "hl_ms_excel.id", ondelete="CASCADE"), nullable=False)
    is_perfomance_test = Column(Boolean, nullable=True, default=False)
    performance_test_weight = Column(Integer, nullable=True, default=100)
    created_by = Column(UUID(as_uuid=True), nullable=False)
    updated_by = Column(UUID(as_uuid=True), nullable=True)

    efficiency_transaction_details = relationship(
        "EfficiencyDataDetail", back_populates="efficiency_transaction", lazy="selectin",  cascade="all, delete")
    excel = relationship(
        "Excel", back_populates="efficiency_transactions", lazy="joined")

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
