
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


class PractitionerCertification(Base):
    __tablename__ = "practitioner_certification"

    practitioner_certification_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, nullable=False)
    practitioner_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("practitioner.practitioner_id"), nullable=False)
    certification_id: Mapped[int] = mapped_column(Integer, ForeignKey("certification.certification_id"), nullable=False)
    preference_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("preference.preference_id"), nullable=True)
    period_start_date: Mapped[date] = mapped_column(Date, nullable=False)
    period_end_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)