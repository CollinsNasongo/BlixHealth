
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


class ZipCode(Base):
    __tablename__ = "zip_code"
    __table_args__ = {"schema": "silver"}

    zip_code: Mapped[str] = mapped_column(String(5), primary_key=True, nullable=False)
    state_id: Mapped[int] = mapped_column(Integer, ForeignKey("state.state_id"), nullable=False)