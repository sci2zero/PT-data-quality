# PROJECT

## `Project.costs`

Validation Target: `VT.PROJECT.Project.Costs`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PROJECT.Project.Costs.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | The sum of linked funding amounts must not exceed the project costs. | GR.PTCRIS_F1_01DCONSIST.sum_of_linked_fundings_amounts |

## `Project.createDate`

Validation Target: `VT.PROJECT.Project.CreateDate`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PROJECT.Project.CreateDate.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Project.createDate is required. | PTCRIS-F1-01DLINEAGE |

## `Project.description`

Validation Target: `VT.PROJECT.Project.Description`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PROJECT.Project.Description.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Project.description is shorter than the minimum allowed length. | PTCRIS-FsF-F2-01M |
| C.PROJECT.Project.Description.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Project.description is required. | PTCRIS-FsF-F2-01M |

## `Project.doi`

Validation Target: `VT.PROJECT.Project.Doi`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PROJECT.Project.Doi.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Project.doi exceeds the maximum allowed length. | UNMAPPED |
| C.PROJECT.Project.Doi.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Project.doi is shorter than the minimum allowed length. | UNMAPPED |
| C.PROJECT.Project.Doi.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Project.doi is recommended. | UNMAPPED |
| C.PROJECT.Project.Doi.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Project.doi does not match the required format. | GR.PTCRIS_F1_01DSTRUCT.doi_format_verification |
| C.PROJECT.Project.Doi.resolvable | RESOLVABLE | ACCURACY | ERROR | False | 5.0 | The identifier in Project.doi must be resolvable through the configured resolver. | GR.PTCRIS_F1_A1.resolvable_doi |
| C.PROJECT.Project.Doi.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Project.doi must be unique within the repository. | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_doi_allocation |

## `Project.doi, raid, projectReference, other identifiers`

Validation Target: `VT.PROJECT.Project.Identifiers`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PROJECT.Project.Identifiers.minCardinality | MIN_CARDINALITY | COMPLETENESS | ERROR | True | 3.0 | The number of values for Project.doi, raid, projectReference, other identifiers is below the minimum allowed cardinality. | GR.PTCRIS_F1_01DACURR.project_without_at_least_one_identifier |
| C.PROJECT.Project.Identifiers.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Project.doi, raid, projectReference, other identifiers is required. | GR.PTCRIS_F1_01DACURR.project_without_at_least_one_identifier |
| C.PROJECT.Project.Identifiers.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Project.doi, raid, projectReference, other identifiers must be unique within the repository. | UNMAPPED |

## `Project.fromDate`

Validation Target: `VT.PROJECT.Project.FromDate`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PROJECT.Project.FromDate.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of Project.fromDate is later than allowed by the configured date constraints. | UNMAPPED |
| C.PROJECT.Project.FromDate.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of Project.fromDate is earlier than allowed by the configured date constraints. | UNMAPPED |
| C.PROJECT.Project.FromDate.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Project.fromDate is required. | GR.PTCRIS_F1_01DCURREN.mandatory_project_boundary_dates |

## `Project.fundings`

Validation Target: `VT.PROJECT.Project.Fundings`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PROJECT.Project.Fundings.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | Funding identifiers recorded on the project and on the linked funding record must match. | GR.PTCRIS_F1_01DCONSIST.different_funding_ids_in_project_and_funding |
| C.PROJECT.Project.Fundings.maxCardinality | MAX_CARDINALITY | CONSISTENCY | ERROR | True | 1.0 | The number of values for Project.fundings exceeds the maximum allowed cardinality. | UNMAPPED |
| C.PROJECT.Project.Fundings.minCardinality | MIN_CARDINALITY | COMPLETENESS | ERROR | True | 3.0 | The number of values for Project.fundings is below the minimum allowed cardinality. | UNMAPPED |
| C.PROJECT.Project.Fundings.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Project.fundings is required. | UNMAPPED |

## `Project.lastModificationDate`

Validation Target: `VT.PROJECT.Project.LastModificationDate`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PROJECT.Project.LastModificationDate.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Project.lastModificationDate is required. | PTCRIS-F1-01DLINEAGE |

## `Project.metadataAccessLevel`

Validation Target: `VT.PROJECT.Project.MetadataAccessLevel`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PROJECT.Project.MetadataAccessLevel.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Project.metadataAccessLevel is required. | PTCRIS-FsF-A1-01M |
| C.PROJECT.Project.MetadataAccessLevel.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Project.metadataAccessLevel must belong to the configured controlled vocabulary. | PTCRIS-FsF-A1-01M |

## `Project.metadataLicense`

Validation Target: `VT.PROJECT.Project.MetadataLicense`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PROJECT.Project.MetadataLicense.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Project.metadataLicense is required. | PTCRIS-FsF-R1.1-01M |
| C.PROJECT.Project.MetadataLicense.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Project.metadataLicense must belong to the configured controlled vocabulary. | PTCRIS-FsF-R1.1-01M |

