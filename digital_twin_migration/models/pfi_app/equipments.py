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


class PFIEquipment(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    __tablename__ = "pfi_ms_equipment"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    parent_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("pfi_ms_equipment.id", ondelete="CASCADE"),
        nullable=True,
        comment="ref to id table ini sendiri (recursive)",
    )
    category_id = db.Column(
        UUID(as_uuid=True),
        db.ForeignKey("pfi_ms_category.id", ondelete="CASCADE"),
    )
    name = db.Column(db.String(255), nullable=False, comment="Nama Equipment")
    description = db.Column(db.Text, nullable=True, comment="Deskripsi Equipment")

    __mapper_args__ = {"eager_defaults": True}
