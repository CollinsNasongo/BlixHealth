
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


class Practice(Base):
    __tablename__ = "practice"
    __table_args__ = {"schema": "silver"}

    practice_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, nullable=False)
    organization_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("silver.organization.organization_id"), nullable=False)
    practice_type_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("silver.practice_type.practice_type_id"), nullable=True)
    practice_name: Mapped[str] = mapped_column(String(255), nullable=False)