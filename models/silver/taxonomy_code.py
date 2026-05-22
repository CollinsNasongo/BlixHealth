
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


class TaxonomyCode(Base):
    __tablename__ = "taxonomy_code"

    taxonomy_code_id: Mapped[int] = mapped_column(BigInteger, primary_key=True, nullable=False)
    taxonomy_code: Mapped[str] = mapped_column(String(50), nullable=False)
    taxonomy_code_grouping: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    taxonomy_code_classification: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    taxonomy_code_specialization: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)
    taxonomy_code_definition: Mapped[Optional[str]] = mapped_column(String(255), nullable=True)