
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


class PractitionerEmail(Base):
    __tablename__ = "practitioner_email"

    practitioner_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("practitioner.practitioner_id"), primary_key=True, nullable=False)
    email_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("email_type.email_type_id"), primary_key=True, nullable=False)
    email_address: Mapped[str] = mapped_column(String(50), primary_key=True, nullable=False)
    preference_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("preference.preference_id"), nullable=True)
    period_start_date: Mapped[date] = mapped_column(Date, nullable=False)
    period_end_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)