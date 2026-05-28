
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


class County(Base):
    __tablename__ = "county"
    __table_args__ = {"schema": "silver"}

    county_fips_code: Mapped[str] = mapped_column(String(5), primary_key=True, nullable=False)
    state_id: Mapped[int] = mapped_column(Integer, ForeignKey("silver.state.state_id"), nullable=False)
    county_code: Mapped[str] = mapped_column(String(3), nullable=False)
    county_name: Mapped[str] = mapped_column(String(100), nullable=False)