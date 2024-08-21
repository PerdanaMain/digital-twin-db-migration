"""
Define the Position model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from sqlalchemy.dialects.postgresql import UUID
import uuid


class Role(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "roles"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    deleted_at = db.Column(db.DateTime, nullable=True, server_default=None)

    resources = db.relationship('Resource', secondary='role_has_resources', back_populates='roles')
    users = db.relationship('User', backref='role')

    def __init__(self, name):
        """ Create a new Position """
        self.name = name
