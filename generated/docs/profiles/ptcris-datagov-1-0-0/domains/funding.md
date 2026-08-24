# FUNDING

## `Funding.amount`

Validation Target: `VT.FUNDING.Funding.Amount`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.FUNDING.Funding.Amount.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Funding.amount is required. | UNMAPPED |

## `Funding.createDate`

Validation Target: `VT.FUNDING.Funding.CreateDate`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.FUNDING.Funding.CreateDate.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Funding.createDate is required. | PTCRIS-F1-01DLINEAGE |

## `Funding.dateAwarded`

Validation Target: `VT.FUNDING.Funding.DateAwarded`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.FUNDING.Funding.DateAwarded.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of Funding.dateAwarded is later than allowed by the configured date constraints. | UNMAPPED |
| C.FUNDING.Funding.DateAwarded.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of Funding.dateAwarded is earlier than allowed by the configured date constraints. | UNMAPPED |
| C.FUNDING.Funding.DateAwarded.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Funding.dateAwarded is recommended. | GR.PTCRIS_F1_01DCURREN.award_year_required_verification |

## `Funding.dateSubmitted`

Validation Target: `VT.FUNDING.Funding.DateSubmitted`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.FUNDING.Funding.DateSubmitted.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of Funding.dateSubmitted is later than allowed by the configured date constraints. | UNMAPPED |
| C.FUNDING.Funding.DateSubmitted.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of Funding.dateSubmitted is earlier than allowed by the configured date constraints. | UNMAPPED |

## `Funding.description`

Validation Target: `VT.FUNDING.Funding.Description`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.FUNDING.Funding.Description.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Funding.description is shorter than the minimum allowed length. | PTCRIS-FsF-F2-01M |
| C.FUNDING.Funding.Description.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Funding.description is required. | PTCRIS-FsF-F2-01M |

## `Funding.doi`

Validation Target: `VT.FUNDING.Funding.Doi`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.FUNDING.Funding.Doi.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Funding.doi exceeds the maximum allowed length. | UNMAPPED |
| C.FUNDING.Funding.Doi.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Funding.doi is shorter than the minimum allowed length. | UNMAPPED |
| C.FUNDING.Funding.Doi.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Funding.doi is recommended. | UNMAPPED |
| C.FUNDING.Funding.Doi.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Funding.doi does not match the required format. | GR.PTCRIS_F1_01DSTRUCT.doi_format_verification |
| C.FUNDING.Funding.Doi.resolvable | RESOLVABLE | ACCURACY | ERROR | False | 5.0 | The identifier in Funding.doi must be resolvable through the configured resolver. | GR.PTCRIS_F1_A1.resolvable_doi |
| C.FUNDING.Funding.Doi.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Funding.doi must be unique within the repository. | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_doi_allocation |

## `Funding.doi, grantAgreementId, other identifiers`

Validation Target: `VT.FUNDING.Funding.Identifiers`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.FUNDING.Funding.Identifiers.minCardinality | MIN_CARDINALITY | COMPLETENESS | ERROR | True | 3.0 | The number of values for Funding.doi, grantAgreementId, other identifiers is below the minimum allowed cardinality. | UNMAPPED |
| C.FUNDING.Funding.Identifiers.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Funding.doi, grantAgreementId, other identifiers is required. | UNMAPPED |

## `Funding.fromDate`

Validation Target: `VT.FUNDING.Funding.FromDate`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.FUNDING.Funding.FromDate.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of Funding.fromDate is later than allowed by the configured date constraints. | GR.PTCRIS_F1_01DCURREN.project_funding_with_suspicious_start_date |
| C.FUNDING.Funding.FromDate.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of Funding.fromDate is earlier than allowed by the configured date constraints. | GR.PTCRIS_F1_01DCURREN.project_funding_with_suspicious_start_date |
| C.FUNDING.Funding.FromDate.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Funding.fromDate is required. | UNMAPPED |

## `Funding.lastModificationDate`