## `Project.name`

Validation Target: `VT.PROJECT.Project.Name`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PROJECT.Project.Name.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Project.name exceeds the maximum allowed length. | UNMAPPED |
| C.PROJECT.Project.Name.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Project.name is shorter than the minimum allowed length. | UNMAPPED |
| C.PROJECT.Project.Name.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Project.name is required. | GR.PTCRIS_F1_01DCONSIST.project_title_presence_requirement |
| C.PROJECT.Project.Name.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Project.name does not match the required format. | UNMAPPED |

## `Project.nationalId (projectReference)`

Validation Target: `VT.PROJECT.Project.NationalIdProjectReference`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PROJECT.Project.NationalIdProjectReference.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Project.nationalId (projectReference) exceeds the maximum allowed length. | UNMAPPED |
| C.PROJECT.Project.NationalIdProjectReference.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Project.nationalId (projectReference) is shorter than the minimum allowed length. | UNMAPPED |
| C.PROJECT.Project.NationalIdProjectReference.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Project.nationalId (projectReference) is required. | UNMAPPED |
| C.PROJECT.Project.NationalIdProjectReference.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Project.nationalId (projectReference) must be unique within the repository. | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_pid_allocation |

## `Project.organisations`

Validation Target: `VT.PROJECT.Project.Organisations`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PROJECT.Project.Organisations.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | Project organisation contributions must be internally consistent: allocated funding must not exceed project funding and consortium membership must include a coordinator when required. | GR.PTCRIS_F1_01DCONSIST.sum_of_organizations_funding_greater_than_project_total; GR.PTCRIS_F1_01DSTRUCT.project_with_coordinating_organization_but_no_other_participants |
| C.PROJECT.Project.Organisations.maxCardinality | MAX_CARDINALITY | CONSISTENCY | ERROR | True | 1.0 | The number of values for Project.organisations exceeds the maximum allowed cardinality. | UNMAPPED |
| C.PROJECT.Project.Organisations.minCardinality | MIN_CARDINALITY | COMPLETENESS | ERROR | True | 3.0 | The number of values for Project.organisations is below the minimum allowed cardinality. | UNMAPPED |
| C.PROJECT.Project.Organisations.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Project.organisations is required. | UNMAPPED |

## `Project.raid`

Validation Target: `VT.PROJECT.Project.Raid`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PROJECT.Project.Raid.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Project.raid exceeds the maximum allowed length. | UNMAPPED |
| C.PROJECT.Project.Raid.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Project.raid is shorter than the minimum allowed length. | UNMAPPED |
| C.PROJECT.Project.Raid.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Project.raid is recommended. | UNMAPPED |
| C.PROJECT.Project.Raid.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Project.raid does not match the required format. | GR.PTCRIS_F1_01DSTRUCT.raid_format_verification |
| C.PROJECT.Project.Raid.resolvable | RESOLVABLE | ACCURACY | ERROR | False | 5.0 | The identifier in Project.raid must be resolvable through the configured resolver. | GR.PTCRIS_F1_A1.resolvable_raid |
| C.PROJECT.Project.Raid.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Project.raid must be unique within the repository. | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_raid_allocation |

## `Project.researchAreas`

Validation Target: `VT.PROJECT.Project.ResearchAreas`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PROJECT.Project.ResearchAreas.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Project.researchAreas is required. | UNMAPPED |
| C.PROJECT.Project.ResearchAreas.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Project.researchAreas must be unique within the repository. | UNMAPPED |
| C.PROJECT.Project.ResearchAreas.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Project.researchAreas must belong to the configured controlled vocabulary. | GR.PTCRIS_F1_01DCONSIST.semantic_iri_url_validation |

## `Project.team`

Validation Target: `VT.PROJECT.Project.Team`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PROJECT.Project.Team.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | If a project team is specified, at least one team member must be a principal investigator. | GR.PTCRIS_F1_01DSTRUCT.project_with_team_but_no_principal_investigator |
| C.PROJECT.Project.Team.maxCardinality | MAX_CARDINALITY | CONSISTENCY | ERROR | True | 1.0 | The number of values for Project.team exceeds the maximum allowed cardinality. | UNMAPPED |
| C.PROJECT.Project.Team.minCardinality | MIN_CARDINALITY | COMPLETENESS | ERROR | True | 3.0 | The number of values for Project.team is below the minimum allowed cardinality. | UNMAPPED |
| C.PROJECT.Project.Team.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Project.team is recommended. | UNMAPPED |

## `Project.toDate`

Validation Target: `VT.PROJECT.Project.ToDate`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PROJECT.Project.ToDate.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of Project.toDate is later than allowed by the configured date constraints. | UNMAPPED |
| C.PROJECT.Project.ToDate.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of Project.toDate is earlier than allowed by the configured date constraints. | UNMAPPED |
| C.PROJECT.Project.ToDate.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Project.toDate is required. | GR.PTCRIS_F1_01DCURREN.mandatory_project_boundary_dates |
