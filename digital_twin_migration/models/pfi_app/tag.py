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


class PFITag(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    __tablename__ = "pfi_ms_tag"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    web_id = db.Column(String, nullable=False)
    name = db.Column(String(150), nullable=False)
    path = db.Column(String(150), nullable=False)
    descriptor = db.Column(String(150), nullable=True)
    point_class = db.Column(String(15), nullable=True)
    point_type = db.Column(String(15), nullable=True)
    digital_set_name = db.Column(String(150), nullable=True)
    engineering_units = db.Column(String(15), nullable=True)
    span = db.Column(Integer, nullable=True)
    zero = db.Column(Integer, nullable=True)
    step = db.Column(Boolean, nullable=True)
    future = db.Column(Boolean, nullable=True)
    display_digits = db.Column(Integer, nullable=False)

    tag_values = db.relationship("PFITagValue", backref="pfi_tag", lazy=True)
