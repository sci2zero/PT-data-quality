# ACTIVITY

## `Involvement.fromDate`

Validation Target: `VT.ACTIVITY.Involvement.FromDate`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ACTIVITY.Involvement.FromDate.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of Involvement.fromDate is later than allowed by the configured date constraints. | UNMAPPED |
| C.ACTIVITY.Involvement.FromDate.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of Involvement.fromDate is earlier than allowed by the configured date constraints. | UNMAPPED |
| C.ACTIVITY.Involvement.FromDate.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Involvement.fromDate is recommended. | UNMAPPED |

## `Involvement.researchAreas`

Validation Target: `VT.ACTIVITY.Involvement.ResearchAreas`  
Importance: `5`  
Requirement level: `MANDATORY`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ACTIVITY.Involvement.ResearchAreas.presence | PRESENCE | COMPLETENESS | ERROR | True | 0 | A value for Involvement.researchAreas is required. | UNMAPPED |
| C.ACTIVITY.Involvement.ResearchAreas.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of Involvement.researchAreas must belong to the configured controlled vocabulary. | UNMAPPED |

## `Involvement.toDate`

Validation Target: `VT.ACTIVITY.Involvement.ToDate`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ACTIVITY.Involvement.ToDate.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of Involvement.toDate is earlier than allowed by the configured date constraints. | UNMAPPED |
| C.ACTIVITY.Involvement.ToDate.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for Involvement.toDate is recommended. | UNMAPPED |

## `PersonContribution.fromDate`

Validation Target: `VT.ACTIVITY.PersonContribution.FromDate`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ACTIVITY.PersonContribution.FromDate.maxDate | MAX_DATE | CONSISTENCY | ERROR | True | 1.0 | The value of PersonContribution.fromDate is later than allowed by the configured date constraints. | UNMAPPED |
| C.ACTIVITY.PersonContribution.FromDate.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of PersonContribution.fromDate is earlier than allowed by the configured date constraints. | UNMAPPED |
| C.ACTIVITY.PersonContribution.FromDate.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for PersonContribution.fromDate is recommended. | UNMAPPED |

## `PersonContribution.researchAreas`

Validation Target: `VT.ACTIVITY.PersonContribution.ResearchAreas`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ACTIVITY.PersonContribution.ResearchAreas.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for PersonContribution.researchAreas is recommended. | UNMAPPED |
| C.ACTIVITY.PersonContribution.ResearchAreas.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of PersonContribution.researchAreas must belong to the configured controlled vocabulary. | UNMAPPED |

## `PersonContribution.toDate`

Validation Target: `VT.ACTIVITY.PersonContribution.ToDate`  
Importance: `3`  
Requirement level: `RECOMMENDED`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ACTIVITY.PersonContribution.ToDate.minDate | MIN_DATE | CONSISTENCY | ERROR | True | 3.0 | The value of PersonContribution.toDate is earlier than allowed by the configured date constraints. | UNMAPPED |
| C.ACTIVITY.PersonContribution.ToDate.presence | PRESENCE | COMPLETENESS | WARNING | False | 0 | A value for PersonContribution.toDate is recommended. | UNMAPPED |

## `PersonDocumentContribution.isCorrespondingContributor`

Validation Target: `VT.ACTIVITY.PersonDocumentContribution.IsCorrespondingContributor`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ACTIVITY.PersonDocumentContribution.IsCorrespondingContributor.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | The corresponding contributor flag may be true only for AUTHOR, PRESENTER, or EDITOR contributions. | UNMAPPED |
| C.ACTIVITY.PersonDocumentContribution.IsCorrespondingContributor.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of PersonDocumentContribution.isCorrespondingContributor must belong to the configured controlled vocabulary. | UNMAPPED |

## `PersonDocumentContribution.isMainContributor`

Validation Target: `VT.ACTIVITY.PersonDocumentContribution.IsMainContributor`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ACTIVITY.PersonDocumentContribution.IsMainContributor.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | The main contributor flag may be true only for an allowed main-contribution type such as AUTHOR, PRESENTER, EDITOR, ADVISOR, ARGUER, or BOARD_MEMBER. | UNMAPPED |
| C.ACTIVITY.PersonDocumentContribution.IsMainContributor.vocabulary | VOCABULARY | VALIDITY | ERROR | True | 3.0 | The value of PersonDocumentContribution.isMainContributor must belong to the configured controlled vocabulary. | UNMAPPED |

## `PersonDocumentContribution.person`

Validation Target: `VT.ACTIVITY.PersonDocumentContribution.Person`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ACTIVITY.PersonDocumentContribution.Person.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | A research output may be linked to a person only when the relevant document dates occur after the person's birth date. | UNMAPPED |

## `PersonEventContribution.case`

Validation Target: `VT.ACTIVITY.PersonEventContribution.Case`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ACTIVITY.PersonEventContribution.Case.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | The case field may be specified only for a person-event contribution linked to an OtherEvent of type TRIAL. | UNMAPPED |

## `PersonEventContribution.labHoursPerWeek`

Validation Target: `VT.ACTIVITY.PersonEventContribution.LabHoursPerWeek`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ACTIVITY.PersonEventContribution.LabHoursPerWeek.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | Lab hours per week may be specified only when the person-event contribution is linked to a course. | UNMAPPED |

## `PersonEventContribution.lectureHoursPerWeek`

Validation Target: `VT.ACTIVITY.PersonEventContribution.LectureHoursPerWeek`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ACTIVITY.PersonEventContribution.LectureHoursPerWeek.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | Lecture hours per week may be specified only when the person-event contribution is linked to a course. | UNMAPPED |

## `PersonEventContribution.locationJurisdiction`

Validation Target: `VT.ACTIVITY.PersonEventContribution.LocationJurisdiction`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ACTIVITY.PersonEventContribution.LocationJurisdiction.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | Location jurisdiction may be specified only for a person-event contribution linked to an OtherEvent of type TRIAL. | UNMAPPED |

## `PersonEventContribution.numberOfReviewsOrAssessment`

Validation Target: `VT.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | The number of reviews or assessments may be specified only for a conference contribution with contribution type REVIEWER. | UNMAPPED |
| C.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment.maxValue | MAX_VALUE | CONSISTENCY | ERROR | True | 1.0 | The value of PersonEventContribution.numberOfReviewsOrAssessment exceeds the maximum allowed value. | UNMAPPED |
| C.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment.minValue | MIN_VALUE | CONSISTENCY | ERROR | True | 3.0 | The value of PersonEventContribution.numberOfReviewsOrAssessment is below the minimum allowed value. | UNMAPPED |

## `PersonEventContribution.otherContactHoursPerWeek`

Validation Target: `VT.ACTIVITY.PersonEventContribution.OtherContactHoursPerWeek`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ACTIVITY.PersonEventContribution.OtherContactHoursPerWeek.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | Other contact hours per week may be specified only when the person-event contribution is linked to a course. | UNMAPPED |

## `PersonEventContribution.tutorialHoursPerWeek`

Validation Target: `VT.ACTIVITY.PersonEventContribution.TutorialHoursPerWeek`  
Importance: `1`  
Requirement level: `OPTIONAL`

| Constraint | Type | Dimension | Severity | Blocking | Weight | Message | Governance |
|---|---|---|---|---|---:|---|---|
| C.ACTIVITY.PersonEventContribution.TutorialHoursPerWeek.custom | CUSTOM | CONSISTENCY | ERROR | True | 5.0 | Tutorial hours per week may be specified only when the person-event contribution is linked to a course. | UNMAPPED |
