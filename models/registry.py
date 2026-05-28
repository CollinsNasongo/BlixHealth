from models.base import Base

from models.blix_healthcare_db.silver.practitioner import Practitioner
from models.blix_healthcare_db.silver.organization import Organization
from models.blix_healthcare_db.silver.location import Location
from models.blix_healthcare_db.silver.practice import Practice

from models.blix_healthcare_db.silver.state import State
from models.blix_healthcare_db.silver.county import County
from models.blix_healthcare_db.silver.zip_code import ZipCode
from models.blix_healthcare_db.silver.language import Language
from models.blix_healthcare_db.silver.marital_status import MaritalStatus
from models.blix_healthcare_db.silver.preference import Preference
from models.blix_healthcare_db.silver.taxonomy_code import TaxonomyCode
from models.blix_healthcare_db.silver.certification import Certification
from models.blix_healthcare_db.silver.license_type import LicenseType
from models.blix_healthcare_db.silver.practice_type import PracticeType
from models.blix_healthcare_db.silver.email_type import EmailType
from models.blix_healthcare_db.silver.identification_type import IdentificationType
from models.blix_healthcare_db.silver.telephone_number_type import TelephoneNumberType
from models.blix_healthcare_db.silver.healthcare_specialty import HealthcareSpecialty

from models.blix_healthcare_db.silver.practitioner_identification import PractitionerIdentification
from models.blix_healthcare_db.silver.practitioner_license import PractitionerLicense
from models.blix_healthcare_db.silver.practitioner_education import PractitionerEducation
from models.blix_healthcare_db.silver.practitioner_email import PractitionerEmail
from models.blix_healthcare_db.silver.practitioner_telephone_number import PractitionerTelephoneNumber
from models.blix_healthcare_db.silver.practitioner_specialty import PractitionerSpecialty
from models.blix_healthcare_db.silver.practitioner_taxonomy_code import PractitionerTaxonomyCode
from models.blix_healthcare_db.silver.practitioner_language_usage import PractitionerLanguageUsage
from models.blix_healthcare_db.silver.practitioner_practice import PractitionerPractice
from models.blix_healthcare_db.silver.practitioner_certification import PractitionerCertification
from models.blix_healthcare_db.silver.practitioner_marital_status import PractitionerMaritalStatus

from models.blix_healthcare_db.silver.organization_email import OrganizationEmail
from models.blix_healthcare_db.silver.organization_location import OrganizationLocation
from models.blix_healthcare_db.silver.organization_taxonomy_code import OrganizationTaxonomyCode
from models.blix_healthcare_db.silver.organization_telephone_number import OrganizationTelephoneNumber
from models.blix_healthcare_db.silver.practice_role_type import PracticeRoleType
from models.blix_healthcare_db.silver.location_type import LocationType


from models.blix_healthcare_db.bronze.member import Member
from models.blix_healthcare_db.bronze.encounter import Encounter
from models.blix_healthcare_db.bronze.provider import Provider
from models.blix_healthcare_db.bronze.us_zip import UsZip
from models.blix_healthcare_db.bronze.taxonomy import Taxonomy

from models.blix_healthcare_db.audit.data_move_log import DataMoveLog


MODEL_REGISTRY = {

    # Core
    ("blix_healthcare_db", "silver", "practitioner"): Practitioner,
    ("blix_healthcare_db", "silver", "organization"): Organization,
    ("blix_healthcare_db", "silver", "location"): Location,
    ("blix_healthcare_db", "silver", "practice"): Practice,

    # Reference
    ("blix_healthcare_db", "silver", "state"): State,
    ("blix_healthcare_db", "silver", "county"): County,
    ("blix_healthcare_db", "silver", "zip_code"): ZipCode,
    ("blix_healthcare_db", "silver", "language"): Language,
    ("blix_healthcare_db", "silver", "marital_status"): MaritalStatus,
    ("blix_healthcare_db", "silver", "preference"): Preference,
    ("blix_healthcare_db", "silver", "taxonomy_code"): TaxonomyCode,
    ("blix_healthcare_db", "silver", "certification"): Certification,
    ("blix_healthcare_db", "silver", "license_type"): LicenseType,
    ("blix_healthcare_db", "silver", "practice_type"): PracticeType,
    ("blix_healthcare_db", "silver", "email_type"): EmailType,
    ("blix_healthcare_db", "silver", "identification_type"): IdentificationType,
    ("blix_healthcare_db", "silver", "telephone_number_type"): TelephoneNumberType,
    ("blix_healthcare_db", "silver", "healthcare_specialty"): HealthcareSpecialty,
    ("blix_healthcare_db", "silver", "location_type"): LocationType,

    # Practitioner Bridges
    ("blix_healthcare_db", "silver", "practitioner_identification"): PractitionerIdentification,
    ("blix_healthcare_db", "silver", "practitioner_license"): PractitionerLicense,
    ("blix_healthcare_db", "silver", "practitioner_education"): PractitionerEducation,
    ("blix_healthcare_db", "silver", "practitioner_email"): PractitionerEmail,
    ("blix_healthcare_db", "silver", "practitioner_telephone_number"): PractitionerTelephoneNumber,
    ("blix_healthcare_db", "silver", "practitioner_specialty"): PractitionerSpecialty,
    ("blix_healthcare_db", "silver", "practitioner_taxonomy_code"): PractitionerTaxonomyCode,
    ("blix_healthcare_db", "silver", "practitioner_language_usage"): PractitionerLanguageUsage,
    ("blix_healthcare_db", "silver", "practitioner_practice"): PractitionerPractice,
    ("blix_healthcare_db", "silver", "practitioner_certification"): PractitionerCertification,
    ("blix_healthcare_db", "silver", "practitioner_marital_status"): PractitionerMaritalStatus,

    # Organization Bridges
    ("blix_healthcare_db", "silver", "organization_email"): OrganizationEmail,
    ("blix_healthcare_db", "silver", "organization_location"): OrganizationLocation,
    ("blix_healthcare_db", "silver", "organization_taxonomy_code"): OrganizationTaxonomyCode,
    ("blix_healthcare_db", "silver", "organization_telephone_number"): OrganizationTelephoneNumber,
    ("blix_healthcare_db", "silver", "practice_role_type"): PracticeRoleType,
    # Bronze
    ("blix_healthcare_db", "bronze", "member"): Member,
    ("blix_healthcare_db", "bronze", "encounter"): Encounter,
    ("blix_healthcare_db", "bronze", "provider"): Provider,
    ("blix_healthcare_db", "bronze", "us_zip"): UsZip,
    ("blix_healthcare_db", "bronze", "taxonomy"): Taxonomy,

    # Audit
    ("blix_healthcare_db", "audit", "data_move_log"): DataMoveLog,
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