# PERSON

## `Education.degreeType`

Validation Target: `VT.PERSON.Education.DegreeType`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Education.DegreeType.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Education.degreeType is required. | UNMAPPED |
| C.PERSON.Education.DegreeType.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Education.degreeType must belong to the configured controlled vocabulary. | UNMAPPED |

## `Education.educationStatus`

Validation Target: `VT.PERSON.Education.EducationStatus`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Education.EducationStatus.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Education.educationStatus is recommended. | UNMAPPED |
| C.PERSON.Education.EducationStatus.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Education.educationStatus must belong to the configured controlled vocabulary. | UNMAPPED |

## `Employment.employmentPositionHierarchy`

Validation Target: `VT.PERSON.Employment.EmploymentPositionHierarchy`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Employment.EmploymentPositionHierarchy.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Employment.employmentPositionHierarchy is required. | UNMAPPED |
| C.PERSON.Employment.EmploymentPositionHierarchy.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Employment.employmentPositionHierarchy must belong to the configured controlled vocabulary. | GR.PTCRIS_F1_01DSEMANT.type_professional_path_classification_validation |

## `ExpertiseOrSkill.researchAreas`

Validation Target: `VT.PERSON.ExpertiseOrSkill.ResearchAreas`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.ExpertiseOrSkill.ResearchAreas.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for ExpertiseOrSkill.researchAreas is recommended. | UNMAPPED |
| C.PERSON.ExpertiseOrSkill.ResearchAreas.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of ExpertiseOrSkill.researchAreas must belong to the configured controlled vocabulary. | UNMAPPED |

## `Involvement.fromDate`

Validation Target: `VT.PERSON.Involvement.FromDate`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Involvement.FromDate.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of Involvement.fromDate is later than allowed by the configured date constraints. | UNMAPPED |
| C.PERSON.Involvement.FromDate.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of Involvement.fromDate is earlier than allowed by the configured date constraints. | UNMAPPED |
| C.PERSON.Involvement.FromDate.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Involvement.fromDate is recommended. | UNMAPPED |

## `Involvement.fundingParts, funding`

Validation Target: `VT.PERSON.Involvement.FundingPartsFunding`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Involvement.FundingPartsFunding.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | Funding references in the involvement must be consistent: fundingParts.funding must match involvement.funding. | UNMAPPED |

## `Involvement.involvementType`

Validation Target: `VT.PERSON.Involvement.InvolvementType`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Involvement.InvolvementType.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Involvement.involvementType is required. | UNMAPPED |
| C.PERSON.Involvement.InvolvementType.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Involvement.involvementType must belong to the configured controlled vocabulary. | UNMAPPED |

## `Involvement.toDate`

Validation Target: `VT.PERSON.Involvement.ToDate`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Involvement.ToDate.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of Involvement.toDate is later than allowed by the configured date constraints. | UNMAPPED |
| C.PERSON.Involvement.ToDate.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of Involvement.toDate is earlier than allowed by the configured date constraints. | UNMAPPED |

## `LanguageKnowledge.academicReview`

Validation Target: `VT.PERSON.LanguageKnowledge.AcademicReview`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.LanguageKnowledge.AcademicReview.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of LanguageKnowledge.academicReview exceeds the maximum allowed length. | UNMAPPED |
| C.PERSON.LanguageKnowledge.AcademicReview.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of LanguageKnowledge.academicReview is shorter than the minimum allowed length. | UNMAPPED |
| C.PERSON.LanguageKnowledge.AcademicReview.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of LanguageKnowledge.academicReview must belong to the configured controlled vocabulary. | UNMAPPED |

## `LanguageKnowledge.academicWriting`

Validation Target: `VT.PERSON.LanguageKnowledge.AcademicWriting`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.LanguageKnowledge.AcademicWriting.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of LanguageKnowledge.academicWriting exceeds the maximum allowed length. | UNMAPPED |
| C.PERSON.LanguageKnowledge.AcademicWriting.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of LanguageKnowledge.academicWriting is shorter than the minimum allowed length. | UNMAPPED |
| C.PERSON.LanguageKnowledge.AcademicWriting.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of LanguageKnowledge.academicWriting must belong to the configured controlled vocabulary. | UNMAPPED |

## `LanguageKnowledge.listening`

