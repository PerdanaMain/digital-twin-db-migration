"""
Define the Excels model
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


class Excel(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    """The Excels model"""

    __tablename__ = "hl_ms_excel"

    # ? Column Defaults
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    excel_filename = Column(String(300), nullable=False, unique=True)
    description = Column(String(300), nullable=True)
    created_by =  Column(UUID(as_uuid=True), nullable=False)
    updated_by =  Column(UUID(as_uuid=True), nullable=True)
    

    # ? Relationships
    variables = relationship("Variable", backref= 'excel')
    efficiency_transactions = relationship("EfficiencyTransaction", lazy="subquery")
    
