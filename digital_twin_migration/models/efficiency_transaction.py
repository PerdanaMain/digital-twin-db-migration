"""
Define the Cases model
"""

from . import db
from .abc import BaseModel, MetaBaseModel
from sqlalchemy.dialects.postgresql import UUID
import uuid


class EfficiencyTransaction(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Cases model"""

    __tablename__ = "hl_tr_data"

    # ? Column Defaults
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    periode = db.Column(db.Date, nullable=False)
    jenis_parameter = db.Column(db.String(300), nullable=False)
    excel_id = db.Column(UUID(as_uuid=True), db.ForeignKey("hl_ms_excel.id"), nullable=False)
    variable_id = db.Column(UUID(as_uuid=True), db.ForeignKey("hl_ms_excel_variables.id"), nullable=False)
    nilai = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=True)
    created_by = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), nullable=False)
    updated_by = db.Column(UUID(as_uuid=True), db.ForeignKey("users.id"), nullable=True)


    # ? Relationship
    excel = db.relationship("Excels", back_populates="efficiency_transactions", lazy=True)
    variable = db.relationship("Variables", back_populates="efficiency_transactions", lazy=True)
    user_created = db.relationship("User", back_populates="efficiency_transactions_created", lazy=True)
    user_updated = db.relationship("User", back_populates="efficiency_transactions_updated", lazy=True)
    
    def __init__(self, name, kode, seq, group_id):
        """Create a new Cases"""
        self.name = name
        self.kode = kode
        self.seq = seq
        self.group_id = group_id
