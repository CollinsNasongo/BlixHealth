--
-- ER/Studio Data Architect SQL Code Generation
-- Project :      BlixSilverModel.DM1
--
-- Date Created : Thursday, May 21, 2026 18:09:36
-- Target DBMS : PostgreSQL 10.x-12.x
--

-- 
-- TABLE: certification 
--

CREATE TABLE certification(
    certification_id                    integer         NOT NULL,
    certificate_issuing_organization    varchar(255)    NOT NULL,
    certification_name                  varchar(255)    NOT NULL,
    certification_description           varchar(255),
    CONSTRAINT PK33 PRIMARY KEY (certification_id)
)
;



-- 
-- TABLE: county 
--

CREATE TABLE county(
    county_fips_code    varchar(5)      NOT NULL,
    state_id            integer         NOT NULL,
    county_code         varchar(3)      NOT NULL,
    county_name         varchar(100)    NOT NULL,
    CONSTRAINT PK3 PRIMARY KEY (county_fips_code)
)
;



-- 
-- TABLE: email_type 
--

CREATE TABLE email_type(
    email_type_id             integer         NOT NULL,
    email_type_name           varchar(255)    NOT NULL,
    email_type_description    varchar(255),
    CONSTRAINT PK32 PRIMARY KEY (email_type_id)
)
;



-- 
-- TABLE: healthcare_specialty 
--

CREATE TABLE healthcare_specialty(
    healthcare_specialty_id             integer         NOT NULL,
    healthcare_specialty_name           varchar(255)    NOT NULL,
    healthcare_specialty_description    varchar(255),
    CONSTRAINT PK31 PRIMARY KEY (healthcare_specialty_id)
)
;



-- 
-- TABLE: identification_type 
--

CREATE TABLE identification_type(
    identification_type_id             integer         NOT NULL,
    identification_type_code           varchar(50)     NOT NULL,
    identification_type_name           varchar(255)    NOT NULL,
    identification_type_description    varchar(255),
    CONSTRAINT PK30 PRIMARY KEY (identification_type_id)
)
;



-- 
-- TABLE: language 
--

CREATE TABLE language(
    language_id      integer         NOT NULL,
    language_code    varchar(50)     NOT NULL,
    language_name    varchar(255)    NOT NULL,
    CONSTRAINT PK29 PRIMARY KEY (language_id)
)
;



-- 
-- TABLE: license_type 
--

CREATE TABLE license_type(
    license_type_id             integer         NOT NULL,
    license_type_name           varchar(255)    NOT NULL,
    license_type_description    varchar(255),
    CONSTRAINT PK28 PRIMARY KEY (license_type_id)
)
;



-- 
-- TABLE: location 
--

CREATE TABLE location(
    location_id         integer           GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    zip_code            varchar(5)        NOT NULL,
    county_fips_code    varchar(5)        NOT NULL,
    address_line_1      varchar(255)      NOT NULL,
    address_line_2      varchar(255),
    city                varchar(100),
    longitude           decimal(10, 6),
    latitude            decimal(9, 6),
    CONSTRAINT PK4 PRIMARY KEY (location_id)
)
;



-- 
-- TABLE: location_type 
--

CREATE TABLE location_type(
    location_type_id             integer         NOT NULL,
    location_type_name           varchar(255)    NOT NULL,
    location_type_description    varchar(255),
    CONSTRAINT PK27 PRIMARY KEY (location_type_id)
)
;



-- 
-- TABLE: marital_status 
--

CREATE TABLE marital_status(
    marital_status_id             integer         NOT NULL,
    marital_status_name           varchar(255)    NOT NULL,
    marital_status_description    varchar(255),
    CONSTRAINT PK26 PRIMARY KEY (marital_status_id)
)
;



-- 
-- TABLE: organization 
--

CREATE TABLE organization(
    organization_id           bigint                       NOT NULL,
    organization_name         varchar(255)                 NOT NULL,
    organization_type         varchar(255),
    parent_organization_id    bigint,
    source_system_id          bigint,
    is_deleted                boolean                      NOT NULL,
    update_date               time without time zone(6),
    load_date                 time without time zone(6)    NOT NULL,
    hash_value                character(64),
    is_active                 boolean                      NOT NULL,
    CONSTRAINT PK25 PRIMARY KEY (organization_id)
)
;



-- 
-- TABLE: organization_email 
--

CREATE TABLE organization_email(
    organization_id      bigint         NOT NULL,
    email_type_id        integer        NOT NULL,
    email_address        varchar(50)    NOT NULL,
    preference_id        integer,
    period_start_date    date           NOT NULL,
    period_end_date      date,
    CONSTRAINT PK24 PRIMARY KEY (organization_id, email_type_id, email_address)
)
;



-- 
-- TABLE: organization_location 
--

CREATE TABLE organization_location(
    organization_id      bigint     NOT NULL,
    location_id          integer    NOT NULL,
    location_type_id     integer    NOT NULL,
    preference_id        integer,
    period_start_date    date       NOT NULL,
    period_end_date      date,
    CONSTRAINT PK34 PRIMARY KEY (organization_id, location_id)
)
;



-- 
-- TABLE: organization_taxonomy_code 
--

CREATE TABLE organization_taxonomy_code(
    organization_id      bigint     NOT NULL,
    taxonomy_code_id     bigint     NOT NULL,
    preference_id        integer,
    period_start_date    date       NOT NULL,
    period_end_date      date,
    CONSTRAINT PK23 PRIMARY KEY (organization_id, taxonomy_code_id)
)
;



-- 
-- TABLE: organization_telephone_number 
--

CREATE TABLE organization_telephone_number(
    organization_id             bigint         NOT NULL,
    telephone_number_type_id    bigint         NOT NULL,
    telephone_number            varchar(50)    NOT NULL,
    preference_id               integer,
    period_start_date           date           NOT NULL,
    period_end_date             date,
    CONSTRAINT PK22 PRIMARY KEY (organization_id, telephone_number_type_id, telephone_number)
)
;



-- 
-- TABLE: practice 
--

CREATE TABLE practice(
    practice_id         bigint          NOT NULL,
    organization_id     bigint          NOT NULL,
    practice_type_id    integer,
    practice_name       varchar(255)    NOT NULL,
    CONSTRAINT PK21 PRIMARY KEY (practice_id)
)
;



-- 
-- TABLE: practice_type 
--

CREATE TABLE practice_type(
    practice_type_id             integer         NOT NULL,
    practice_type_name           varchar(255)    NOT NULL,
    practice_type_description    varchar(255),
    CONSTRAINT PK20 PRIMARY KEY (practice_type_id)
)
;



-- 
-- TABLE: practitioner 
--

CREATE TABLE practitioner(
    practitioner_id         bigint                       NOT NULL,
    national_provider_id    bigint,
    first_name              varchar(255)                 NOT NULL,
    middle_name             varchar(255),
    last_name               varchar(255)                 NOT NULL,
    date_of_birth           date,
    race                    varchar(255),
    gender                  varchar(255),
    ethnicity               varchar(255),
    nationality             varchar(255),
    source_system_id        bigint,
    is_deleted              boolean                      NOT NULL,
    update_date             time without time zone(6),
    load_date               time without time zone(6)    NOT NULL,
    hash_value              character(64),
    is_active               boolean                      NOT NULL,
    CONSTRAINT PK19 PRIMARY KEY (practitioner_id)
)
;



-- 
-- TABLE: practitioner_certification 
--

CREATE TABLE practitioner_certification(
    practitioner_certification_id    bigint     NOT NULL,
    practitioner_id                  bigint     NOT NULL,
    certification_id                 integer    NOT NULL,
    preference_id                    integer,
    period_start_date                date       NOT NULL,
    period_end_date                  date,
    CONSTRAINT PK18 PRIMARY KEY (practitioner_certification_id)
)
;



-- 
-- TABLE: practitioner_education 
--

