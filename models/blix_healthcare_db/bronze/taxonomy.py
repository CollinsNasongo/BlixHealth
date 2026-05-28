from __future__ import annotations

from datetime import datetime, timezone
from typing import Optional

from sqlalchemy import (
    DateTime,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class Taxonomy(Base):
    __tablename__ = "bronze_nucc_taxonomy"

    code: Mapped[str] = mapped_column(String(50), primary_key=True, nullable=False)

    grouping: Mapped[Optional[str]] = mapped_column(String(255))

    classification: Mapped[Optional[str]] = mapped_column(String(255))

    specialization: Mapped[Optional[str]] = mapped_column(String(255))

    definition: Mapped[Optional[str]] = mapped_column(Text)

    notes: Mapped[Optional[str]] = mapped_column(Text)

    display_name: Mapped[Optional[str]] = mapped_column(String(255))

    section: Mapped[Optional[str]] = mapped_column(String(100))

    ingestion_ts: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )