from flask_sqlalchemy import SQLAlchemy
from digital_twin_migration.database import Base

db = SQLAlchemy()

import digital_twin_migration.models.authentication
import digital_twin_migration.models.efficiency_app

# ? =======================================