CREATE TABLE practitioner_education(
    practitioner_id               bigint         NOT NULL,
    educational_institution_id    bigint         NOT NULL,
    education_attainment_level    varchar(50)    NOT NULL,
    period_start_date             date           NOT NULL,
    period_end_date               date,
    CONSTRAINT PK17 PRIMARY KEY (practitioner_id, educational_institution_id, education_attainment_level)
)
;



-- 
-- TABLE: practitioner_email 
--

CREATE TABLE practitioner_email(
    practitioner_id      bigint         NOT NULL,
    email_type_id        integer        NOT NULL,
    email_address        varchar(50)    NOT NULL,
    preference_id        integer,
    period_start_date    date           NOT NULL,
    period_end_date      date,
    CONSTRAINT PK16 PRIMARY KEY (practitioner_id, email_type_id, email_address)
)
;



-- 
-- TABLE: practitioner_identification 
--

CREATE TABLE practitioner_identification(
    practitioner_id               bigint         NOT NULL,
    identification_type_id        integer        NOT NULL,
    identification_value          varchar(50)    NOT NULL,
    period_start_date             date           NOT NULL,
    period_end_date               date,
    issuing_organization_id       bigint,
    identification_issued_date    date,
    identification_expiry_date    date,
    CONSTRAINT PK15 PRIMARY KEY (practitioner_id, identification_type_id, identification_value)
)
;



-- 
-- TABLE: practitioner_language_usage 
--

CREATE TABLE practitioner_language_usage(
    practitioner_id              bigint     NOT NULL,
    language_id                  integer    NOT NULL,
    preference_id                integer,
    interpreter_required_flag    boolean    NOT NULL,
    CONSTRAINT PK14 PRIMARY KEY (practitioner_id, language_id)
)
;



-- 
-- TABLE: practitioner_license 
--

CREATE TABLE practitioner_license(
    practitioner_id              bigint         NOT NULL,
    licensing_organization_id    bigint         NOT NULL,
    license_number               varchar(50)    NOT NULL,
    license_type_id              integer        NOT NULL,
    state_id                     integer,
    period_start_date            date           NOT NULL,
    period_end_date              date,
    CONSTRAINT PK20 PRIMARY KEY (practitioner_id, licensing_organization_id, license_number)
)
;



-- 
-- TABLE: practitioner_marital_status 
--

CREATE TABLE practitioner_marital_status(
    practitioner_id      bigint     NOT NULL,
    marital_status_id    integer    NOT NULL,
    period_start_date    date       NOT NULL,
    period_end_date      date,
    CONSTRAINT PK12 PRIMARY KEY (practitioner_id, marital_status_id)
)
;



-- 
-- TABLE: practitioner_practice 
--

CREATE TABLE practitioner_practice(
    practitioner_id          bigint     NOT NULL,
    practice_id              bigint     NOT NULL,
    preference_id            integer,
    practice_role_type_id    bigint,
    period_start_date        date       NOT NULL,
    period_end_date          date,
    CONSTRAINT PK18 PRIMARY KEY (practitioner_id, practice_id)
)
;



-- 
-- TABLE: practitioner_specialty 
--

CREATE TABLE practitioner_specialty(
    practitioner_id            bigint     NOT NULL,
    healthcare_specialty_id    integer    NOT NULL,
    preference_id              integer,
    period_start_date          date       NOT NULL,
    period_end_date            date,
    CONSTRAINT PK10 PRIMARY KEY (practitioner_id, healthcare_specialty_id)
)
;



-- 
-- TABLE: practitioner_taxonomy_code 
--

CREATE TABLE practitioner_taxonomy_code(
    practitioner_id      bigint     NOT NULL,
    taxonomy_code_id     bigint     NOT NULL,
    preference_id        integer,
    period_start_date    date       NOT NULL,
    period_end_date      date,
    CONSTRAINT PK9 PRIMARY KEY (practitioner_id, taxonomy_code_id)
)
;



-- 
-- TABLE: practitioner_telephone_number 
--

CREATE TABLE practitioner_telephone_number(
    practitioner_id             bigint         NOT NULL,
    telephone_number_type_id    bigint         NOT NULL,
    telephone_number            varchar(50)    NOT NULL,
    preference_id               integer,
    period_start_date           date           NOT NULL,
    period_end_date             date,
    CONSTRAINT PK8 PRIMARY KEY (practitioner_id, telephone_number_type_id, telephone_number)
)
;



