"""
Define the Cases model
"""

from digital_twin_migration.models import db
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import Index


class EfficiencyTransaction(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Cases model"""

    __tablename__ = "hl_tr_data"

    # ? Column Defaults
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    periode = db.Column(db.Date, nullable=False)
    jenis_parameter = db.Column(db.String(300), nullable=False)
    excel_id = db.Column(UUID(as_uuid=True), db.ForeignKey("hl_ms_excel.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=True)
    created_by =  db.Column(UUID(as_uuid=True), nullable=False)
    updated_by =  db.Column(UUID(as_uuid=True), nullable=True)
    

    
    
    efficiency_transaction_details = db.relationship("EfficiencyTransactionDetail", backref="efficiency_transaction")

    
    def __init__(self, periode, jenis_parameter, excel_id, created_by):
        """Create a new Cases"""
        self.periode = periode
        self.jenis_parameter = jenis_parameter
        self.excel_id = excel_id
        self.created_by = created_by
