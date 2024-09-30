"""
Define the Variables model
"""

from enum import Enum
from uuid import uuid4

from sqlalchemy import JSON, BigInteger, Boolean, Column, Date, DateTime, Float, ForeignKey, Integer, String
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


class Variable(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    """The Variables model"""

    __tablename__ = "hl_ms_excel_variables"

    # ? Default Columns
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    excel_id = Column(UUID(as_uuid=True), ForeignKey(
        "hl_ms_excel.id", ondelete="CASCADE"), nullable=False)

    category = Column(String(255), nullable=True)

    input_name = Column(String(255), nullable=True)

    excel_variable_name = Column(String(500))

    satuan = Column(String(50))
    
    in_out = Column(String(25))
    
    is_pareto = Column(Boolean, default=False)

    is_faktor_koreksi = Column(Boolean, default=False)

    is_nilai_losses = Column(Boolean, default=False)

    is_nphr = Column(Boolean, default=False)

    is_over_haul = Column(Boolean, default=False)
    
    konstanta = Column(Float)

    web_id = Column(String(255), nullable=True, comment="PI Web ID")
    created_by = Column(UUID(as_uuid=True), nullable=False)
    updated_by = Column(UUID(as_uuid=True), nullable=True)

    # ? Relationship
    efficiency_transaction_details = relationship(
        "EfficiencyDataDetail", back_populates="variable", lazy="selectin", cascade="all, delete")

    excel = relationship("Excel", back_populates="variables", lazy="joined")

    causes = relationship(
        "VariableCause", back_populates="variable", lazy="selectin", cascade="all, delete")

    headers = relationship(
        "VariableHeader", back_populates="variable", lazy="selectin", cascade="all, delete")
