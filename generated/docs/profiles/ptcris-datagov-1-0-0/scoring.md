# Scoring policy — PTCRIS-DATAGOV-1.0.0

Minimum required score: **60**

## Constraint-type defaults

| Weight key | Weight | Included in score | Description |
|---|---:|---|---|
| PRESENCE |  | False | Presence affects requirement-level validity/reporting and is not scored by the legacy scoring model. |
| MINIMUM | 3 | True | Default weight for minimum length/value/cardinality/date constraints. |
| MAXIMUM | 1 | True | Default weight for maximum length/value/cardinality/date constraints. |
| REGEX | 3 | True | Default weight for regular-expression/format constraints. |
| UNIQUENESS | 5 | True | Default weight for uniqueness constraints. |
| VOCABULARY | 3 | True | Default weight for controlled-vocabulary constraints. |
| RESOLVABLE | 5 | True | Default weight for resolver constraints. |
| CUSTOM | 5 | True | Default weight for custom/business constraints. |

## Target importance

| Domain | Validation target | Importance | Requirement level | Blocking on presence failure |
|---|---|---:|---|---|
| ACTIVITY | VT.ACTIVITY.Involvement.FromDate | 3 | RECOMMENDED | False |
| ACTIVITY | VT.ACTIVITY.Involvement.ResearchAreas | 5 | MANDATORY | True |
| ACTIVITY | VT.ACTIVITY.Involvement.ToDate | 3 | RECOMMENDED | False |
| ACTIVITY | VT.ACTIVITY.PersonContribution.FromDate | 3 | RECOMMENDED | False |
| ACTIVITY | VT.ACTIVITY.PersonContribution.ResearchAreas | 3 | RECOMMENDED | False |
| ACTIVITY | VT.ACTIVITY.PersonContribution.ToDate | 3 | RECOMMENDED | False |
| ACTIVITY | VT.ACTIVITY.PersonDocumentContribution.IsCorrespondingContributor | 1 | OPTIONAL | False |
| ACTIVITY | VT.ACTIVITY.PersonDocumentContribution.IsMainContributor | 1 | OPTIONAL | False |
| ACTIVITY | VT.ACTIVITY.PersonDocumentContribution.Person | 1 | OPTIONAL | False |
| ACTIVITY | VT.ACTIVITY.PersonEventContribution.Case | 1 | OPTIONAL | False |
| ACTIVITY | VT.ACTIVITY.PersonEventContribution.LabHoursPerWeek | 1 | OPTIONAL | False |
| ACTIVITY | VT.ACTIVITY.PersonEventContribution.LectureHoursPerWeek | 1 | OPTIONAL | False |
| ACTIVITY | VT.ACTIVITY.PersonEventContribution.LocationJurisdiction | 1 | OPTIONAL | False |
| ACTIVITY | VT.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment | 1 | OPTIONAL | False |
| ACTIVITY | VT.ACTIVITY.PersonEventContribution.OtherContactHoursPerWeek | 1 | OPTIONAL | False |
| ACTIVITY | VT.ACTIVITY.PersonEventContribution.TutorialHoursPerWeek | 1 | OPTIONAL | False |
| FUNDING | VT.FUNDING.Funding.Amount | 5 | MANDATORY | True |
| FUNDING | VT.FUNDING.Funding.CreateDate | 5 | MANDATORY | True |
| FUNDING | VT.FUNDING.Funding.DateAwarded | 3 | RECOMMENDED | False |
| FUNDING | VT.FUNDING.Funding.DateSubmitted | 1 | OPTIONAL | False |
| FUNDING | VT.FUNDING.Funding.Description | 5 | MANDATORY | True |
| FUNDING | VT.FUNDING.Funding.Doi | 3 | RECOMMENDED | False |
| FUNDING | VT.FUNDING.Funding.FromDate | 5 | MANDATORY | True |
| FUNDING | VT.FUNDING.Funding.Identifiers | 5 | MANDATORY | True |
| FUNDING | VT.FUNDING.Funding.LastModificationDate | 5 | MANDATORY | True |
| FUNDING | VT.FUNDING.Funding.MetadataAccessLevel | 5 | MANDATORY | True |
| FUNDING | VT.FUNDING.Funding.MetadataLicense | 5 | MANDATORY | True |
| FUNDING | VT.FUNDING.Funding.Name | 5 | MANDATORY | True |
| FUNDING | VT.FUNDING.Funding.ProjectInvolvement | 5 | MANDATORY | True |
| FUNDING | VT.FUNDING.Funding.ProjectReferenceIdGrantAgreementId | 3 | RECOMMENDED | False |
| FUNDING | VT.FUNDING.Funding.ResearchAreas | 3 | RECOMMENDED | False |
| FUNDING | VT.FUNDING.Funding.ToDate | 5 | MANDATORY | True |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.Active | 1 | OPTIONAL | False |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.CreateDate | 5 | MANDATORY | True |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.DateDissolved | 1 | OPTIONAL | False |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.DateEstablished | 3 | RECOMMENDED | False |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.Description | 5 | MANDATORY | True |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.Fundref | 1 | OPTIONAL | False |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.Grid | 1 | OPTIONAL | False |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.Isni | 1 | OPTIONAL | False |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.LastModificationDate | 5 | MANDATORY | True |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel | 5 | MANDATORY | True |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense | 5 | MANDATORY | True |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.Name | 5 | MANDATORY | True |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId | 1 | OPTIONAL | False |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.PostalAddress | 1 | OPTIONAL | False |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.Ringgold | 1 | OPTIONAL | False |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.Ror | 3 | RECOMMENDED | False |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.RorIsni | 5 | MANDATORY | True |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid | 1 | OPTIONAL | False |
| ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.Sector | 3 | RECOMMENDED | False |
| OUTPUT | VT.OUTPUT.Document.Contributors | 5 | MANDATORY | True |
| OUTPUT | VT.OUTPUT.Document.CreateDate | 5 | MANDATORY | True |
| OUTPUT | VT.OUTPUT.Document.Description | 5 | MANDATORY | True |
| OUTPUT | VT.OUTPUT.Document.DocumentDate | 5 | MANDATORY | True |
| OUTPUT | VT.OUTPUT.Document.Doi | 3 | RECOMMENDED | False |
| OUTPUT | VT.OUTPUT.Document.Handle | 3 | RECOMMENDED | False |
| OUTPUT | VT.OUTPUT.Document.Identifiers | 5 | MANDATORY | True |
| OUTPUT | VT.OUTPUT.Document.LastModificationDate | 5 | MANDATORY | True |
| OUTPUT | VT.OUTPUT.Document.MetadataAccessLevel | 5 | MANDATORY | True |
| OUTPUT | VT.OUTPUT.Document.MetadataLicense | 5 | MANDATORY | True |
| OUTPUT | VT.OUTPUT.Document.OpenAccess | 3 | RECOMMENDED | False |
| OUTPUT | VT.OUTPUT.Document.ResearchAreas | 5 | MANDATORY | True |
| OUTPUT | VT.OUTPUT.Document.Title | 5 | MANDATORY | True |
| OUTPUT | VT.OUTPUT.IntellectualProperty.DateEndTerm | 3 | RECOMMENDED | False |
| OUTPUT | VT.OUTPUT.IntellectualProperty.DateFilingPriority | 3 | RECOMMENDED | False |
| OUTPUT | VT.OUTPUT.IntellectualProperty.DateRequested | 3 | RECOMMENDED | False |
| OUTPUT | VT.OUTPUT.PublicationSeriesPublisher.FromDate | 3 | RECOMMENDED | False |
| OUTPUT | VT.OUTPUT.PublicationSeriesPublisher.ToDate | 1 | OPTIONAL | False |
| OUTPUT | VT.OUTPUT.PublicationUnit.NumberOfPages | 1 | OPTIONAL | False |
| OUTPUT | VT.OUTPUT.PublicationUnitPart.NumberOfPages | 1 | OPTIONAL | False |
| OUTPUT | VT.OUTPUT.Thesis.ThesisDefenceDate | 3 | RECOMMENDED | False |
| OUTPUT | VT.OUTPUT.Thesis.TopicAcceptanceDate | 3 | RECOMMENDED | False |
| OUTPUT | VT.OUTPUT.ThesisPhysicalDescription.NumberOfAppendices | 1 | OPTIONAL | False |
| OUTPUT | VT.OUTPUT.ThesisPhysicalDescription.NumberOfChapters | 1 | OPTIONAL | False |
| OUTPUT | VT.OUTPUT.ThesisPhysicalDescription.NumberOfGraphs | 1 | OPTIONAL | False |
| OUTPUT | VT.OUTPUT.ThesisPhysicalDescription.NumberOfIlustrations | 1 | OPTIONAL | False |
| OUTPUT | VT.OUTPUT.ThesisPhysicalDescription.NumberOfPages | 1 | OPTIONAL | False |
| OUTPUT | VT.OUTPUT.ThesisPhysicalDescription.NumberOfReferences | 1 | OPTIONAL | False |
| OUTPUT | VT.OUTPUT.ThesisPhysicalDescription.NumberOfTables | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.Education.DegreeType | 5 | MANDATORY | True |
| PERSON | VT.PERSON.Education.EducationStatus | 3 | RECOMMENDED | False |
| PERSON | VT.PERSON.Employment.EmploymentPositionHierarchy | 5 | MANDATORY | True |
| PERSON | VT.PERSON.ExpertiseOrSkill.ResearchAreas | 3 | RECOMMENDED | False |
| PERSON | VT.PERSON.Involvement.FromDate | 3 | RECOMMENDED | False |
| PERSON | VT.PERSON.Involvement.FundingPartsFunding | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.Involvement.InvolvementType | 5 | MANDATORY | True |
| PERSON | VT.PERSON.Involvement.ToDate | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.LanguageKnowledge.AcademicReview | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.LanguageKnowledge.AcademicWriting | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.LanguageKnowledge.Listening | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.LanguageKnowledge.Overall | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.LanguageKnowledge.Reading | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.LanguageKnowledge.Speaking | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.LanguageKnowledge.Writing | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.Membership.MembershipType | 5 | MANDATORY | True |
| PERSON | VT.PERSON.Person.AuthenticusId | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.Person.Biography | 5 | MANDATORY | True |
| PERSON | VT.PERSON.Person.CreateDate | 5 | MANDATORY | True |
| PERSON | VT.PERSON.Person.Involvements | 5 | MANDATORY | True |
| PERSON | VT.PERSON.Person.LastModificationDate | 5 | MANDATORY | True |
| PERSON | VT.PERSON.Person.LattesId | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.Person.MetadataAccessLevel | 5 | MANDATORY | True |
| PERSON | VT.PERSON.Person.MetadataLicense | 5 | MANDATORY | True |
| PERSON | VT.PERSON.Person.Name | 5 | MANDATORY | True |
| PERSON | VT.PERSON.Person.NationalIdCienciaId | 5 | MANDATORY | True |
| PERSON | VT.PERSON.Person.OpenAlexId | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.Person.Orcid | 3 | RECOMMENDED | False |
| PERSON | VT.PERSON.Person.ScholarId | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.Person.ScopusAuthorId | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.Person.WebOfScienceResearcherId | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.PersonName.Firstname | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.PersonName.Lastname | 5 | MANDATORY | True |
| PERSON | VT.PERSON.PersonName.OtherName | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.PersonName.PersonNameType | 5 | MANDATORY | True |
| PERSON | VT.PERSON.PersonalInfo.BirthDate | 3 | RECOMMENDED | False |
| PERSON | VT.PERSON.PersonalInfo.Sex | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.Prize.EffectiveDate | 5 | MANDATORY | True |
| PERSON | VT.PERSON.Prize.ResearchAreas | 3 | RECOMMENDED | False |
| PERSON | VT.PERSON.Prize.ToDate | 1 | OPTIONAL | False |
| PERSON | VT.PERSON.Prize.Type | 5 | MANDATORY | True |
| PROJECT | VT.PROJECT.Project.Costs | 1 | OPTIONAL | False |
| PROJECT | VT.PROJECT.Project.CreateDate | 5 | MANDATORY | True |
| PROJECT | VT.PROJECT.Project.Description | 5 | MANDATORY | True |
| PROJECT | VT.PROJECT.Project.Doi | 3 | RECOMMENDED | False |
| PROJECT | VT.PROJECT.Project.FromDate | 5 | MANDATORY | True |
| PROJECT | VT.PROJECT.Project.Fundings | 5 | MANDATORY | True |
| PROJECT | VT.PROJECT.Project.Identifiers | 5 | MANDATORY | True |
| PROJECT | VT.PROJECT.Project.LastModificationDate | 5 | MANDATORY | True |
| PROJECT | VT.PROJECT.Project.MetadataAccessLevel | 5 | MANDATORY | True |
| PROJECT | VT.PROJECT.Project.MetadataLicense | 5 | MANDATORY | True |
| PROJECT | VT.PROJECT.Project.Name | 5 | MANDATORY | True |
| PROJECT | VT.PROJECT.Project.NationalIdProjectReference | 5 | MANDATORY | True |
| PROJECT | VT.PROJECT.Project.Organisations | 5 | MANDATORY | True |
| PROJECT | VT.PROJECT.Project.Raid | 3 | RECOMMENDED | False |
| PROJECT | VT.PROJECT.Project.ResearchAreas | 5 | MANDATORY | True |
| PROJECT | VT.PROJECT.Project.Team | 3 | RECOMMENDED | False |
| PROJECT | VT.PROJECT.Project.ToDate | 5 | MANDATORY | True |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.Contact.ContactEmail | 1 | OPTIONAL | False |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.Contact.FaxNumber | 1 | OPTIONAL | False |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.Contact.MobilePhoneNumber | 1 | OPTIONAL | False |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.Contact.PhoneNumber | 1 | OPTIONAL | False |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.Country.Code | 5 | MANDATORY | True |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.Currency.Code | 5 | MANDATORY | True |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.Currency.Symbol | 1 | OPTIONAL | False |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue | 5 | MANDATORY | True |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.EntityIndicator.Subclass | 1 | OPTIONAL | False |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.FlexibleDate.Day | 3 | RECOMMENDED | False |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.FlexibleDate.Month | 3 | RECOMMENDED | False |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.FlexibleDate.TextYear | 5 | MANDATORY | True |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.FlexibleDate.Year | 3 | RECOMMENDED | False |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.GeoLocation.Address | 3 | RECOMMENDED | False |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.GeoLocation.Latitude | 5 | MANDATORY | True |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.GeoLocation.Longitude | 5 | MANDATORY | True |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.Identifier.RegularExpression | 3 | RECOMMENDED | False |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.Language.LanguageCode | 5 | MANDATORY | True |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.LanguageTag.LanguageTag | 5 | MANDATORY | True |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.MonetaryAmount.Amount | 5 | MANDATORY | True |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.Height | 5 | MANDATORY | True |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset | 5 | MANDATORY | True |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset | 5 | MANDATORY | True |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.Width | 5 | MANDATORY | True |
| SHARED_COMPONENTS | VT.SHARED_COMPONENTS.ResearchArea.Name | 5 | MANDATORY | True |
