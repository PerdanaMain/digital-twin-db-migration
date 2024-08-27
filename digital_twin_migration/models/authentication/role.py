"""
Define the Position model
"""
from enum import Enum
from uuid import uuid4

from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from digital_twin_migration.database import Base
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.security.access_control import (
    Allow,
    Authenticated,
    RolePrincipal,
    UserPrincipal,
)

class Role(Base, TimestampMixin):
    """ The User model """

    __tablename__ = "auth_mr_role"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(300), nullable=False)

    resources = relationship('Resource', secondary='auth_tr_role_resource', back_populates='roles')
    users = relationship('User', backref='role')
    
    __mapper_args__ = {"eager_defaults": True}
