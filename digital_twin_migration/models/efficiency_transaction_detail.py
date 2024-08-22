"""
Define the Cases model
"""

from . import db
from .abc import BaseModel, MetaBaseModel
from sqlalchemy.dialects.postgresql import UUID
import uuid


class EfficiencyTransactionDetail(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Cases model"""

    __tablename__ = "hl_tr_data_detail"

    # ? Column Defaults
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    variable_id = db.Column(UUID(as_uuid=True), db.ForeignKey("hl_ms_excel_variables.id"), nullable=False)
    efficiency_transaction_id = db.Column(UUID(as_uuid=True), db.ForeignKey("hl_tr_data.id"), nullable=False)
    nilai = db.Column(db.Float, nullable=False)
    persen_hr = db.Column(db.Float, nullable=False, default=1)
    deviasi = db.Column(db.Float, nullable=False, default=1)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=True)
    created_by =  db.Column(UUID(as_uuid=True), nullable=False)
    updated_by =  db.Column(UUID(as_uuid=True), nullable=False)

    
    def __init__(self, variable_id, efficiency_transaction_id, nilai, created_by):
        """Create a new Cases"""
        self.efficiency_transaction_id=efficiency_transaction_id
        self.variable_id = variable_id
        self.nilai = nilai
        self.created_by = created_by
