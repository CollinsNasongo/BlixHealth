from models.base import Base

from models.silver.practitioner import Practitioner
from models.silver.organization import Organization
from models.silver.location import Location
from models.silver.practice import Practice

from models.silver.state import State
from models.silver.county import County
from models.silver.zip_code import ZipCode
from models.silver.language import Language
from models.silver.marital_status import MaritalStatus
from models.silver.preference import Preference
from models.silver.taxonomy_code import TaxonomyCode
from models.silver.certification import Certification
from models.silver.license_type import LicenseType
from models.silver.practice_type import PracticeType
from models.silver.email_type import EmailType
from models.silver.identification_type import IdentificationType
from models.silver.telephone_number_type import TelephoneNumberType
from models.silver.healthcare_specialty import HealthcareSpecialty

from models.silver.practitioner_identification import PractitionerIdentification
from models.silver.practitioner_license import PractitionerLicense
from models.silver.practitioner_education import PractitionerEducation
from models.silver.practitioner_email import PractitionerEmail
from models.silver.practitioner_telephone_number import PractitionerTelephoneNumber
from models.silver.practitioner_specialty import PractitionerSpecialty
from models.silver.practitioner_taxonomy_code import PractitionerTaxonomyCode
from models.silver.practitioner_language_usage import PractitionerLanguageUsage
from models.silver.practitioner_practice import PractitionerPractice
from models.silver.practitioner_certification import PractitionerCertification
from models.silver.practitioner_marital_status import PractitionerMaritalStatus

from models.silver.organization_email import OrganizationEmail
from models.silver.organization_location import OrganizationLocation
from models.silver.organization_taxonomy_code import OrganizationTaxonomyCode
from models.silver.organization_telephone_number import OrganizationTelephoneNumber


MODEL_REGISTRY = {

    # Core
    ("silver", "practitioner"): Practitioner,
    ("silver", "organization"): Organization,
    ("silver", "location"): Location,
    ("silver", "practice"): Practice,

    # Reference
    ("silver", "state"): State,
    ("silver", "county"): County,
    ("silver", "zip_code"): ZipCode,
    ("silver", "language"): Language,
    ("silver", "marital_status"): MaritalStatus,
    ("silver", "preference"): Preference,
    ("silver", "taxonomy_code"): TaxonomyCode,
    ("silver", "certification"): Certification,
    ("silver", "license_type"): LicenseType,
    ("silver", "practice_type"): PracticeType,
    ("silver", "email_type"): EmailType,
    ("silver", "identification_type"): IdentificationType,
    ("silver", "telephone_number_type"): TelephoneNumberType,
    ("silver", "healthcare_specialty"): HealthcareSpecialty,

    # Practitioner Bridges
    ("silver", "practitioner_identification"): PractitionerIdentification,
    ("silver", "practitioner_license"): PractitionerLicense,
    ("silver", "practitioner_education"): PractitionerEducation,
    ("silver", "practitioner_email"): PractitionerEmail,
    ("silver", "practitioner_telephone_number"): PractitionerTelephoneNumber,
    ("silver", "practitioner_specialty"): PractitionerSpecialty,
    ("silver", "practitioner_taxonomy_code"): PractitionerTaxonomyCode,
    ("silver", "practitioner_language_usage"): PractitionerLanguageUsage,
    ("silver", "practitioner_practice"): PractitionerPractice,
    ("silver", "practitioner_certification"): PractitionerCertification,
    ("silver", "practitioner_marital_status"): PractitionerMaritalStatus,

    # Organization Bridges
    ("silver", "organization_email"): OrganizationEmail,
    ("silver", "organization_location"): OrganizationLocation,
    ("silver", "organization_taxonomy_code"): OrganizationTaxonomyCode,
    ("silver", "organization_telephone_number"): OrganizationTelephoneNumber,
}

# =====================================================
# REGISTRY HELPER
# =====================================================

def get_model(schema_name: str, table_name: str) -> type[Base]:
    
    key = (
        schema_name.lower(),
        table_name.lower(),
    )

    try:
        return MODEL_REGISTRY[key]

    except KeyError:
        raise KeyError(
            f"Model not registered: {schema_name}.{table_name}"
        )