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

    id = db.Column(BigInteger, primary_key=True, autoincrement=True)
    tag_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("pfi_ms_tag.id", ondelete="CASCADE"),
        nullable=False,  # Consider making this not nullable if it's always required
        comment="Reference to PFITag",
    )
    time_stamp = db.Column(DateTime, nullable=False)
    value = db.Column(Float, nullable=False)
    units_abbreviation = db.Column(String(15), nullable=False)
    good = db.Column(Boolean, nullable=False)
    questionable = db.Column(Boolean, nullable=False)
    substituted = db.Column(Boolean, nullable=False)
    annotated = db.Column(Boolean, nullable=False)
