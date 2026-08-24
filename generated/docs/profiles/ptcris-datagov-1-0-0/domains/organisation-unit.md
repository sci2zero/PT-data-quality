# ORGANISATION_UNIT

## `OrganisationUnit.active`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.Active`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ORGANISATION_UNIT.OrganisationUnit.Active.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of OrganisationUnit.active must belong to the configured controlled vocabulary. | UNMAPPED |

## `OrganisationUnit.createDate`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.CreateDate`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ORGANISATION_UNIT.OrganisationUnit.CreateDate.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for OrganisationUnit.createDate is required. | PTCRIS-F1-01DLINEAGE |

## `OrganisationUnit.dateDissolved`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.DateDissolved`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ORGANISATION_UNIT.OrganisationUnit.DateDissolved.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of OrganisationUnit.dateDissolved is later than allowed by the configured date constraints. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.DateDissolved.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of OrganisationUnit.dateDissolved is earlier than allowed by the configured date constraints. | UNMAPPED |

## `OrganisationUnit.dateEstablished`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.DateEstablished`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ORGANISATION_UNIT.OrganisationUnit.DateEstablished.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of OrganisationUnit.dateEstablished is later than allowed by the configured date constraints. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.DateEstablished.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for OrganisationUnit.dateEstablished is recommended. | UNMAPPED |

## `OrganisationUnit.description`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.Description`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ORGANISATION_UNIT.OrganisationUnit.Description.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of OrganisationUnit.description is shorter than the minimum allowed length. | PTCRIS-FsF-F2-01M |
| C.ORGANISATION_UNIT.OrganisationUnit.Description.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for OrganisationUnit.description is required. | PTCRIS-FsF-F2-01M |

## `OrganisationUnit.fundref`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.Fundref`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ORGANISATION_UNIT.OrganisationUnit.Fundref.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of OrganisationUnit.fundref exceeds the maximum allowed length. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Fundref.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of OrganisationUnit.fundref is shorter than the minimum allowed length. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Fundref.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of OrganisationUnit.fundref does not match the required format. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Fundref.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of OrganisationUnit.fundref must be unique within the repository. | UNMAPPED |

## `OrganisationUnit.grid`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.Grid`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ORGANISATION_UNIT.OrganisationUnit.Grid.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of OrganisationUnit.grid exceeds the maximum allowed length. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Grid.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of OrganisationUnit.grid is shorter than the minimum allowed length. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Grid.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of OrganisationUnit.grid does not match the required format. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Grid.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of OrganisationUnit.grid must be unique within the repository. | UNMAPPED |

## `OrganisationUnit.isni`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.Isni`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ORGANISATION_UNIT.OrganisationUnit.Isni.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of OrganisationUnit.isni exceeds the maximum allowed length. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Isni.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of OrganisationUnit.isni is shorter than the minimum allowed length. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Isni.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of OrganisationUnit.isni does not match the required format. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Isni.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of OrganisationUnit.isni must be unique within the repository. | UNMAPPED |

## `OrganisationUnit.lastModificationDate`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.LastModificationDate`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ORGANISATION_UNIT.OrganisationUnit.LastModificationDate.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for OrganisationUnit.lastModificationDate is required. | PTCRIS-F1-01DLINEAGE |

## `OrganisationUnit.metadataAccessLevel`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for OrganisationUnit.metadataAccessLevel is required. | PTCRIS-FsF-A1-01M |
| C.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of OrganisationUnit.metadataAccessLevel must belong to the configured controlled vocabulary. | PTCRIS-FsF-A1-01M |

## `OrganisationUnit.metadataLicense`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for OrganisationUnit.metadataLicense is required. | PTCRIS-FsF-R1.1-01M |
| C.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of OrganisationUnit.metadataLicense must belong to the configured controlled vocabulary. | PTCRIS-FsF-R1.1-01M |

## `OrganisationUnit.name`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.Name`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ORGANISATION_UNIT.OrganisationUnit.Name.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of OrganisationUnit.name exceeds the maximum allowed length. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Name.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of OrganisationUnit.name is shorter than the minimum allowed length. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Name.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for OrganisationUnit.name is required. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Name.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of OrganisationUnit.name does not match the required format. | UNMAPPED |

## `OrganisationUnit.openAlexId`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of OrganisationUnit.openAlexId exceeds the maximum allowed length. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of OrganisationUnit.openAlexId is shorter than the minimum allowed length. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of OrganisationUnit.openAlexId does not match the required format. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of OrganisationUnit.openAlexId must be unique within the repository. | UNMAPPED |

## `OrganisationUnit.postalAddress`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.PostalAddress`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|

## `OrganisationUnit.ringgold`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.Ringgold`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ORGANISATION_UNIT.OrganisationUnit.Ringgold.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of OrganisationUnit.ringgold exceeds the maximum allowed length. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Ringgold.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of OrganisationUnit.ringgold is shorter than the minimum allowed length. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Ringgold.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of OrganisationUnit.ringgold does not match the required format. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Ringgold.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of OrganisationUnit.ringgold must be unique within the repository. | UNMAPPED |

## `OrganisationUnit.ror`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.Ror`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ORGANISATION_UNIT.OrganisationUnit.Ror.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of OrganisationUnit.ror exceeds the maximum allowed length. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Ror.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of OrganisationUnit.ror is shorter than the minimum allowed length. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Ror.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for OrganisationUnit.ror is recommended. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Ror.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The ROR identifier must contain exactly 9 characters, start with 0, and be followed by eight lowercase letters or digits. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Ror.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of OrganisationUnit.ror must be unique within the repository. | UNMAPPED |

## `OrganisationUnit.ror, isni`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.RorIsni`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ORGANISATION_UNIT.OrganisationUnit.RorIsni.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for OrganisationUnit.ror, isni is required. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.RorIsni.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of OrganisationUnit.ror, isni must be unique within the repository. | UNMAPPED |

## `OrganisationUnit.scopusAfid`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of OrganisationUnit.scopusAfid exceeds the maximum allowed length. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of OrganisationUnit.scopusAfid is shorter than the minimum allowed length. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of OrganisationUnit.scopusAfid does not match the required format. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of OrganisationUnit.scopusAfid must be unique within the repository. | UNMAPPED |

## `OrganisationUnit.sector`

Validation Target: `VT.ORGANISATION_UNIT.OrganisationUnit.Sector`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ORGANISATION_UNIT.OrganisationUnit.Sector.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for OrganisationUnit.sector is recommended. | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Sector.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of OrganisationUnit.sector must belong to the configured controlled vocabulary. | UNMAPPED |
