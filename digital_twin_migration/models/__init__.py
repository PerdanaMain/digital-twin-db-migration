from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .position import Position
from .resource import Resource
from .role import Role
from .role_has_resource import RoleHasResource