-- 
-- TABLE: preference 
--

CREATE TABLE preference(
    preference_id             integer         NOT NULL,
    preference_name           varchar(255)    NOT NULL,
    preference_description    varchar(255),
    CONSTRAINT PK7 PRIMARY KEY (preference_id)
)
;



-- 
-- TABLE: state 
--

CREATE TABLE state(
    state_id      integer         GENERATED ALWAYS AS IDENTITY (START WITH 1 INCREMENT BY 1),
    state_code    varchar(2)      NOT NULL,
    state_name    varchar(100)    NOT NULL,
    fips_code     varchar(2)      NOT NULL,
    CONSTRAINT PK2_1 PRIMARY KEY (state_id)
)
;



-- 
-- TABLE: taxonomy_code 
--

CREATE TABLE taxonomy_code(
    taxonomy_code_id                bigint          NOT NULL,
    taxonomy_code                   varchar(50)     NOT NULL,
    taxonomy_code_grouping          varchar(255),
    taxonomy_code_classification    varchar(255),
    taxonomy_code_specialization    varchar(255),
    taxonomy_code_definition        varchar(255),
    CONSTRAINT PK6 PRIMARY KEY (taxonomy_code_id)
)
;



-- 
-- TABLE: telephone_number_type 
--

CREATE TABLE telephone_number_type(
    telephone_number_type_id             bigint          NOT NULL,
    telephone_number_type_name           varchar(255)    NOT NULL,
    telephone_number_type_description    varchar(255),
    CONSTRAINT PK5 PRIMARY KEY (telephone_number_type_id)
)
;



-- 
-- TABLE: zip_code 
--

CREATE TABLE zip_code(
    zip_code    varchar(5)    NOT NULL,
    state_id    integer       NOT NULL,
    CONSTRAINT PK2 PRIMARY KEY (zip_code)
)
;



-- 
-- TABLE: county 
--

ALTER TABLE county ADD CONSTRAINT Refstate6 
    FOREIGN KEY (state_id)
    REFERENCES state(state_id)
;


-- 
-- TABLE: location 
--

ALTER TABLE location ADD CONSTRAINT Refzip_code1 
    FOREIGN KEY (zip_code)
    REFERENCES zip_code(zip_code)
;

ALTER TABLE location ADD CONSTRAINT Refcounty4 
    FOREIGN KEY (county_fips_code)
    REFERENCES county(county_fips_code)
;


-- 
-- TABLE: organization_email 
--

ALTER TABLE organization_email ADD CONSTRAINT Reforganization21 
    FOREIGN KEY (organization_id)
    REFERENCES organization(organization_id)
;

ALTER TABLE organization_email ADD CONSTRAINT Refemail_type22 
    FOREIGN KEY (email_type_id)
    REFERENCES email_type(email_type_id)
;

ALTER TABLE organization_email ADD CONSTRAINT Refpreference48 
    FOREIGN KEY (preference_id)
    REFERENCES preference(preference_id)
;


-- 
-- TABLE: organization_location 
--

ALTER TABLE organization_location ADD CONSTRAINT Reforganization43 
    FOREIGN KEY (organization_id)
    REFERENCES organization(organization_id)
;

ALTER TABLE organization_location ADD CONSTRAINT Reflocation45 
    FOREIGN KEY (location_id)
    REFERENCES location(location_id)
;

ALTER TABLE organization_location ADD CONSTRAINT Reflocation_type46 
    FOREIGN KEY (location_type_id)
    REFERENCES location_type(location_type_id)
;

ALTER TABLE organization_location ADD CONSTRAINT Refpreference50 
    FOREIGN KEY (preference_id)
    REFERENCES preference(preference_id)
;


-- 
-- TABLE: organization_taxonomy_code 
--

ALTER TABLE organization_taxonomy_code ADD CONSTRAINT Reftaxonomy_code34 
    FOREIGN KEY (taxonomy_code_id)
    REFERENCES taxonomy_code(taxonomy_code_id)
