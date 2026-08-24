# OUTPUT

## `Document.contributors`

Validation Target: `VT.OUTPUT.Document.Contributors`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.Document.Contributors.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | At least one managed person must be linked to the research output, except when the output is a source/container for another document type. | UNMAPPED |
| C.OUTPUT.Document.Contributors.minCardinality | MIN_CARDINALITY | COMPLETENESS | ERROR | True | 3.0 | The number of values for Document.contributors is below the minimum allowed cardinality. | UNMAPPED |
| C.OUTPUT.Document.Contributors.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Document.contributors is required. | UNMAPPED |

## `Document.createDate`

Validation Target: `VT.OUTPUT.Document.CreateDate`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.Document.CreateDate.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Document.createDate is required. | PTCRIS-F1-01DLINEAGE |

## `Document.description`

Validation Target: `VT.OUTPUT.Document.Description`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.Document.Description.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Document.description is shorter than the minimum allowed length. | PTCRIS-FsF-F2-01M |
| C.OUTPUT.Document.Description.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Document.description is required. | PTCRIS-FsF-F2-01M |

## `Document.documentDate`

Validation Target: `VT.OUTPUT.Document.DocumentDate`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.Document.DocumentDate.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of Document.documentDate is later than allowed by the configured date constraints. | UNMAPPED |
| C.OUTPUT.Document.DocumentDate.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of Document.documentDate is earlier than allowed by the configured date constraints. | UNMAPPED |
| C.OUTPUT.Document.DocumentDate.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Document.documentDate is required. | UNMAPPED |

## `Document.doi`

Validation Target: `VT.OUTPUT.Document.Doi`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.Document.Doi.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Document.doi exceeds the maximum allowed length. | UNMAPPED |
| C.OUTPUT.Document.Doi.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Document.doi is shorter than the minimum allowed length. | UNMAPPED |
| C.OUTPUT.Document.Doi.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Document.doi is recommended. | UNMAPPED |
| C.OUTPUT.Document.Doi.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Document.doi does not match the required format. | GR.PTCRIS_F1_01DSTRUCT.doi_format_verification |
| C.OUTPUT.Document.Doi.resolvable | RESOLVABLE | ACCURACY | ERROR | False | 5.0 | The identifier in Document.doi must be resolvable through the configured resolver. | GR.PTCRIS_F1_A1.resolvable_doi |
| C.OUTPUT.Document.Doi.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Document.doi must be unique within the repository. | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_doi_allocation |

## `Document.doi, handle, other identifiers`

Validation Target: `VT.OUTPUT.Document.Identifiers`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.Document.Identifiers.minCardinality | MIN_CARDINALITY | COMPLETENESS | ERROR | True | 3.0 | The number of values for Document.doi, handle, other identifiers is below the minimum allowed cardinality. | UNMAPPED |
| C.OUTPUT.Document.Identifiers.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Document.doi, handle, other identifiers is required. | UNMAPPED |
| C.OUTPUT.Document.Identifiers.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Document.doi, handle, other identifiers must be unique within the repository. | UNMAPPED |

## `Document.handle`

Validation Target: `VT.OUTPUT.Document.Handle`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.Document.Handle.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Document.handle exceeds the maximum allowed length. | UNMAPPED |
| C.OUTPUT.Document.Handle.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Document.handle is shorter than the minimum allowed length. | UNMAPPED |
| C.OUTPUT.Document.Handle.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Document.handle is recommended. | UNMAPPED |
| C.OUTPUT.Document.Handle.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Document.handle does not match the required format. | GR.PTCRIS_F1_01DSTRUCT.handle_format_verification |
| C.OUTPUT.Document.Handle.resolvable | RESOLVABLE | ACCURACY | ERROR | False | 5.0 | The identifier in Document.handle must be resolvable through the configured resolver. | GR.PTCRIS_F1_A1.resolvable_handle |
| C.OUTPUT.Document.Handle.unique | UNIQUENESS | UNIQUENESS | ERROR | True | 5.0 | The value of Document.handle must be unique within the repository. | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_handle_allocation |

## `Document.lastModificationDate`

Validation Target: `VT.OUTPUT.Document.LastModificationDate`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.Document.LastModificationDate.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Document.lastModificationDate is required. | PTCRIS-F1-01DLINEAGE |

## `Document.metadataAccessLevel`

Validation Target: `VT.OUTPUT.Document.MetadataAccessLevel`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.Document.MetadataAccessLevel.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Document.metadataAccessLevel is required. | PTCRIS-FsF-A1-01M |
| C.OUTPUT.Document.MetadataAccessLevel.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Document.metadataAccessLevel must belong to the configured controlled vocabulary. | PTCRIS-FsF-A1-01M |

## `Document.metadataLicense`

