
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


class Practitioner(Base):
    __tablename__ = "practitioner"
    __table_args__ = {"schema": "silver"}

    practitioner_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, nullable=False)
    national_provider_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    first_name: Mapped[str] = mapped_column(String(255), nullable=False)
    middle_name: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    date_of_birth: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    race: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    gender: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    ethnicity: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    nationality: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    source_system_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False)
    update_date: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    load_date: Mapped[time] = mapped_column(Time, nullable=False)
    hash_value: Mapped[Optional[str]] = mapped_column(CHAR(64), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False)