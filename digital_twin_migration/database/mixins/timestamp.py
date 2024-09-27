# pylint: skip-file

from sqlalchemy import Column, DateTime, func
from sqlalchemy.ext.declarative import declared_attr


class TimestampMixin:
    @declared_attr
    def created_at(cls):
        return Column(
            DateTime, default=func.now().op("AT TIME ZONE")("Asia/Jakarta"), nullable=False
        )

    @declared_attr
    def updated_at(cls):
        return Column(
            DateTime,
            default=func.now().op("AT TIME ZONE")("Asia/Jakarta"),
            onupdate=func.now().op("AT TIME ZONE")("Asia/Jakarta"),
            nullable=True,
        )
