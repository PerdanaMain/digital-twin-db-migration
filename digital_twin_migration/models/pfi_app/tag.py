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
    web_id = db.Column(db.Text, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    path = db.Column(db.String(150), nullable=False)
    descriptor = db.Column(db.String(150), nullable=True)
    point_class = db.Column(db.String(15), nullable=True)
    point_type = db.Column(db.String(15), nullable=True)
    digital_set_name = db.Column(db.String(150), nullable=True)
    engineering_units = db.Column(db.String(15), nullable=True)
    span = db.Column(db.Integer, nullable=True)
    zero = db.Column(db.Integer, nullable=True)
    step = db.Column(db.Boolean, nullable=True)
    future = db.Column(db.Boolean, nullable=True)
    display_digits = db.Column(db.Integer, nullable=False)

    tag_values = db.relationship("PFITagValue", backref="pfi_ms_tag", lazy=True)