Validation Target: `VT.OUTPUT.Document.MetadataLicense`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.Document.MetadataLicense.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Document.metadataLicense is required. | PTCRIS-FsF-R1.1-01M |
| C.OUTPUT.Document.MetadataLicense.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Document.metadataLicense must belong to the configured controlled vocabulary. | PTCRIS-FsF-R1.1-01M |

## `Document.openAccess`

Validation Target: `VT.OUTPUT.Document.OpenAccess`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.Document.OpenAccess.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Document.openAccess is recommended. | UNMAPPED |
| C.OUTPUT.Document.OpenAccess.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Document.openAccess must belong to the configured controlled vocabulary. | UNMAPPED |

## `Document.researchAreas`

Validation Target: `VT.OUTPUT.Document.ResearchAreas`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.Document.ResearchAreas.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Document.researchAreas is required. | UNMAPPED |
| C.OUTPUT.Document.ResearchAreas.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Document.researchAreas must belong to the configured controlled vocabulary. | UNMAPPED |

## `Document.title`

Validation Target: `VT.OUTPUT.Document.Title`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.Document.Title.maxLength | MAX_LENGTH | CONSISTENCY | ERROR | True | 1.0 | The value of Document.title exceeds the maximum allowed length. | UNMAPPED |
| C.OUTPUT.Document.Title.minLength | MIN_LENGTH | CONSISTENCY | ERROR | True | 3.0 | The value of Document.title is shorter than the minimum allowed length. | UNMAPPED |
| C.OUTPUT.Document.Title.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Document.title is required. | UNMAPPED |
| C.OUTPUT.Document.Title.pattern | REGEX | VALIDITY | ERROR | True | 3.0 | The value of Document.title does not match the required format. | UNMAPPED |

## `IntellectualProperty.dateEndTerm`

Validation Target: `VT.OUTPUT.IntellectualProperty.DateEndTerm`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.IntellectualProperty.DateEndTerm.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of IntellectualProperty.dateEndTerm is earlier than allowed by the configured date constraints. | UNMAPPED |
| C.OUTPUT.IntellectualProperty.DateEndTerm.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for IntellectualProperty.dateEndTerm is recommended. | UNMAPPED |

## `IntellectualProperty.dateFilingPriority`

Validation Target: `VT.OUTPUT.IntellectualProperty.DateFilingPriority`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.IntellectualProperty.DateFilingPriority.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of IntellectualProperty.dateFilingPriority is later than allowed by the configured date constraints. | UNMAPPED |
| C.OUTPUT.IntellectualProperty.DateFilingPriority.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of IntellectualProperty.dateFilingPriority is earlier than allowed by the configured date constraints. | UNMAPPED |
| C.OUTPUT.IntellectualProperty.DateFilingPriority.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for IntellectualProperty.dateFilingPriority is recommended. | UNMAPPED |

## `IntellectualProperty.dateRequested`

Validation Target: `VT.OUTPUT.IntellectualProperty.DateRequested`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.IntellectualProperty.DateRequested.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of IntellectualProperty.dateRequested is later than allowed by the configured date constraints. | UNMAPPED |
| C.OUTPUT.IntellectualProperty.DateRequested.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of IntellectualProperty.dateRequested is earlier than allowed by the configured date constraints. | UNMAPPED |
| C.OUTPUT.IntellectualProperty.DateRequested.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for IntellectualProperty.dateRequested is recommended. | UNMAPPED |

## `PublicationSeriesPublisher.fromDate`

Validation Target: `VT.OUTPUT.PublicationSeriesPublisher.FromDate`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.PublicationSeriesPublisher.FromDate.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of PublicationSeriesPublisher.fromDate is later than allowed by the configured date constraints. | UNMAPPED |
| C.OUTPUT.PublicationSeriesPublisher.FromDate.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of PublicationSeriesPublisher.fromDate is earlier than allowed by the configured date constraints. | UNMAPPED |
| C.OUTPUT.PublicationSeriesPublisher.FromDate.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for PublicationSeriesPublisher.fromDate is recommended. | UNMAPPED |

## `PublicationSeriesPublisher.toDate`

Validation Target: `VT.OUTPUT.PublicationSeriesPublisher.ToDate`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.PublicationSeriesPublisher.ToDate.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of PublicationSeriesPublisher.toDate is earlier than allowed by the configured date constraints. | UNMAPPED |

## `PublicationUnit.numberOfPages`

Validation Target: `VT.OUTPUT.PublicationUnit.NumberOfPages`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.PublicationUnit.NumberOfPages.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of PublicationUnit.numberOfPages exceeds the maximum allowed value. | UNMAPPED |
| C.OUTPUT.PublicationUnit.NumberOfPages.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of PublicationUnit.numberOfPages is below the minimum allowed value. | UNMAPPED |

