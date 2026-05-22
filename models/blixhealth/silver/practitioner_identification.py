
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


class PractitionerIdentification(Base):
    __tablename__ = "practitioner_identification"

    practitioner_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("practitioner.practitioner_id"), primary_key=True, nullable=False)
    identification_type_id: Mapped[int] = mapped_column(Integer, ForeignKey("identification_type.identification_type_id"), primary_key=True, nullable=False)
    identification_value: Mapped[str] = mapped_column(String(50), primary_key=True, nullable=False)
    period_start_date: Mapped[date] = mapped_column(Date, nullable=False)
    period_end_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    issuing_organization_id: Mapped[Optional[int]] = mapped_column(BigInteger, nullable=True)
    identification_issued_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    identification_expiry_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)