from digital_twin_migration.database import db


class PFIValueTag(db.Model):
    __tablename__ = "pfi_value_tag"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    tag_id = db.Column(
        db.BigInteger, db.ForeignKey("pfi_ms_tag.id", ondelete="CASCADE"), nullable=False
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
