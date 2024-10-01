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


class ThermoflowStatus(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    """The Efficiency Data model"""

    __tablename__ = "hl_ms_thermoflow_status"

    # ? Column Defaults
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    is_running = Column(Boolean, nullable=False, default=False)