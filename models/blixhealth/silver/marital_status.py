
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


class MaritalStatus(Base):
    __tablename__ = "marital_status"

    marital_status_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    marital_status_name: Mapped[str] = mapped_column(String(255), nullable=False)
    marital_status_description: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)