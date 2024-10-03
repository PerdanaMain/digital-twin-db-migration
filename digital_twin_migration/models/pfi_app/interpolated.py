from digital_twin_migration.database import db
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel


class PFIInterpolated(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    __tablename__ = "dl_value_tag_interpolated"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    tag_id = db.Column(
        db.BigInteger, db.ForeignKey("dl_ms_tag.id", ondelete="CASCADE"), nullable=False
    )
    time_stamp = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.Float, nullable=False)
    units_abbreviation = db.Column(db.String(15), nullable=False)
    good = db.Column(db.Boolean, nullable=False)
    questionable = db.Column(db.Boolean, nullable=False)
    substituted = db.Column(db.Boolean, nullable=False)
    annotated = db.Column(db.Boolean, nullable=False)

    tag = db.relationship("PFIMasterTag", back_populates="tag_values", lazy="joined")

    __mapper_args__ = {"eager_defaults": True}
