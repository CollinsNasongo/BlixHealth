
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


class PractitionerLicense(Base):
    __tablename__ = "practitioner_license"

    practitioner_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("practitioner.practitioner_id"), primary_key=True, nullable=False)
    licensing_organization_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("organization.organization_id"), primary_key=True, nullable=False)
    license_number: Mapped[str] = mapped_column(String(50), primary_key=True, nullable=False)
    license_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("license_type.license_type_id"), nullable=False)
    state_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("state.state_id"), nullable=True)
    period_start_date: Mapped[date] = mapped_column(Date, nullable=False)
    period_end_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)