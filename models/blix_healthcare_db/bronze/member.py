from __future__ import annotations

from datetime import datetime, timezone, date
from decimal import Decimal
from typing import Optional

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    Integer,
    Numeric,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class Member(Base):
    __tablename__ = "member"
    __table_args__ = {"schema": "bronze"}

    member_id: Mapped[str] = mapped_column(String(100), primary_key=True, nullable=False)
    subscriber_id: Mapped[Optional[str]] = mapped_column(String(100))
    member_number: Mapped[Optional[str]] = mapped_column(String(100))
    policy_number: Mapped[Optional[str]] = mapped_column(String(100))

    first_name: Mapped[Optional[str]] = mapped_column(String(100))
    middle_name: Mapped[Optional[str]] = mapped_column(String(100))
    last_name: Mapped[Optional[str]] = mapped_column(String(100))
    preferred_name: Mapped[Optional[str]] = mapped_column(String(100))

    gender: Mapped[Optional[str]] = mapped_column(String(50))
    date_of_birth: Mapped[Optional[date]] = mapped_column(Date)
    age: Mapped[Optional[int]] = mapped_column(Integer)

    marital_status: Mapped[Optional[str]] = mapped_column(String(50))
    race: Mapped[Optional[str]] = mapped_column(String(100))
    ethnicity: Mapped[Optional[str]] = mapped_column(String(100))
    nationality: Mapped[Optional[str]] = mapped_column(String(100))

    ssn_last_4: Mapped[Optional[str]] = mapped_column(String(4))

    email_address: Mapped[Optional[str]] = mapped_column(String(255))
    mobile_phone: Mapped[Optional[str]] = mapped_column(String(25))
    home_phone: Mapped[Optional[str]] = mapped_column(String(25))

    address_line_1: Mapped[Optional[str]] = mapped_column(String(255))
    address_line_2: Mapped[Optional[str]] = mapped_column(String(255))
    city: Mapped[Optional[str]] = mapped_column(String(100))
    state: Mapped[Optional[str]] = mapped_column(String(100))
    zip_code: Mapped[Optional[str]] = mapped_column(String(20))
    county: Mapped[Optional[str]] = mapped_column(String(100))
    country: Mapped[Optional[str]] = mapped_column(String(100))

    plan_id: Mapped[Optional[str]] = mapped_column(String(100))
    plan_name: Mapped[Optional[str]] = mapped_column(String(255))
    plan_type: Mapped[Optional[str]] = mapped_column(String(100))
    coverage_tier: Mapped[Optional[str]] = mapped_column(String(100))

    coverage_start_date: Mapped[Optional[date]] = mapped_column(Date)
    coverage_end_date: Mapped[Optional[date]] = mapped_column(Date)

    member_status: Mapped[Optional[str]] = mapped_column(String(50))

    primary_care_provider_id: Mapped[Optional[str]] = mapped_column(String(100))
    primary_care_provider_name: Mapped[Optional[str]] = mapped_column(String(255))

    assigned_practice_id: Mapped[Optional[str]] = mapped_column(String(100))
    assigned_practice_name: Mapped[Optional[str]] = mapped_column(String(255))

    employer_group_id: Mapped[Optional[str]] = mapped_column(String(100))
    employer_group_name: Mapped[Optional[str]] = mapped_column(String(255))

    emergency_contact_name: Mapped[Optional[str]] = mapped_column(String(255))
    emergency_contact_relationship: Mapped[Optional[str]] = mapped_column(String(100))
    emergency_contact_phone: Mapped[Optional[str]] = mapped_column(String(25))

    preferred_language: Mapped[Optional[str]] = mapped_column(String(100))
    secondary_language: Mapped[Optional[str]] = mapped_column(String(100))

    communication_preference: Mapped[Optional[str]] = mapped_column(String(100))

    paperless_enrollment_flag: Mapped[Optional[bool]] = mapped_column(Boolean)

    premium_amount: Mapped[Optional[Decimal]] = mapped_column(Numeric(12, 2))
    copay_amount: Mapped[Optional[Decimal]] = mapped_column(Numeric(12, 2))
    deductible_amount: Mapped[Optional[Decimal]] = mapped_column(Numeric(12, 2))

    chronic_condition_1: Mapped[Optional[str]] = mapped_column(String(255))
    chronic_condition_2: Mapped[Optional[str]] = mapped_column(String(255))
    chronic_condition_3: Mapped[Optional[str]] = mapped_column(String(255))

    smoker_flag: Mapped[Optional[bool]] = mapped_column(Boolean)
    disability_flag: Mapped[Optional[bool]] = mapped_column(Boolean)

    portal_registration_date: Mapped[Optional[date]] = mapped_column(Date)

    record_created_date: Mapped[Optional[datetime]] = mapped_column(DateTime)
    last_update_timestamp: Mapped[Optional[datetime]] = mapped_column(DateTime)

    is_deleted: Mapped[Optional[bool]] = mapped_column(Boolean)

    source_system: Mapped[Optional[str]] = mapped_column(String(100))

    hash_value: Mapped[Optional[str]] = mapped_column(Text)
    ingestion_ts: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(timezone.utc),)