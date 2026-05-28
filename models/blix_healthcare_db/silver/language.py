
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


class Language(Base):
    __tablename__ = "language"
    __table_args__ = {"schema": "silver"}

    language_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    language_code: Mapped[str] = mapped_column(String(50), nullable=False)
    language_name: Mapped[str] = mapped_column(String(255), nullable=False)