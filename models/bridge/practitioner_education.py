
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


class PractitionerEducation(Base):
    __tablename__ = "practitioner_education"

    practitioner_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("practitioner.practitioner_id"), primary_key=True, nullable=False)
    educational_institution_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("organization.organization_id"), primary_key=True, nullable=False)
    education_attainment_level: Mapped[str] = mapped_column(String(50), primary_key=True, nullable=False)
    period_start_date: Mapped[date] = mapped_column(Date, nullable=False)
    period_end_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)