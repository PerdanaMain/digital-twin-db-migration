from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .resource import Resource
from .role import Role
from .role_has_resource import RoleHasResource

# ? =======================================
from .cases import Cases
from .excels import Excels
from .variables import Variables
from .efficiency_transaction import EfficiencyTransaction
from .efficiency_transaction_detail import EfficiencyTransactionDetail
