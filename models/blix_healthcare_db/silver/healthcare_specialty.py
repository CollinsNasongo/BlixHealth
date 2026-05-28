
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


class HealthcareSpecialty(Base):
    __tablename__ = "healthcare_specialty"
    __table_args__ = {"schema": "silver"}

    healthcare_specialty_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    healthcare_specialty_name: Mapped[str] = mapped_column(String(255), nullable=False)
    healthcare_specialty_description: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)