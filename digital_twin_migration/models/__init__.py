from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .position import Position
from .resource import Resource
from .role import Role
from .role_has_resource import RoleHasResource

# ? =======================================
from .case_inputs import Case_inputs
from .case_ouputs import Case_outputs
from .cases import Cases
from .excels import Excels
from .units import Units
from .variables import Variables
