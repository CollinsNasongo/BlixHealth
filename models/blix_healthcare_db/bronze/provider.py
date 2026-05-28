from __future__ import annotations

from datetime import date, datetime, timezone
from typing import Optional

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    Integer,
    String,
    Text,
)
from sqlalchemy.orm import Mapped, mapped_column

from models.base import Base


class Provider(Base):
    __tablename__ = "provider"
    __table_args__ = {"schema": "bronze"}

    provider_id: Mapped[str] = mapped_column(String(100), primary_key=True, nullable=False)
    internal_provider_id: Mapped[Optional[str]] = mapped_column(String(100))

    npi: Mapped[Optional[str]] = mapped_column(String(20))
    internal_credentialing_id: Mapped[Optional[str]] = mapped_column(String(100))

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

    org_email_address: Mapped[Optional[str]] = mapped_column(String(255))
    personal_email_address: Mapped[Optional[str]] = mapped_column(String(255))

    mobile_phone_1: Mapped[Optional[str]] = mapped_column(String(25))
    mobile_phone_2: Mapped[Optional[str]] = mapped_column(String(25))

    office_phone_1: Mapped[Optional[str]] = mapped_column(String(25))
    office_phone_2: Mapped[Optional[str]] = mapped_column(String(25))

    fax_number_1: Mapped[Optional[str]] = mapped_column(String(25))

    home_address_line_1: Mapped[Optional[str]] = mapped_column(String(255))
    home_address_line_2: Mapped[Optional[str]] = mapped_column(String(255))

    home_city: Mapped[Optional[str]] = mapped_column(String(100))
    home_state: Mapped[Optional[str]] = mapped_column(String(100))
    home_zip_code: Mapped[Optional[str]] = mapped_column(String(20))
    home_county: Mapped[Optional[str]] = mapped_column(String(100))
    home_country: Mapped[Optional[str]] = mapped_column(String(100))

    practice_id: Mapped[Optional[str]] = mapped_column(String(100))
    practice_name: Mapped[Optional[str]] = mapped_column(String(255))
    practice_type: Mapped[Optional[str]] = mapped_column(String(100))

    practice_county: Mapped[Optional[str]] = mapped_column(String(100))
    practice_city: Mapped[Optional[str]] = mapped_column(String(100))
    practice_state: Mapped[Optional[str]] = mapped_column(String(100))
    practice_zip_code: Mapped[Optional[str]] = mapped_column(String(20))

    practice_phone_number: Mapped[Optional[str]] = mapped_column(String(25))
    practice_fax_number: Mapped[Optional[str]] = mapped_column(String(25))

    practice_role: Mapped[Optional[str]] = mapped_column(String(100))
    employment_status: Mapped[Optional[str]] = mapped_column(String(100))

    hire_date: Mapped[Optional[date]] = mapped_column(Date)
    provider_start_date: Mapped[Optional[date]] = mapped_column(Date)

    is_primary_provider: Mapped[Optional[bool]] = mapped_column(Boolean)

    primary_healthcare_service: Mapped[Optional[str]] = mapped_column(String(255))
    secondary_healthcare_service: Mapped[Optional[str]] = mapped_column(String(255))
    tertiary_healthcare_service: Mapped[Optional[str]] = mapped_column(String(255))

    primary_specialty: Mapped[Optional[str]] = mapped_column(String(255))
    secondary_specialty: Mapped[Optional[str]] = mapped_column(String(255))
    tertiary_specialty: Mapped[Optional[str]] = mapped_column(String(255))

    primary_taxonomy_code: Mapped[Optional[str]] = mapped_column(String(50))
    primary_taxonomy_description: Mapped[Optional[str]] = mapped_column(Text)

    secondary_taxonomy_code: Mapped[Optional[str]] = mapped_column(String(50))
    secondary_taxonomy_description: Mapped[Optional[str]] = mapped_column(Text)

    tertiary_taxonomy_code: Mapped[Optional[str]] = mapped_column(String(50))
    tertiary_taxonomy_description: Mapped[Optional[str]] = mapped_column(Text)

    license_type_1: Mapped[Optional[str]] = mapped_column(String(100))
    license_number_1: Mapped[Optional[str]] = mapped_column(String(100))
    issuing_state_1: Mapped[Optional[str]] = mapped_column(String(100))
    license_issue_date_1: Mapped[Optional[date]] = mapped_column(Date)
    license_expiration_date_1: Mapped[Optional[date]] = mapped_column(Date)
    license_status_1: Mapped[Optional[str]] = mapped_column(String(100))

    license_type_2: Mapped[Optional[str]] = mapped_column(String(100))
    license_number_2: Mapped[Optional[str]] = mapped_column(String(100))
    issuing_state_2: Mapped[Optional[str]] = mapped_column(String(100))
    license_issue_date_2: Mapped[Optional[date]] = mapped_column(Date)
    license_expiration_date_2: Mapped[Optional[date]] = mapped_column(Date)
    license_status_2: Mapped[Optional[str]] = mapped_column(String(100))

    highest_degree: Mapped[Optional[str]] = mapped_column(String(100))

    education_institution_1: Mapped[Optional[str]] = mapped_column(String(255))
    education_type_1: Mapped[Optional[str]] = mapped_column(String(100))
    graduation_year_1: Mapped[Optional[int]] = mapped_column(Integer)

    education_institution_2: Mapped[Optional[str]] = mapped_column(String(255))
    education_type_2: Mapped[Optional[str]] = mapped_column(String(100))
    graduation_year_2: Mapped[Optional[int]] = mapped_column(Integer)

    primary_board_certification: Mapped[Optional[str]] = mapped_column(String(255))
    secondary_board_certification: Mapped[Optional[str]] = mapped_column(String(255))

    board_certification_issue_date: Mapped[Optional[date]] = mapped_column(Date)
    board_certification_expiration_date: Mapped[Optional[date]] = mapped_column(Date)

    primary_language: Mapped[Optional[str]] = mapped_column(String(100))
    secondary_language: Mapped[Optional[str]] = mapped_column(String(100))
    tertiary_language: Mapped[Optional[str]] = mapped_column(String(100))

    interpreter_required_flag: Mapped[Optional[bool]] = mapped_column(Boolean)

    provider_portal_registration_date: Mapped[Optional[date]] = mapped_column(Date)

    record_created_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    last_update_timestamp: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    is_deleted: Mapped[Optional[bool]] = mapped_column(Boolean)

    source_system: Mapped[Optional[str]] = mapped_column(String(100))

    hash_value: Mapped[Optional[str]] = mapped_column(Text)

    ingestion_ts: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )