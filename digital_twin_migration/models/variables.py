"""
Define the Variables model
"""

from . import db
from enum import Enum
from .abc import BaseModel, MetaBaseModel
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Variables(db.Model, BaseModel, metaclass=MetaBaseModel):
    """The Variables model"""

    __tablename__ = "hl_ms_excel_variables"

    # ? Default Columns
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    excel_id = db.Column(UUID(as_uuid=True), db.ForeignKey("hl_ms_excel.id"), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    input_name = db.Column(db.String(255), nullable=False)
    short_name = db.Column(db.String(155))
    satuan = db.Column(db.String(50))
    in_out = db.Column(db.String(25))
    created_by =  db.Column(UUID(as_uuid=True), nullable=False)
    updated_by =  db.Column(UUID(as_uuid=True), nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, nullable=True)

    # ? Relationship
    efficiency_transaction_detail = db.relationship("EfficiencyTransactionDetail", backref="variables", lazy=True)


    def __init__(
        self,category ,excel_id, input_name, short_name, satuan, in_out, created_by
    ):
        """Create a new Variables""",
        self.excel_id = excel_id
        self.input_name = input_name
        self.short_name = short_name
        self.satuan = satuan
        self.in_out = in_out
        self.category = category
        self.created_by = created_by