Validation Target: `VT.PERSON.LanguageKnowledge.Listening`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.LanguageKnowledge.Listening.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of LanguageKnowledge.listening exceeds the maximum allowed length. | UNMAPPED |
| C.PERSON.LanguageKnowledge.Listening.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of LanguageKnowledge.listening is shorter than the minimum allowed length. | UNMAPPED |
| C.PERSON.LanguageKnowledge.Listening.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of LanguageKnowledge.listening must belong to the configured controlled vocabulary. | UNMAPPED |

## `LanguageKnowledge.overall`

Validation Target: `VT.PERSON.LanguageKnowledge.Overall`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.LanguageKnowledge.Overall.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of LanguageKnowledge.overall exceeds the maximum allowed length. | UNMAPPED |
| C.PERSON.LanguageKnowledge.Overall.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of LanguageKnowledge.overall is shorter than the minimum allowed length. | UNMAPPED |
| C.PERSON.LanguageKnowledge.Overall.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of LanguageKnowledge.overall must belong to the configured controlled vocabulary. | UNMAPPED |

## `LanguageKnowledge.reading`

Validation Target: `VT.PERSON.LanguageKnowledge.Reading`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.LanguageKnowledge.Reading.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of LanguageKnowledge.reading exceeds the maximum allowed length. | UNMAPPED |
| C.PERSON.LanguageKnowledge.Reading.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of LanguageKnowledge.reading is shorter than the minimum allowed length. | UNMAPPED |
| C.PERSON.LanguageKnowledge.Reading.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of LanguageKnowledge.reading must belong to the configured controlled vocabulary. | UNMAPPED |

## `LanguageKnowledge.speaking`

Validation Target: `VT.PERSON.LanguageKnowledge.Speaking`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.LanguageKnowledge.Speaking.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of LanguageKnowledge.speaking exceeds the maximum allowed length. | UNMAPPED |
| C.PERSON.LanguageKnowledge.Speaking.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of LanguageKnowledge.speaking is shorter than the minimum allowed length. | UNMAPPED |
| C.PERSON.LanguageKnowledge.Speaking.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of LanguageKnowledge.speaking must belong to the configured controlled vocabulary. | UNMAPPED |

## `LanguageKnowledge.writing`

Validation Target: `VT.PERSON.LanguageKnowledge.Writing`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.LanguageKnowledge.Writing.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of LanguageKnowledge.writing exceeds the maximum allowed length. | UNMAPPED |
| C.PERSON.LanguageKnowledge.Writing.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of LanguageKnowledge.writing is shorter than the minimum allowed length. | UNMAPPED |
| C.PERSON.LanguageKnowledge.Writing.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of LanguageKnowledge.writing must belong to the configured controlled vocabulary. | UNMAPPED |

## `Membership.membershipType`

Validation Target: `VT.PERSON.Membership.MembershipType`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Membership.MembershipType.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Membership.membershipType is required. | UNMAPPED |
| C.PERSON.Membership.MembershipType.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Membership.membershipType must belong to the configured controlled vocabulary. | UNMAPPED |

## `Person.authenticusId`

Validation Target: `VT.PERSON.Person.AuthenticusId`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Person.AuthenticusId.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Person.authenticusId exceeds the maximum allowed length. | PTCRIS-F1-01DSTRUCT; PTCRIS-F1-01DACURR |
| C.PERSON.Person.AuthenticusId.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Person.authenticusId is shorter than the minimum allowed length. | PTCRIS-F1-01DSTRUCT; PTCRIS-F1-01DACURR |
| C.PERSON.Person.AuthenticusId.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Person.authenticusId does not match the required format. | PTCRIS-F1-01DSTRUCT; PTCRIS-F1-01DACURR |
| C.PERSON.Person.AuthenticusId.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Person.authenticusId must be unique within the repository. | PTCRIS-F1-01DSTRUCT; PTCRIS-F1-01DACURR |

## `Person.biography`

Validation Target: `VT.PERSON.Person.Biography`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Person.Biography.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Person.biography is shorter than the minimum allowed length. | PTCRIS-FsF-F2-01M |
| C.PERSON.Person.Biography.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Person.biography is required. | PTCRIS-FsF-F2-01M |

## `Person.createDate`

Validation Target: `VT.PERSON.Person.CreateDate`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Person.CreateDate.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Person.createDate is required. | PTCRIS-F1-01DLINEAGE |

## `Person.involvements`

