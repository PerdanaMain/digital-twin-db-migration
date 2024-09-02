"""
Define the Cases model
"""

from enum import Enum
from uuid import uuid4

from sqlalchemy import BigInteger, Boolean, Column, Float, ForeignKey, Integer, String, select
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from digital_twin_migration.database import db
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel
from digital_twin_migration.models.efficiency_app.efficiency_trasanction_detail_root_causes import EfficiencyDataDetailRootCause
from digital_twin_migration.security.access_control import (
    Allow,
    Authenticated,
    RolePrincipal,
    UserPrincipal,
)


class EfficiencyDetailPermission(Enum):
    CREATE = "create"
    READ = "read"
    EDIT = "edit"
    DELETE = "delete"


class EfficiencyDataDetail(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    """The Efficiency Data Detail model"""

    __tablename__ = "hl_tr_data_detail"

    # ? Column Defaults
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    variable_id = Column(UUID(as_uuid=True), ForeignKey(
        "hl_ms_excel_variables.id", ondelete="CASCADE"), nullable=False)
    efficiency_transaction_id = Column(
        UUID(as_uuid=True), ForeignKey("hl_tr_data.id",ondelete="CASCADE"), nullable=False)
    nilai = Column(Float, nullable=True)
    nilai_string = Column(String(255), nullable=True)
    persen_hr = Column(Float, nullable=False, default=100)
    deviasi = Column(Float, nullable=False, default=1)
    created_by = Column(UUID(as_uuid=True), nullable=False)
    updated_by = Column(UUID(as_uuid=True),  nullable=True)

    root_causes = relationship("EfficiencyDataDetailRootCause",
                               back_populates="efficiency_transaction_detail", lazy="selectin")
    
    efficiency_transaction = relationship("EfficiencyTransaction", back_populates="efficiency_transaction_details", lazy="joined")
    
    variable = relationship("Variable", back_populates="efficiency_transaction_details", lazy="joined")

    __mapper_args__ = {"eager_defaults": True}
    
    
    @classmethod
    def total_cost(cls):
        # SQL-side calculation (for queries)
        return (
            select(db.func.sum(EfficiencyDataDetailRootCause.biaya))
            .where(EfficiencyDataDetailRootCause.data_detail_id == cls.id)
            .label('total_cost')
        )
    
    
    def __acl__(self):
        # basic_permissions = [CasePermission.READ]
        # self_permissions = [
        #     CasePermission.READ,
        #     CasePermission.EDIT,
        #     CasePermission.DELETE,
        # ]
        all_permissions = list(EfficiencyDetailPermission)

        return [
            (Allow, Authenticated, all_permissions),
            (Allow, RolePrincipal("admin"), all_permissions),
        ]
