
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


class PractitionerPractice(Base):
    __tablename__ = "practitioner_practice"
    __table_args__ = {"schema": "silver"}

    practitioner_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("silver.practitioner.practitioner_id"), primary_key=True, nullable=False)
    practice_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("silver.practice.practice_id"), primary_key=True, nullable=False)
    preference_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("silver.preference.preference_id"), nullable=True)
    practice_role_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("silver.practice_role_type.practice_role_type_id"), nullable=True)
    period_start_date: Mapped[date] = mapped_column(Date, nullable=False)
    period_end_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)