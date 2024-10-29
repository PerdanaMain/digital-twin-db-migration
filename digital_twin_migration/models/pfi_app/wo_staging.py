from digital_twin_migration.database import db
from digital_twin_migration.database.mixins import TimestampMixin
from digital_twin_migration.models.abc import BaseModel, MetaBaseModel


class PFIWOStaging(db.Model, BaseModel, TimestampMixin, metaclass=MetaBaseModel):
    __tablename__ = "dl_wo_staging"

    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    assetnum = db.Column(db.Text, nullable=True)
    description1 = db.Column(db.Text, nullable=True)
    unit = db.Column(db.Integer, nullable=True)
    location = db.Column(db.String(25), nullable=True)
    system_tag = db.Column(db.String(5), nullable=True)
    wonum = db.Column(db.String(10), nullable=True)
    description2 = db.Column(db.Text, nullable=True)
    worktype = db.Column(db.String(5), nullable=True)
    jpnum = db.Column(db.String(10), nullable=True)
    workgroup = db.Column(db.String(30), nullable=True)
    mat_cost_max = db.Column(db.Float, nullable=True)
    serv_cost_max = db.Column(db.Float, nullable=True)
    total_cost_max = db.Column(db.Float, nullable=True)
    wo_start = db.Column(db.DateTime, nullable=True)
    wo_finish = db.Column(db.DateTime, nullable=True)
    wo_start_olah = db.Column(db.DateTime, nullable=True)
    wo_finish_olah = db.Column(db.DateTime, nullable=True)
    reportdate = db.Column(db.DateTime, nullable=True)
    reportdate_olah = db.Column(db.DateTime, nullable=True)
    time_to_event = db.Column(db.Float, nullable=True)
    actstart = db.Column(db.DateTime, nullable=True)
    actfinish = db.Column(db.DateTime, nullable=True)
    actstart_olah = db.Column(db.DateTime, nullable=True)
    actfinish_olah = db.Column(db.DateTime, nullable=True)
    act_repair = db.Column(db.Float, nullable=True)
    jumlah_labor = db.Column(db.Integer, nullable=True)
    need_downtime = db.Column(db.String(100), nullable=True)
    validation_downtime = db.Column(db.String(100), nullable=True)
    down_0_and_not_oh = db.Column(db.Integer, nullable=True)
    downtime = db.Column(db.Integer, nullable=True)
    failure_code = db.Column(db.String(10), nullable=True)
    problem_code = db.Column(db.String(10), nullable=True)
    act_finish_wo_start = db.Column(db.Float, nullable=True)

    __mapper_args__ = {"eager_defaults": True}
