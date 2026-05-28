
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


class OrganizationTaxonomyCode(Base):
    __tablename__ = "organization_taxonomy_code"
    __table_args__ = {"schema": "silver"}

    organization_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("silver.organization.organization_id"), primary_key=True, nullable=False)
    taxonomy_code_id: Mapped[int] = mapped_column(Integer, ForeignKey("silver.taxonomy_code.taxonomy_code_id"), primary_key=True, nullable=False)
    preference_id: Mapped[Optional[int]] = mapped_column(Integer, ForeignKey("silver.preference.preference_id"), nullable=True)
    period_start_date: Mapped[date] = mapped_column(Date, nullable=False)
    period_end_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)