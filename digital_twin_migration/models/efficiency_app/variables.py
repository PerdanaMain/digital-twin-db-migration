"""
Define the Variables model
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


class Variable(Base, TimestampMixin):
    """The Variables model"""

    __tablename__ = "hl_ms_excel_variables"

    # ? Default Columns
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    excel_id = Column(UUID(as_uuid=True), ForeignKey(
        "hl_ms_excel.id"), nullable=False)
    category = Column(String(255), nullable=True)
    input_name = Column(String(255), nullable=False)
    short_name = Column(String(155))
    excel_variable_name = Column(String(500))
    satuan = Column(String(50))
    in_out = Column(String(25))
    is_pareto = Column(Boolean, default=False)
    is_faktor_koreksi = Column(Boolean, default=False)
    is_nilai_losses = Column(Boolean, default=False)
    created_by = Column(UUID(as_uuid=True), nullable=False)
    updated_by = Column(UUID(as_uuid=True), nullable=True)
    
    # ? Relationship
    efficiency_transaction_detail = relationship(
        "EfficiencyTransactionDetail", backref="variable", lazy=True)

    causes = relationship("VariableCause", backref="variable", lazy=True)
    headers = relationship(
        "VariableHeader", backref="variable", lazy=True)

