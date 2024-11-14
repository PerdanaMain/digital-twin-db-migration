from digital_twin_migration.database import db
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel


class Predict(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    __tablename__ = "dl_predict_tag"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    tag_id = db.Column(
        db.BigInteger, db.ForeignKey("dl_ms_tag.id", ondelete="CASCADE"), nullable=False
    )
    time_stamp = db.Column(db.DateTime, nullable=False)
    value = db.Column(db.Float, nullable=False)

    tag = db.relationship("PFIMasterTag", back_populates="tag_values_interpolated", lazy="joined")

    __mapper_args__ = {"eager_defaults": True}
