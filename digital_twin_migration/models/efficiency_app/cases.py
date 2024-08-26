"""
Define the Cases model
"""

from digital_twin_migration.models import db
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import Index


class Cases(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Cases model"""

    __tablename__ = "hl_ms_masterdata"

    # ? Column Defaults
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(300), nullable=False, unique=True)
    kode = db.Column(db.String(300), nullable=True)
    seq = db.Column(db.Integer, nullable=True)
    group_id = db.Column(db.String(300), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=True)

    def __init__(self, name, kode, seq, group_id):
        """Create a new Cases"""
        self.name = name
        self.kode = kode
        self.seq = seq
        self.group_id = group_id