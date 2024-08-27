"""
Define the Position model
"""
from digital_twin_migration.models import db
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy import Index

class RoleHasResource(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "role_has_resources"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    role_id = db.Column(UUID(as_uuid=True), db.ForeignKey('roles.id'), nullable=False)
    resource_id = db.Column(UUID(as_uuid=True), db.ForeignKey('resources.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    deleted_at = db.Column(db.DateTime, nullable=True)
    
    def __init__(self, role_id, resource_id):
        """ Create a new Position """
        self.role_id = role_id
        self.resource_id = resource_id
