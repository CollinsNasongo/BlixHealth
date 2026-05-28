from models.base import Base

from models.blixhealth.silver.practitioner import Practitioner
from models.blixhealth.silver.organization import Organization
from models.blixhealth.silver.location import Location
from models.blixhealth.silver.practice import Practice

from models.blixhealth.silver.state import State
from models.blixhealth.silver.county import County
from models.blixhealth.silver.zip_code import ZipCode
from models.blixhealth.silver.language import Language
from models.blixhealth.silver.marital_status import MaritalStatus
from models.blixhealth.silver.preference import Preference
from models.blixhealth.silver.taxonomy_code import TaxonomyCode
from models.blixhealth.silver.certification import Certification
from models.blixhealth.silver.license_type import LicenseType
from models.blixhealth.silver.practice_type import PracticeType
from models.blixhealth.silver.email_type import EmailType
from models.blixhealth.silver.identification_type import IdentificationType
from models.blixhealth.silver.telephone_number_type import TelephoneNumberType
from models.blixhealth.silver.healthcare_specialty import HealthcareSpecialty

from models.blixhealth.silver.practitioner_identification import PractitionerIdentification
from models.blixhealth.silver.practitioner_license import PractitionerLicense
from models.blixhealth.silver.practitioner_education import PractitionerEducation
from models.blixhealth.silver.practitioner_email import PractitionerEmail
from models.blixhealth.silver.practitioner_telephone_number import PractitionerTelephoneNumber
from models.blixhealth.silver.practitioner_specialty import PractitionerSpecialty
from models.blixhealth.silver.practitioner_taxonomy_code import PractitionerTaxonomyCode
from models.blixhealth.silver.practitioner_language_usage import PractitionerLanguageUsage
from models.blixhealth.silver.practitioner_practice import PractitionerPractice
from models.blixhealth.silver.practitioner_certification import PractitionerCertification
from models.blixhealth.silver.practitioner_marital_status import PractitionerMaritalStatus

from models.blixhealth.silver.organization_email import OrganizationEmail
from models.blixhealth.silver.organization_location import OrganizationLocation
from models.blixhealth.silver.organization_taxonomy_code import OrganizationTaxonomyCode
from models.blixhealth.silver.organization_telephone_number import OrganizationTelephoneNumber


from models.blixhealth.bronze.member import Member
from models.blixhealth.bronze.encounter import Encounter
from models.blixhealth.bronze.provider import Provider
from models.blixhealth.bronze.us_zip import UsZip
from models.blixhealth.bronze.taxonomy import Taxonomy

from models.blixhealth.audit.data_move_log import DataMoveLog


MODEL_REGISTRY = {

    # Core
    ("blixhealth", "silver", "practitioner"): Practitioner,
    ("blixhealth", "silver", "organization"): Organization,
    ("blixhealth", "silver", "location"): Location,
    ("blixhealth", "silver", "practice"): Practice,

    # Reference
    ("blixhealth", "silver", "state"): State,
    ("blixhealth", "silver", "county"): County,
    ("blixhealth", "silver", "zip_code"): ZipCode,
    ("blixhealth", "silver", "language"): Language,
    ("blixhealth", "silver", "marital_status"): MaritalStatus,
    ("blixhealth", "silver", "preference"): Preference,
    ("blixhealth", "silver", "taxonomy_code"): TaxonomyCode,
    ("blixhealth", "silver", "certification"): Certification,
    ("blixhealth", "silver", "license_type"): LicenseType,
    ("blixhealth", "silver", "practice_type"): PracticeType,
    ("blixhealth", "silver", "email_type"): EmailType,
    ("blixhealth", "silver", "identification_type"): IdentificationType,
    ("blixhealth", "silver", "telephone_number_type"): TelephoneNumberType,
    ("blixhealth", "silver", "healthcare_specialty"): HealthcareSpecialty,

    # Practitioner Bridges
    ("blixhealth", "silver", "practitioner_identification"): PractitionerIdentification,
    ("blixhealth", "silver", "practitioner_license"): PractitionerLicense,
    ("blixhealth", "silver", "practitioner_education"): PractitionerEducation,
    ("blixhealth", "silver", "practitioner_email"): PractitionerEmail,
    ("blixhealth", "silver", "practitioner_telephone_number"): PractitionerTelephoneNumber,
    ("blixhealth", "silver", "practitioner_specialty"): PractitionerSpecialty,
    ("blixhealth", "silver", "practitioner_taxonomy_code"): PractitionerTaxonomyCode,
    ("blixhealth", "silver", "practitioner_language_usage"): PractitionerLanguageUsage,
    ("blixhealth", "silver", "practitioner_practice"): PractitionerPractice,
    ("blixhealth", "silver", "practitioner_certification"): PractitionerCertification,
    ("blixhealth", "silver", "practitioner_marital_status"): PractitionerMaritalStatus,

    # Organization Bridges
    ("blixhealth", "silver", "organization_email"): OrganizationEmail,
    ("blixhealth", "silver", "organization_location"): OrganizationLocation,
    ("blixhealth", "silver", "organization_taxonomy_code"): OrganizationTaxonomyCode,
    ("blixhealth", "silver", "organization_telephone_number"): OrganizationTelephoneNumber,

    # Bronze
    ("blixhealth", "bronze", "member"): Member,
    ("blixhealth", "bronze", "encounter"): Encounter,
    ("blixhealth", "bronze", "provider"): Provider,
    ("blixhealth", "bronze", "us_zip"): UsZip,
    ("blixhealth", "bronze", "taxonomy"): Taxonomy,

    # Audit
    ("blixhealth", "audit", "data_move_log"): DataMoveLog,
}

# =====================================================
# REGISTRY HELPER
# =====================================================

def get_model(database_name: str, schema_name: str, table_name: str) -> type[Base]:

    key = (
        database_name.lower(),
        schema_name.lower(),
        table_name.lower(),
    )

    try:
        return MODEL_REGISTRY[key]

    except KeyError:
        raise KeyError(
            f"Model not registered: "
            f"{database_name}.{schema_name}.{table_name}"
        )