;

ALTER TABLE organization_taxonomy_code ADD CONSTRAINT Reforganization42 
    FOREIGN KEY (organization_id)
    REFERENCES organization(organization_id)
;

ALTER TABLE organization_taxonomy_code ADD CONSTRAINT Refpreference51 
    FOREIGN KEY (preference_id)
    REFERENCES preference(preference_id)
;


-- 
-- TABLE: organization_telephone_number 
--

ALTER TABLE organization_telephone_number ADD CONSTRAINT Reftelephone_number_type29 
    FOREIGN KEY (telephone_number_type_id)
    REFERENCES telephone_number_type(telephone_number_type_id)
;

ALTER TABLE organization_telephone_number ADD CONSTRAINT Reforganization38 
    FOREIGN KEY (organization_id)
    REFERENCES organization(organization_id)
;

ALTER TABLE organization_telephone_number ADD CONSTRAINT Refpreference52 
    FOREIGN KEY (preference_id)
    REFERENCES preference(preference_id)
;


-- 
-- TABLE: practice 
--

ALTER TABLE practice ADD CONSTRAINT Reforganization7 
    FOREIGN KEY (organization_id)
    REFERENCES organization(organization_id)
;

ALTER TABLE practice ADD CONSTRAINT Refpractice_type8 
    FOREIGN KEY (practice_type_id)
    REFERENCES practice_type(practice_type_id)
;


-- 
-- TABLE: practitioner_certification 
--

ALTER TABLE practitioner_certification ADD CONSTRAINT Refpractitioner23 
    FOREIGN KEY (practitioner_id)
    REFERENCES practitioner(practitioner_id)
;

ALTER TABLE practitioner_certification ADD CONSTRAINT Refcertification24 
    FOREIGN KEY (certification_id)
    REFERENCES certification(certification_id)
;

ALTER TABLE practitioner_certification ADD CONSTRAINT Refpreference53 
    FOREIGN KEY (preference_id)
    REFERENCES preference(preference_id)
;


-- 
-- TABLE: practitioner_education 
--

ALTER TABLE practitioner_education ADD CONSTRAINT Reforganization31 
    FOREIGN KEY (educational_institution_id)
    REFERENCES organization(organization_id)
;

ALTER TABLE practitioner_education ADD CONSTRAINT Refpractitioner41 
    FOREIGN KEY (practitioner_id)
    REFERENCES practitioner(practitioner_id)
;


-- 
-- TABLE: practitioner_email 
--

ALTER TABLE practitioner_email ADD CONSTRAINT Refpractitioner26 
    FOREIGN KEY (practitioner_id)
    REFERENCES practitioner(practitioner_id)
;

ALTER TABLE practitioner_email ADD CONSTRAINT Refemail_type27 
    FOREIGN KEY (email_type_id)
    REFERENCES email_type(email_type_id)
;

ALTER TABLE practitioner_email ADD CONSTRAINT Refpreference54 
    FOREIGN KEY (preference_id)
    REFERENCES preference(preference_id)
;


-- 
-- TABLE: practitioner_identification 
--

ALTER TABLE practitioner_identification ADD CONSTRAINT Refpractitioner19 
    FOREIGN KEY (practitioner_id)
    REFERENCES practitioner(practitioner_id)
;

ALTER TABLE practitioner_identification ADD CONSTRAINT Refidentification_type20 
    FOREIGN KEY (identification_type_id)
    REFERENCES identification_type(identification_type_id)
;


-- 
-- TABLE: practitioner_language_usage 
--

ALTER TABLE practitioner_language_usage ADD CONSTRAINT Refpractitioner16 
    FOREIGN KEY (practitioner_id)
    REFERENCES practitioner(practitioner_id)
;

ALTER TABLE practitioner_language_usage ADD CONSTRAINT Reflanguage17 
    FOREIGN KEY (language_id)
    REFERENCES language(language_id)
;

ALTER TABLE practitioner_language_usage ADD CONSTRAINT Refpreference18 
    FOREIGN KEY (preference_id)
    REFERENCES preference(preference_id)
