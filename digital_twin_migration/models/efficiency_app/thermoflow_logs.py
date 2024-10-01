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


class ThermoflowLog(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    """The Efficiency Data model"""

    __tablename__ = "hl_tr_thermoflow_log"

    # ? Column Defaults
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    efficiency_transaction_id = Column(
        UUID(as_uuid=True), ForeignKey("hl_tr_data.id", ondelete="CASCADE"), nullable=False)
    status = Column(String(300), nullable=False, default="running")
    error_message = Column(String(300), nullable=True)
    completed_at = Column(DateTime, nullable=True)

    efficiency_transaction = relationship(
        "EfficiencyTransaction", back_populates="thermoflow_log", lazy="joined")

    __mapper_args__ = {"eager_defaults": True}
