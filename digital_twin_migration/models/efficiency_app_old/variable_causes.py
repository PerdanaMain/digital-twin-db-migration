"""
Define the Cases model
"""

from digital_twin_migration.models import db
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import Index


class VariableCauses(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Variable Causes model"""

    __tablename__ = "hl_ms_excel_variables_cause"

    # ? Column Defaults
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    parent_id = db.Column(UUID(as_uuid=True), db.ForeignKey('hl_ms_excel_variables_cause.id'),
                          nullable=True, comment='ref to id table ini sendiri (recursive)', default=id)
    variable_id = db.Column(UUID(as_uuid=True), db.ForeignKey(
        'hl_ms_excel_variables.id'), nullable=False)
    nama = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, nullable=True,
                           server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=True)
    created_by = db.Column(db.String(100), nullable=True)
    updated_by = db.Column(db.String(100), nullable=True)
    
    root_causes = db.relationship("EfficiencyTransactionDetailRootCauses", backref="variable_causes", lazy=True)

    def __init__(self, variable_id, nama, created_by):
        """Create a new Cases"""
        self.variable_id = variable_id
        self.nama = nama
        self.created_by = created_by
