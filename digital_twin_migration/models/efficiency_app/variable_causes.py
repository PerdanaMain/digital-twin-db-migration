
"""
Define the Variable Causes model
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


class VariableCause(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    """The Variable Causes model"""

    __tablename__ = "hl_ms_excel_variables_cause"

    # ? Column Defaults
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    parent_id = Column(UUID(as_uuid=True), ForeignKey('hl_ms_excel_variables_cause.id'),
                          nullable=True, comment='ref to id table ini sendiri (recursive)', default=id)
    variable_id = Column(UUID(as_uuid=True), ForeignKey(
        'hl_ms_excel_variables.id', ondelete="CASCADE"), nullable=False)
    name = Column(String(255), nullable=True)
    created_by = Column(String(100), nullable=True)
    updated_by = Column(String(100), nullable=True)
    
    root_causes = relationship("EfficiencyDataDetailRootCause", backref="variable_cause", lazy="joined")
