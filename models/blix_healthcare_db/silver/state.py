
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


class State(Base):
    __tablename__ = "state"

    state_id: Mapped[Optional[int]] = mapped_column(Integer, primary_key=True, autoincrement=True, nullable=True)
    state_code: Mapped[str] = mapped_column(String(2), nullable=False)
    state_name: Mapped[str] = mapped_column(String(100), nullable=False)
    fips_code: Mapped[str] = mapped_column(String(2), nullable=False)