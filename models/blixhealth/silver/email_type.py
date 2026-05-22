
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


class EmailType(Base):
    __tablename__ = "email_type"

    email_type_id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    email_type_name: Mapped[str] = mapped_column(String(255), nullable=False)
    email_type_description: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)