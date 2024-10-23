from digital_twin_migration.database import db
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel


class PFIPSDValue(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    __tablename__ = "dl_psd_value"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    tag_id = db.Column(
        db.BigInteger, db.ForeignKey("dl_ms_tag.id", ondelete="CASCADE"), nullable=False
    )
    psd_value = db.Column(db.Float, nullable=True)
    total_value_1 = db.Column(db.Float, nullable=True)
    total_value_2 = db.Column(db.Float, nullable=True)
    total_value_3 = db.Column(db.Float, nullable=True)
    max_value_1 = db.Column(db.Float, nullable=True)
    max_value_2 = db.Column(db.Float, nullable=True)
    max_value_3 = db.Column(db.Float, nullable=True)

    tag = db.relationship("PFIMasterTag", back_populates="tag_values", lazy="joined")

    __mapper_args__ = {"eager_defaults": True}
