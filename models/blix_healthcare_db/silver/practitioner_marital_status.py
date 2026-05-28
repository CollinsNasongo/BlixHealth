
from __future__ import annotations

from datetime import date, time
from decimal import Decimal
from typing import Optional

from sqlalchemy import (
    BigInteger,
    Boolean,
    CHAR,
    Date,
    ForeignKey,
    Integer,
    Numeric,
    String,
    Time,
)
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class PractitionerMaritalStatus(Base):
    __tablename__ = "practitioner_marital_status"
    __table_args__ = {"schema": "silver"}

    practitioner_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("silver.practitioner.practitioner_id"), primary_key=True, nullable=False)
    marital_status_id: Mapped[int] = mapped_column(Integer, ForeignKey("silver.marital_status.marital_status_id"), primary_key=True, nullable=False)
    period_start_date: Mapped[date] = mapped_column(Date, nullable=False)
    period_end_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)