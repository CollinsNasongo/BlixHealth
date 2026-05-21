
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


class Location(Base):
    __tablename__ = "location"

    location_id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=True)
    zip_code: Mapped[str] = mapped_column(String(5), ForeignKey("zip_code.zip_code"), nullable=False)
    county_fips_code: Mapped[str] = mapped_column(String(5), ForeignKey("county.county_fips_code"), nullable=False)
    address_line_1: Mapped[str] = mapped_column(String(255), nullable=False)
    address_line_2: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    city: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    longitude: Mapped[Optional[Decimal]] = mapped_column(Numeric(10, 6), nullable=True)
    latitude: Mapped[Optional[Decimal]] = mapped_column(Numeric(9, 6), nullable=True)