Validation Target: `VT.FUNDING.Funding.LastModificationDate`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.FUNDING.Funding.LastModificationDate.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Funding.lastModificationDate is required. | PTCRIS-F1-01DLINEAGE |

## `Funding.metadataAccessLevel`

Validation Target: `VT.FUNDING.Funding.MetadataAccessLevel`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.FUNDING.Funding.MetadataAccessLevel.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Funding.metadataAccessLevel is required. | PTCRIS-FsF-A1-01M |
| C.FUNDING.Funding.MetadataAccessLevel.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Funding.metadataAccessLevel must belong to the configured controlled vocabulary. | PTCRIS-FsF-A1-01M |

## `Funding.metadataLicense`

Validation Target: `VT.FUNDING.Funding.MetadataLicense`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.FUNDING.Funding.MetadataLicense.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Funding.metadataLicense is required. | PTCRIS-FsF-R1.1-01M |
| C.FUNDING.Funding.MetadataLicense.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Funding.metadataLicense must belong to the configured controlled vocabulary. | PTCRIS-FsF-R1.1-01M |

## `Funding.name`

Validation Target: `VT.FUNDING.Funding.Name`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.FUNDING.Funding.Name.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Funding.name exceeds the maximum allowed length. | UNMAPPED |
| C.FUNDING.Funding.Name.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Funding.name is shorter than the minimum allowed length. | UNMAPPED |
| C.FUNDING.Funding.Name.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Funding.name is required. | UNMAPPED |
| C.FUNDING.Funding.Name.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Funding.name does not match the required format. | GR.PTCRIS_F1_01DSTRUCT.format_validation_for_award_title_name |

## `Funding.project, involvement`

Validation Target: `VT.FUNDING.Funding.ProjectInvolvement`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.FUNDING.Funding.ProjectInvolvement.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | A funding record must be linked to exactly one funded context: a project, an employment, or an education record. | UNMAPPED |
| C.FUNDING.Funding.ProjectInvolvement.minCardinality | MIN_CARDINALITY | COMPLETENESS | ERROR | True | 3.0 | The number of values for Funding.project, involvement is below the minimum allowed cardinality. | UNMAPPED |
| C.FUNDING.Funding.ProjectInvolvement.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Funding.project, involvement is required. | UNMAPPED |

## `Funding.projectReferenceId`

Validation Target: `VT.FUNDING.Funding.ProjectReferenceId`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.FUNDING.Funding.ProjectReferenceId.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Funding.projectReferenceId exceeds the maximum allowed length. | UNMAPPED |
| C.FUNDING.Funding.ProjectReferenceId.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Funding.projectReferenceId is shorter than the minimum allowed length. | UNMAPPED |
| C.FUNDING.Funding.ProjectReferenceId.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Funding.projectReferenceId is recommended. | UNMAPPED |
| C.FUNDING.Funding.ProjectReferenceId.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Funding.projectReferenceId must be unique within the repository. | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_pid_allocation |

## `Funding.researchAreas`

Validation Target: `VT.FUNDING.Funding.ResearchAreas`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.FUNDING.Funding.ResearchAreas.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Funding.researchAreas is recommended. | UNMAPPED |
| C.FUNDING.Funding.ResearchAreas.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Funding.researchAreas must belong to the configured controlled vocabulary. | UNMAPPED |

## `Funding.toDate`

Validation Target: `VT.FUNDING.Funding.ToDate`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.FUNDING.Funding.ToDate.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of Funding.toDate is later than allowed by the configured date constraints. | GR.PTCRIS_F1_01DCURREN.project_funding_with_suspicious_start_date |
| C.FUNDING.Funding.ToDate.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of Funding.toDate is earlier than allowed by the configured date constraints. | GR.PTCRIS_F1_01DCURREN.project_funding_with_suspicious_start_date |
| C.FUNDING.Funding.ToDate.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Funding.toDate is required. | UNMAPPED |
