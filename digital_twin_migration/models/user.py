"""
Define the User model
"""
from . import db
from .abc import BaseModel, MetaBaseModel
from sqlalchemy.dialects.postgresql import UUID
import uuid
from flask_bcrypt import generate_password_hash, check_password_hash


class User(db.Model, BaseModel, metaclass=MetaBaseModel):
    """ The User model """

    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(300), nullable=False, unique=True)
    username = db.Column(db.String(300), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    position_id = db.Column(UUID(as_uuid=True), db.ForeignKey('positions.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, server_default=db.func.now())
    deleted_at = db.Column(db.DateTime, nullable=True, server_default=None)

    position = db.relationship('Position', back_populates='users', lazy=True)
    role = db.relationship('Role', back_populates='users', lazy=True)

    def __init__(self, name, email, username, position_id):
        """ Create a new User """
        self.name = name
        self.email = email
        self.username = username
        self.position_id = position_id

    def set_password(self, password):
        self.password = generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return check_password_hash(self.password, password)
