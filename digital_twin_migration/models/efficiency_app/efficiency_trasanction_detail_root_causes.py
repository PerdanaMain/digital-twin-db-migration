"""
Define the Cases model
"""

from digital_twin_migration.models import db
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import Index


class EfficiencyTransactionDetailRootCauses(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Cases model"""

    __tablename__ = "hl_tr_data_detail_root_cause"

    # ? db.Column Defaults
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    data_detail_id = db.Column(UUID(as_uuid=True), db.ForeignKey('hl_tr_data_detail.id'), nullable=True, comment='Ref to hl_tr_data_detail')
    cause_id = db.Column(UUID(as_uuid=True), db.ForeignKey('hl_ms_excel_variables_cause.id'), nullable=True, comment='Ref to hl_m_cause 1 to many')
    is_repair = db.Column(db.Boolean, default=False, comment='1=ya, 0=tidak')
    biaya = db.Column(db.Float, nullable=True, comment='Besar Biaya yang dikeluarkan (input)')
    created_at = db.Column(db.DateTime, nullable=True)
    updated_at = db.Column(db.DateTime, nullable=True)
    created_by = db.Column(UUID(as_uuid=True), nullable=True)
    updated_by = db.Column(UUID(as_uuid=True), nullable=True)
    variable_header_value = db.Column(db.JSON, nullable=True, comment='[{id: 9, nama: \'sdasdas asdasd\', val: 1}]')
    
    def __init__(self, periode, jenis_parameter, excel_id, created_by):
        """Create a new Cases"""
        self.periode = periode
        self.jenis_parameter = jenis_parameter
        self.excel_id = excel_id
        self.created_by = created_by
