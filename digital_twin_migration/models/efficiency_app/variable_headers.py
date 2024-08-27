"""
Define the Cases model
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


class VariableHeader(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    """The Variable Headers model"""

    __tablename__ = "hl_ms_excel_variables_header"

    # ? Column Defaults
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    variable_id = Column(UUID(as_uuid=True), ForeignKey(
        'hl_ms_excel_variables.id', ondelete="CASCADE"), nullable=False)
    nama = Column(String(255), nullable=True)
    created_by = Column(String(100), nullable=True)
    updated_by = Column(String(100), nullable=True)

  
