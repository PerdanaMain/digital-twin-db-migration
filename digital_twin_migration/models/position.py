"""
Define the Position model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from sqlalchemy.dialects.postgresql import UUID
import uuid

class Position(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "positions"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    deleted_at = db.Column(db.DateTime, nullable=True, server_default=None)
    
    users = db.relationship('User', back_populates='position', lazy=True)

    def __init__(self, title):
        """ Create a new Position """
        self.title = title 
    

