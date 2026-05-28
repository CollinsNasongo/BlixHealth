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


class DataMoveLog(Base):
    __tablename__ = "audit_ingestion_log"

    run_id: Mapped[str] = mapped_column(String(100), primary_key=True, nullable=False)

    dataset: Mapped[Optional[str]] = mapped_column(String(255))

    source_file: Mapped[Optional[str]] = mapped_column(String(500))

    target_file: Mapped[Optional[str]] = mapped_column(String(500))

    status: Mapped[Optional[str]] = mapped_column(String(50))

    records_processed: Mapped[Optional[int]] = mapped_column(Integer)

    error_message: Mapped[Optional[str]] = mapped_column(Text)

    run_timestamp: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))