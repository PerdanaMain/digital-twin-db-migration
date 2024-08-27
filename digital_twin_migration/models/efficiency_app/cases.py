"""
Define the Cases model
"""

from enum import Enum
from uuid import uuid4

from sqlalchemy import BigInteger, Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from digital_twin_migration.database import db
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel
from digital_twin_migration.security.access_control import (
    Allow,
    Authenticated,
    RolePrincipal,
    UserPrincipal,
)

class CasePermission(Enum):
    CREATE = "create"
    READ = "read"
    EDIT = "edit"
    DELETE = "delete"


class Case(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    __tablename__ = "hl_ms_masterdata"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String(300), nullable=False, unique=True)
    kode = Column(String(300), nullable=True)
    seq = Column(Integer, nullable=True)
    group_id = Column(String(300), nullable=True)

    # task_author_id = Column(
    #     BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    # )

    # author = relationship("User", back_populates="tasks", uselist=False, lazy="raise")

    __mapper_args__ = {"eager_defaults": True}

    def __acl__(self):
        # basic_permissions = [CasePermission.READ]
        # self_permissions = [
        #     CasePermission.READ,
        #     CasePermission.EDIT,
        #     CasePermission.DELETE,
        # ]
        all_permissions = list(CasePermission)

        return [
            (Allow, Authenticated, all_permissions),
            (Allow, RolePrincipal("admin"), all_permissions),
        ]