## `PublicationUnitPart.numberOfPages`

Validation Target: `VT.OUTPUT.PublicationUnitPart.NumberOfPages`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.PublicationUnitPart.NumberOfPages.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of PublicationUnitPart.numberOfPages exceeds the maximum allowed value. | UNMAPPED |
| C.OUTPUT.PublicationUnitPart.NumberOfPages.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of PublicationUnitPart.numberOfPages is below the minimum allowed value. | UNMAPPED |

## `Thesis.thesisDefenceDate`

Validation Target: `VT.OUTPUT.Thesis.ThesisDefenceDate`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.Thesis.ThesisDefenceDate.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of Thesis.thesisDefenceDate is later than allowed by the configured date constraints. | UNMAPPED |
| C.OUTPUT.Thesis.ThesisDefenceDate.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of Thesis.thesisDefenceDate is earlier than allowed by the configured date constraints. | UNMAPPED |
| C.OUTPUT.Thesis.ThesisDefenceDate.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Thesis.thesisDefenceDate is recommended. | UNMAPPED |

## `Thesis.topicAcceptanceDate`

Validation Target: `VT.OUTPUT.Thesis.TopicAcceptanceDate`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.Thesis.TopicAcceptanceDate.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of Thesis.topicAcceptanceDate is later than allowed by the configured date constraints. | UNMAPPED |
| C.OUTPUT.Thesis.TopicAcceptanceDate.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of Thesis.topicAcceptanceDate is earlier than allowed by the configured date constraints. | UNMAPPED |
| C.OUTPUT.Thesis.TopicAcceptanceDate.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Thesis.topicAcceptanceDate is recommended. | UNMAPPED |

## `ThesisPhysicalDescription.numberOfAppendices`

Validation Target: `VT.OUTPUT.ThesisPhysicalDescription.NumberOfAppendices`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.ThesisPhysicalDescription.NumberOfAppendices.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of ThesisPhysicalDescription.numberOfAppendices exceeds the maximum allowed value. | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfAppendices.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of ThesisPhysicalDescription.numberOfAppendices is below the minimum allowed value. | UNMAPPED |

## `ThesisPhysicalDescription.numberOfChapters`

Validation Target: `VT.OUTPUT.ThesisPhysicalDescription.NumberOfChapters`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.ThesisPhysicalDescription.NumberOfChapters.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of ThesisPhysicalDescription.numberOfChapters exceeds the maximum allowed value. | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfChapters.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of ThesisPhysicalDescription.numberOfChapters is below the minimum allowed value. | UNMAPPED |

## `ThesisPhysicalDescription.numberOfGraphs`

Validation Target: `VT.OUTPUT.ThesisPhysicalDescription.NumberOfGraphs`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.ThesisPhysicalDescription.NumberOfGraphs.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of ThesisPhysicalDescription.numberOfGraphs exceeds the maximum allowed value. | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfGraphs.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of ThesisPhysicalDescription.numberOfGraphs is below the minimum allowed value. | UNMAPPED |

## `ThesisPhysicalDescription.numberOfIlustrations`

Validation Target: `VT.OUTPUT.ThesisPhysicalDescription.NumberOfIlustrations`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.ThesisPhysicalDescription.NumberOfIlustrations.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of ThesisPhysicalDescription.numberOfIlustrations exceeds the maximum allowed value. | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfIlustrations.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of ThesisPhysicalDescription.numberOfIlustrations is below the minimum allowed value. | UNMAPPED |

## `ThesisPhysicalDescription.numberOfPages`

Validation Target: `VT.OUTPUT.ThesisPhysicalDescription.NumberOfPages`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.ThesisPhysicalDescription.NumberOfPages.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of ThesisPhysicalDescription.numberOfPages exceeds the maximum allowed value. | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfPages.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of ThesisPhysicalDescription.numberOfPages is below the minimum allowed value. | UNMAPPED |

## `ThesisPhysicalDescription.numberOfReferences`

Validation Target: `VT.OUTPUT.ThesisPhysicalDescription.NumberOfReferences`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.ThesisPhysicalDescription.NumberOfReferences.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of ThesisPhysicalDescription.numberOfReferences exceeds the maximum allowed value. | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfReferences.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of ThesisPhysicalDescription.numberOfReferences is below the minimum allowed value. | UNMAPPED |

## `ThesisPhysicalDescription.numberOfTables`

Validation Target: `VT.OUTPUT.ThesisPhysicalDescription.NumberOfTables`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.OUTPUT.ThesisPhysicalDescription.NumberOfTables.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of ThesisPhysicalDescription.numberOfTables exceeds the maximum allowed value. | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfTables.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of ThesisPhysicalDescription.numberOfTables is below the minimum allowed value. | UNMAPPED |
