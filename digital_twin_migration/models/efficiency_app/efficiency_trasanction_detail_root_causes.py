"""
Define the Cases model
"""

from enum import Enum
from uuid import uuid4

from sqlalchemy import JSON, BigInteger, Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from digital_twin_migration.database import Base
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.security.access_control import (
    Allow,
    Authenticated,
    RolePrincipal,
    UserPrincipal,
)


class EfficiencyDataDetailRootCause(Base, TimestampMixin):
    """The Cases model"""

    __tablename__ = "hl_tr_data_detail_root_cause"

    # ? Column Defaults
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    data_detail_id = Column(UUID(as_uuid=True), ForeignKey('hl_tr_data_detail.id'), nullable=True, comment='Ref to hl_tr_data_detail')
    cause_id = Column(UUID(as_uuid=True), ForeignKey('hl_ms_excel_variables_cause.id'), nullable=True, comment='Ref to hl_m_cause 1 to many')
    is_repair = Column(Boolean, default=False, comment='1=ya, 0=tidak')
    biaya = Column(Float, nullable=True, comment='Besar Biaya yang dikeluarkan (input)')
    created_at = Column(DateTime, nullable=True)
    updated_at = Column(DateTime, nullable=True)
    created_by = Column(UUID(as_uuid=True), nullable=True)
    updated_by = Column(UUID(as_uuid=True), nullable=True)
    variable_header_value = Column(JSON, nullable=True, comment='[{id: 9, nama: \'sdasdas asdasd\', val: 1}]')
    
    __mapper_args__ = {"eager_defaults": True}
    
    