Validation Target: `VT.PERSON.Person.Involvements`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Person.Involvements.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | A Portuguese researcher must have at least one linked employment with a start date and an employment position. | UNMAPPED |
| C.PERSON.Person.Involvements.maxCardinality | MAX_CARDINALITY | CONSISTENCY | ERROR | True | 1.0 | The number of values for Person.involvements exceeds the maximum allowed cardinality. | UNMAPPED |
| C.PERSON.Person.Involvements.minCardinality | MIN_CARDINALITY | COMPLETENESS | ERROR | True | 3.0 | The number of values for Person.involvements is below the minimum allowed cardinality. | UNMAPPED |
| C.PERSON.Person.Involvements.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Person.involvements is required. | GR.PTCRIS_F1_01DCURREN.mandatory_start_date_of_professional_career |

## `Person.lastModificationDate`

Validation Target: `VT.PERSON.Person.LastModificationDate`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Person.LastModificationDate.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Person.lastModificationDate is required. | PTCRIS-F1-01DLINEAGE |

## `Person.lattesId`

Validation Target: `VT.PERSON.Person.LattesId`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Person.LattesId.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Person.lattesId exceeds the maximum allowed length. | PTCRIS-F1-01DSTRUCT; PTCRIS-F1-01DACURR |
| C.PERSON.Person.LattesId.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Person.lattesId is shorter than the minimum allowed length. | PTCRIS-F1-01DSTRUCT; PTCRIS-F1-01DACURR |
| C.PERSON.Person.LattesId.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Person.lattesId does not match the required format. | PTCRIS-F1-01DSTRUCT; PTCRIS-F1-01DACURR |
| C.PERSON.Person.LattesId.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Person.lattesId must be unique within the repository. | PTCRIS-F1-01DSTRUCT; PTCRIS-F1-01DACURR |

## `Person.metadataAccessLevel`

Validation Target: `VT.PERSON.Person.MetadataAccessLevel`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Person.MetadataAccessLevel.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Person.metadataAccessLevel is required. | PTCRIS-FsF-A1-01M |
| C.PERSON.Person.MetadataAccessLevel.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Person.metadataAccessLevel must belong to the configured controlled vocabulary. | PTCRIS-FsF-A1-01M |

## `Person.metadataLicense`

Validation Target: `VT.PERSON.Person.MetadataLicense`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Person.MetadataLicense.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Person.metadataLicense is required. | PTCRIS-FsF-R1.1-01M |
| C.PERSON.Person.MetadataLicense.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Person.metadataLicense must belong to the configured controlled vocabulary. | PTCRIS-FsF-R1.1-01M |

## `Person.name`

Validation Target: `VT.PERSON.Person.Name`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Person.Name.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Person.name exceeds the maximum allowed length. | UNMAPPED |
| C.PERSON.Person.Name.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Person.name is shorter than the minimum allowed length. | UNMAPPED |
| C.PERSON.Person.Name.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Person.name is required. | GR.PTCRIS_F1_01DACURR.full_name_presence_and_length_validation |

## `Person.nationalId (cienciaId)`

Validation Target: `VT.PERSON.Person.NationalIdCienciaId`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Person.NationalIdCienciaId.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Person.nationalId (cienciaId) exceeds the maximum allowed length. | PTCRIS-F1-01DSTRUCT; PTCRIS-DQ-F1-01IDUNIQ |
| C.PERSON.Person.NationalIdCienciaId.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Person.nationalId (cienciaId) is shorter than the minimum allowed length. | PTCRIS-F1-01DSTRUCT; PTCRIS-DQ-F1-01IDUNIQ |
| C.PERSON.Person.NationalIdCienciaId.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Person.nationalId (cienciaId) is required. | PTCRIS-F1-01DSTRUCT; PTCRIS-DQ-F1-01IDUNIQ |
| C.PERSON.Person.NationalIdCienciaId.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Person.nationalId (cienciaId) does not match the required format. | PTCRIS-F1-01DSTRUCT; PTCRIS-DQ-F1-01IDUNIQ |
| C.PERSON.Person.NationalIdCienciaId.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Person.nationalId (cienciaId) must be unique within the repository. | PTCRIS-F1-01DSTRUCT; GR.PTCRIS_F1_01DACURR.global_uniqueness_of_science_id_allocation; PTCRIS-DQ-F1-01IDUNIQ |

## `Person.openAlexId`

Validation Target: `VT.PERSON.Person.OpenAlexId`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Person.OpenAlexId.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Person.openAlexId exceeds the maximum allowed length. | PTCRIS-F1-01DSTRUCT; PTCRIS-F1-01DACURR |
| C.PERSON.Person.OpenAlexId.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Person.openAlexId is shorter than the minimum allowed length. | PTCRIS-F1-01DSTRUCT; PTCRIS-F1-01DACURR |
| C.PERSON.Person.OpenAlexId.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Person.openAlexId does not match the required format. | PTCRIS-F1-01DSTRUCT; PTCRIS-F1-01DACURR |
| C.PERSON.Person.OpenAlexId.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Person.openAlexId must be unique within the repository. | PTCRIS-F1-01DSTRUCT; PTCRIS-F1-01DACURR |

## `Person.orcid`

Validation Target: `VT.PERSON.Person.Orcid`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Person.Orcid.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Person.orcid exceeds the maximum allowed length. | UNMAPPED |
| C.PERSON.Person.Orcid.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Person.orcid is shorter than the minimum allowed length. | UNMAPPED |
| C.PERSON.Person.Orcid.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Person.orcid is recommended. | UNMAPPED |
| C.PERSON.Person.Orcid.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Person.orcid does not match the required format. | GR.PTCRIS_F1_01DSTRUCT.open_researcher_and_contributor_id_orcid_format_verification |
| C.PERSON.Person.Orcid.resolvable | RESOLVABLE | ACCURACY | ERROR | False | 5.0 | The identifier in Person.orcid must be resolvable through the configured resolver. | GR.PTCRIS_F1_A1.resolvable_pid |
| C.PERSON.Person.Orcid.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Person.orcid must be unique within the repository. | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_orcid_allocation |

## `Person.scholarId`

Validation Target: `VT.PERSON.Person.ScholarId`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Person.ScholarId.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Person.scholarId exceeds the maximum allowed length. | PTCRIS-F1-01DSTRUCT; PTCRIS-F1-01DACURR |
| C.PERSON.Person.ScholarId.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Person.scholarId is shorter than the minimum allowed length. | PTCRIS-F1-01DSTRUCT; PTCRIS-F1-01DACURR |
| C.PERSON.Person.ScholarId.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Person.scholarId does not match the required format. | PTCRIS-F1-01DSTRUCT; PTCRIS-F1-01DACURR |
| C.PERSON.Person.ScholarId.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Person.scholarId must be unique within the repository. | PTCRIS-F1-01DSTRUCT; PTCRIS-F1-01DACURR |

## `Person.scopusAuthorId`

Validation Target: `VT.PERSON.Person.ScopusAuthorId`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Person.ScopusAuthorId.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Person.scopusAuthorId exceeds the maximum allowed length. | PTCRIS-F1-01DACURR |
| C.PERSON.Person.ScopusAuthorId.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Person.scopusAuthorId is shorter than the minimum allowed length. | PTCRIS-F1-01DACURR |
| C.PERSON.Person.ScopusAuthorId.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Person.scopusAuthorId does not match the required format. | GR.PTCRIS_F1_01DSTRUCT.scopus_author_id_format_validation; PTCRIS-F1-01DACURR |
| C.PERSON.Person.ScopusAuthorId.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Person.scopusAuthorId must be unique within the repository. | PTCRIS-F1-01DACURR |

## `Person.webOfScienceResearcherId`

Validation Target: `VT.PERSON.Person.WebOfScienceResearcherId`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Person.WebOfScienceResearcherId.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Person.webOfScienceResearcherId exceeds the maximum allowed length. | PTCRIS-F1-01DACURR |
| C.PERSON.Person.WebOfScienceResearcherId.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Person.webOfScienceResearcherId is shorter than the minimum allowed length. | PTCRIS-F1-01DACURR |
| C.PERSON.Person.WebOfScienceResearcherId.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Person.webOfScienceResearcherId does not match the required format. | GR.PTCRIS_F1_01DSTRUCT.web_of_science_researcher_id_format_validation; PTCRIS-F1-01DACURR |
| C.PERSON.Person.WebOfScienceResearcherId.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Person.webOfScienceResearcherId must be unique within the repository. | PTCRIS-F1-01DACURR |

## `PersonName.firstname`

Validation Target: `VT.PERSON.PersonName.Firstname`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.PersonName.Firstname.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of PersonName.firstname exceeds the maximum allowed length. | UNMAPPED |
| C.PERSON.PersonName.Firstname.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of PersonName.firstname is shorter than the minimum allowed length. | UNMAPPED |
| C.PERSON.PersonName.Firstname.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of PersonName.firstname does not match the required format. | UNMAPPED |

## `PersonName.lastname`

Validation Target: `VT.PERSON.PersonName.Lastname`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.PersonName.Lastname.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of PersonName.lastname exceeds the maximum allowed length. | UNMAPPED |
| C.PERSON.PersonName.Lastname.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of PersonName.lastname is shorter than the minimum allowed length. | UNMAPPED |
| C.PERSON.PersonName.Lastname.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for PersonName.lastname is required. | GR.PTCRIS_F1_01DACURR.full_name_presence_and_length_validation |
| C.PERSON.PersonName.Lastname.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of PersonName.lastname does not match the required format. | GR.PTCRIS_F1_01DSTRUCT.standardized_citation_name_format_verification |

## `PersonName.otherName`

Validation Target: `VT.PERSON.PersonName.OtherName`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.PersonName.OtherName.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of PersonName.otherName exceeds the maximum allowed length. | UNMAPPED |
| C.PERSON.PersonName.OtherName.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of PersonName.otherName is shorter than the minimum allowed length. | UNMAPPED |
| C.PERSON.PersonName.OtherName.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of PersonName.otherName does not match the required format. | UNMAPPED |

## `PersonName.personNameType`

Validation Target: `VT.PERSON.PersonName.PersonNameType`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.PersonName.PersonNameType.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of PersonName.personNameType exceeds the maximum allowed length. | UNMAPPED |
| C.PERSON.PersonName.PersonNameType.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of PersonName.personNameType is shorter than the minimum allowed length. | UNMAPPED |
| C.PERSON.PersonName.PersonNameType.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for PersonName.personNameType is required. | UNMAPPED |
| C.PERSON.PersonName.PersonNameType.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of PersonName.personNameType must belong to the configured controlled vocabulary. | UNMAPPED |

## `PersonalInfo.birthDate`

Validation Target: `VT.PERSON.PersonalInfo.BirthDate`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.PersonalInfo.BirthDate.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of PersonalInfo.birthDate is later than allowed by the configured date constraints. | GR.PTCRIS_F1_01DCONSIST.non_existent_or_futuristic_birth_date_restriction |
| C.PERSON.PersonalInfo.BirthDate.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of PersonalInfo.birthDate is earlier than allowed by the configured date constraints. | GR.PTCRIS_F1_01DCONSIST.non_existent_or_futuristic_birth_date_restriction |
| C.PERSON.PersonalInfo.BirthDate.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for PersonalInfo.birthDate is recommended. | UNMAPPED |

## `PersonalInfo.sex`

Validation Target: `VT.PERSON.PersonalInfo.Sex`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.PersonalInfo.Sex.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of PersonalInfo.sex exceeds the maximum allowed length. | UNMAPPED |
| C.PERSON.PersonalInfo.Sex.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of PersonalInfo.sex is shorter than the minimum allowed length. | UNMAPPED |
| C.PERSON.PersonalInfo.Sex.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of PersonalInfo.sex must belong to the configured controlled vocabulary. | GR.PTCRIS_F1_01DSEMANT.gender_classification_conformity |

## `Prize.effectiveDate`

Validation Target: `VT.PERSON.Prize.EffectiveDate`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Prize.EffectiveDate.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of Prize.effectiveDate is later than allowed by the configured date constraints. | UNMAPPED |
| C.PERSON.Prize.EffectiveDate.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of Prize.effectiveDate is earlier than allowed by the configured date constraints. | UNMAPPED |
| C.PERSON.Prize.EffectiveDate.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Prize.effectiveDate is required. | UNMAPPED |

## `Prize.researchAreas`

Validation Target: `VT.PERSON.Prize.ResearchAreas`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Prize.ResearchAreas.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Prize.researchAreas is recommended. | UNMAPPED |
| C.PERSON.Prize.ResearchAreas.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Prize.researchAreas must belong to the configured controlled vocabulary. | UNMAPPED |

## `Prize.toDate`

Validation Target: `VT.PERSON.Prize.ToDate`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Prize.ToDate.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of Prize.toDate is earlier than allowed by the configured date constraints. | UNMAPPED |

## `Prize.type`

Validation Target: `VT.PERSON.Prize.Type`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.PERSON.Prize.Type.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Prize.type is required. | UNMAPPED |
| C.PERSON.Prize.Type.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Prize.type must belong to the configured controlled vocabulary. | UNMAPPED |