;


-- 
-- TABLE: practitioner_license 
--

ALTER TABLE practitioner_license ADD CONSTRAINT Refpractitioner12 
    FOREIGN KEY (practitioner_id)
    REFERENCES practitioner(practitioner_id)
;

ALTER TABLE practitioner_license ADD CONSTRAINT Reforganization13 
    FOREIGN KEY (licensing_organization_id)
    REFERENCES organization(organization_id)
;

ALTER TABLE practitioner_license ADD CONSTRAINT Reflicense_type14 
    FOREIGN KEY (license_type_id)
    REFERENCES license_type(license_type_id)
;

ALTER TABLE practitioner_license ADD CONSTRAINT Refstate15 
    FOREIGN KEY (state_id)
    REFERENCES state(state_id)
;


-- 
-- TABLE: practitioner_marital_status 
--

ALTER TABLE practitioner_marital_status ADD CONSTRAINT Refmarital_status30 
    FOREIGN KEY (marital_status_id)
    REFERENCES marital_status(marital_status_id)
;

ALTER TABLE practitioner_marital_status ADD CONSTRAINT Refpractitioner40 
    FOREIGN KEY (practitioner_id)
    REFERENCES practitioner(practitioner_id)
;


-- 
-- TABLE: practitioner_practice 
--

ALTER TABLE practitioner_practice ADD CONSTRAINT Refpractitioner10 
    FOREIGN KEY (practitioner_id)
    REFERENCES practitioner(practitioner_id)
;

ALTER TABLE practitioner_practice ADD CONSTRAINT Refpractice11 
    FOREIGN KEY (practice_id)
    REFERENCES practice(practice_id)
;

ALTER TABLE practitioner_practice ADD CONSTRAINT Refpreference55 
    FOREIGN KEY (preference_id)
    REFERENCES preference(preference_id)
;


-- 
-- TABLE: practitioner_specialty 
--

ALTER TABLE practitioner_specialty ADD CONSTRAINT Refhealthcare_specialty35 
    FOREIGN KEY (healthcare_specialty_id)
    REFERENCES healthcare_specialty(healthcare_specialty_id)
;

ALTER TABLE practitioner_specialty ADD CONSTRAINT Refpractitioner36 
    FOREIGN KEY (practitioner_id)
    REFERENCES practitioner(practitioner_id)
;

ALTER TABLE practitioner_specialty ADD CONSTRAINT Refpreference56 
    FOREIGN KEY (preference_id)
    REFERENCES preference(preference_id)
;


-- 
-- TABLE: practitioner_taxonomy_code 
--

ALTER TABLE practitioner_taxonomy_code ADD CONSTRAINT Refpractitioner32 
    FOREIGN KEY (practitioner_id)
    REFERENCES practitioner(practitioner_id)
;

ALTER TABLE practitioner_taxonomy_code ADD CONSTRAINT Reftaxonomy_code33 
    FOREIGN KEY (taxonomy_code_id)
    REFERENCES taxonomy_code(taxonomy_code_id)
;

ALTER TABLE practitioner_taxonomy_code ADD CONSTRAINT Refpreference57 
    FOREIGN KEY (preference_id)
    REFERENCES preference(preference_id)
;


-- 
-- TABLE: practitioner_telephone_number 
--

ALTER TABLE practitioner_telephone_number ADD CONSTRAINT Reftelephone_number_type28 
    FOREIGN KEY (telephone_number_type_id)
    REFERENCES telephone_number_type(telephone_number_type_id)
;

ALTER TABLE practitioner_telephone_number ADD CONSTRAINT Refpractitioner39 
    FOREIGN KEY (practitioner_id)
    REFERENCES practitioner(practitioner_id)
;

ALTER TABLE practitioner_telephone_number ADD CONSTRAINT Refpreference58 
    FOREIGN KEY (preference_id)
    REFERENCES preference(preference_id)
;


-- 
-- TABLE: zip_code 
--

ALTER TABLE zip_code ADD CONSTRAINT Refstate2 
    FOREIGN KEY (state_id)
    REFERENCES state(state_id)
;


