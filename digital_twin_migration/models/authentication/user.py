"""
Define the User model
"""
from enum import Enum
from uuid import uuid4

from sqlalchemy import BigInteger, Boolean, Column, DateTime, ForeignKey, Index, Integer, String
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
from flask_bcrypt import generate_password_hash, check_password_hash


class User(Base, TimestampMixin):
    """ The User model """

    __tablename__ = "auth_mr_user"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(300), nullable=False)
    email = Column(String(300), nullable=False, unique=True)
    username = Column(String(300), nullable=False, unique=True)
    password = Column(String(300), nullable=False)
    position = Column(String(300), nullable=False)
    role_id = Column(UUID(as_uuid=True), ForeignKey(
        'auth_mr_role.id'), nullable=False)

    __table_args__ = (
        Index('users_name_email_username_idx', 'name', 'email', 'username'),
    )
    
    __mapper_args__ = {"eager_defaults": True}

    def set_password(self, password):
        self.password = generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.password, password)
