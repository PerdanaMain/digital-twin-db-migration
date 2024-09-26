from uuid import uuid4
from digital_twin_migration.database import db
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

import datetime
from enum import Enum
from uuid import uuid4

from sqlalchemy import (
    BigInteger,
    Boolean,
    Column,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Integer,
    String,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates

from digital_twin_migration.database import db
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel
from digital_twin_migration.security.access_control import (
    Allow,
    Authenticated,
    RolePrincipal,
    UserPrincipal,
)


class PFITagValue(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    __tablename__ = "pfi_value_tag"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    tag_id = db.Column(
        db.BigInteger, db.ForeignKey("pfi_ms_tag.id", ondelete="CASCADE"), nullable=False
    )
    time_stamp = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.Float, nullable=False)
    units_abbreviation = db.Column(db.String(15), nullable=False)
    good = db.Column(db.Boolean, nullable=False)
    questionable = db.Column(db.Boolean, nullable=False)
    substituted = db.Column(db.Boolean, nullable=False)
    annotated = db.Column(db.Boolean, nullable=False)

    tag = relationship("PFITag", back_populates="tag_values", lazy="joined")
