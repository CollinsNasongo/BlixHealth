from __future__ import annotations

from datetime import date, datetime, timezone
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


class Encounter(Base):
    __tablename__ = "bronze_encounter"

    encounter_id: Mapped[str] = mapped_column(String(100), primary_key=True, nullable=False)
    encounter_number: Mapped[Optional[str]] = mapped_column(String(100))

    patient_id: Mapped[Optional[str]] = mapped_column(String(100))
    member_id: Mapped[Optional[str]] = mapped_column(String(100))

    is_blixplan_member: Mapped[Optional[bool]] = mapped_column(Boolean)

    patient_first_name: Mapped[Optional[str]] = mapped_column(String(100))
    patient_last_name: Mapped[Optional[str]] = mapped_column(String(100))
    patient_gender: Mapped[Optional[str]] = mapped_column(String(50))

    patient_date_of_birth: Mapped[Optional[date]] = mapped_column(Date)
    patient_age: Mapped[Optional[int]] = mapped_column(Integer)

    patient_city: Mapped[Optional[str]] = mapped_column(String(100))
    patient_county: Mapped[Optional[str]] = mapped_column(String(100))
    patient_state: Mapped[Optional[str]] = mapped_column(String(100))

    provider_id: Mapped[Optional[str]] = mapped_column(String(100))
    provider_npi: Mapped[Optional[str]] = mapped_column(String(50))
    provider_name: Mapped[Optional[str]] = mapped_column(String(255))

    practice_id: Mapped[Optional[str]] = mapped_column(String(100))
    practice_name: Mapped[Optional[str]] = mapped_column(String(255))
    practice_type: Mapped[Optional[str]] = mapped_column(String(100))

    encounter_date: Mapped[Optional[date]] = mapped_column(Date)

    appointment_datetime: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    check_in_timestamp: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    check_out_timestamp: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    encounter_duration_minutes: Mapped[Optional[int]] = mapped_column(Integer)

    encounter_type: Mapped[Optional[str]] = mapped_column(String(100))
    visit_category: Mapped[Optional[str]] = mapped_column(String(100))
    encounter_status: Mapped[Optional[str]] = mapped_column(String(50))

    chief_complaint: Mapped[Optional[str]] = mapped_column(Text)
    visit_reason: Mapped[Optional[str]] = mapped_column(Text)

    primary_diagnosis_code: Mapped[Optional[str]] = mapped_column(String(50))
    primary_diagnosis_description: Mapped[Optional[str]] = mapped_column(Text)

    secondary_diagnosis_code: Mapped[Optional[str]] = mapped_column(String(50))
    secondary_diagnosis_description: Mapped[Optional[str]] = mapped_column(Text)

    primary_procedure_code: Mapped[Optional[str]] = mapped_column(String(50))
    primary_procedure_description: Mapped[Optional[str]] = mapped_column(Text)

    secondary_procedure_code: Mapped[Optional[str]] = mapped_column(String(50))
    secondary_procedure_description: Mapped[Optional[str]] = mapped_column(Text)

    primary_healthcare_service: Mapped[Optional[str]] = mapped_column(String(255))
    provider_specialty: Mapped[Optional[str]] = mapped_column(String(255))

    telehealth_flag: Mapped[Optional[bool]] = mapped_column(Boolean)
    referral_flag: Mapped[Optional[bool]] = mapped_column(Boolean)

    blood_pressure: Mapped[Optional[str]] = mapped_column(String(20))
    heart_rate: Mapped[Optional[int]] = mapped_column(Integer)

    temperature: Mapped[Optional[Decimal]] = mapped_column(Numeric(5, 2))
    bmi: Mapped[Optional[Decimal]] = mapped_column(Numeric(5, 2))

    disposition: Mapped[Optional[str]] = mapped_column(String(255))

    insurance_plan_name: Mapped[Optional[str]] = mapped_column(String(255))
    payer_type: Mapped[Optional[str]] = mapped_column(String(100))

    claim_id: Mapped[Optional[str]] = mapped_column(String(100))
    claim_status: Mapped[Optional[str]] = mapped_column(String(100))

    billed_amount: Mapped[Optional[Decimal]] = mapped_column(Numeric(12, 2))
    allowed_amount: Mapped[Optional[Decimal]] = mapped_column(Numeric(12, 2))
    paid_amount: Mapped[Optional[Decimal]] = mapped_column(Numeric(12, 2))
    patient_responsibility_amount: Mapped[Optional[Decimal]] = mapped_column(Numeric(12, 2))
    copay_collected: Mapped[Optional[Decimal]] = mapped_column(Numeric(12, 2))

    admission_flag: Mapped[Optional[bool]] = mapped_column(Boolean)
    readmission_flag: Mapped[Optional[bool]] = mapped_column(Boolean)

    record_created_date: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))
    last_update_timestamp: Mapped[Optional[datetime]] = mapped_column(DateTime(timezone=True))

    source_system: Mapped[Optional[str]] = mapped_column(String(100))

    is_deleted: Mapped[Optional[bool]] = mapped_column(Boolean)

    ingestion_ts: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )