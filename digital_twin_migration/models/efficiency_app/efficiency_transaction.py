"""
Define the Efficiency Data model
"""

from enum import Enum
from uuid import uuid4

from sqlalchemy import BigInteger, Boolean, Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

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
    periode = Column(Date, nullable=False)
    jenis_parameter = Column(String(300), nullable=False)
    excel_id = Column(UUID(as_uuid=True), ForeignKey("hl_ms_excel.id", ondelete="CASCADE"), nullable=False)
    created_by =  Column(UUID(as_uuid=True), nullable=False)
    updated_by =  Column(UUID(as_uuid=True), nullable=True)
    
    efficiency_transaction_details = relationship("EfficiencyDataDetail", backref="efficiency_transaction", lazy="dynamic")

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
