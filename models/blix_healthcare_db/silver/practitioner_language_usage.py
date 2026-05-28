
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


class PractitionerLanguageUsage(Base):
    __tablename__ = "practitioner_language_usage"
    __table_args__ = {"schema": "silver"}

    practitioner_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("silver.practitioner.practitioner_id"), primary_key=True, nullable=False)
    language_id: Mapped[int] = mapped_column(Integer, ForeignKey("silver.language.language_id"), primary_key=True, nullable=False)
    preference_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("silver.preference.preference_id"), nullable=True)
    interpreter_required_flag: Mapped[bool] = mapped_column(Boolean, nullable=False)