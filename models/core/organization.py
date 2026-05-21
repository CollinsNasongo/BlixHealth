
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


class Organization(Base):
    __tablename__ = "organization"

    organization_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, nullable=False)
    organization_name: Mapped[str] = mapped_column(String(255), nullable=False)
    organization_type: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    parent_organization_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    source_system_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, nullable=False)
    update_date: Mapped[Optional[time]] = mapped_column(Time, nullable=True)
    load_date: Mapped[time] = mapped_column(Time, nullable=False)
    hash_value: Mapped[Optional[str]] = mapped_column(CHAR(64), nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False)