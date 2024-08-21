"""
Define the Excels model
"""

from . import db
from .abc import BaseModel, MetaBaseModel
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Excels(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Excels model"""

    __tablename__ = "hl_ms_excel"

    # ? Column Defaults
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    excel_filename = db.Column(db.String(300), nullable=False, unique=True)
    description = db.Column(db.String(300), nullable=True)
    created_by =  db.Column(UUID(as_uuid=True), nullable=False)
    updated_by =  db.Column(UUID(as_uuid=True), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=True)

    # ? Relationships
    variables = db.relationship("Variables", back_populates="excels", lazy=True)
    efficiency_transactions = db.relationship("EfficiencyTransaction", back_populates="excel", lazy=True)
    
    

    def __init__(self, excel_filename, description, created_by):
        """Create a new Excels"""
        self.excel_filename = excel_filename
        self.description = description
        self.created_by = created_by
