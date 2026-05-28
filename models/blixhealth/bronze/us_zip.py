from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal
from typing import Optional

from sqlalchemy import (
    Boolean,
    DateTime,
    Integer,
    Numeric,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class UsZip(Base):
    __tablename__ = "bronze_us_zip"

    zip: Mapped[str] = mapped_column(String(10), primary_key=True, nullable=False)

    lat: Mapped[Optional[Decimal]] = mapped_column(Numeric(10, 6))
    lng: Mapped[Optional[Decimal]] = mapped_column(Numeric(10, 6))

    city: Mapped[Optional[str]] = mapped_column(String(100))

    state_id: Mapped[Optional[str]] = mapped_column(String(10))
    state_name: Mapped[Optional[str]] = mapped_column(String(100))

    zcta: Mapped[Optional[bool]] = mapped_column(Boolean)

    parent_zcta: Mapped[Optional[str]] = mapped_column(String(10))

    population: Mapped[Optional[int]] = mapped_column(Integer)

    density: Mapped[Optional[Decimal]] = mapped_column(Numeric(10, 2))

    county_fips: Mapped[Optional[str]] = mapped_column(String(10))
    county_name: Mapped[Optional[str]] = mapped_column(String(100))

    county_weights: Mapped[Optional[str]] = mapped_column(Text)

    county_names_all: Mapped[Optional[str]] = mapped_column(Text)

    county_fips_all: Mapped[Optional[str]] = mapped_column(Text)

    imprecise: Mapped[Optional[bool]] = mapped_column(Boolean)

    military: Mapped[Optional[bool]] = mapped_column(Boolean)

    timezone: Mapped[Optional[str]] = mapped_column(String(100))

    ingestion_ts: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )