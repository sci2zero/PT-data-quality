# Review required — PTCRIS-DATAGOV-1.0.0

| Type | Artifact | Notes |
|---|---|---|
| Validation Target | VT.PERSON.Involvement.ToDate | dateDissolved not present in PTCRIS, this constraint is for future use, if dateDissolved is introduced in future |
| Validation Target | VT.PERSON.PersonalInfo.Sex | Female, Male (maybe to introduce Other) |
| Validation Target | VT.ORGANISATION_UNIT.OrganisationUnit.PostalAddress | If postalAddress is provided, and location is provided, can it be checked whether it is aligned |
| Constraint | C.PERSON.ExpertiseOrSkill.ResearchAreas.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.Involvement.FundingPartsFunding.custom |  |
| Constraint | C.PERSON.Person.Biography.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.Person.Biography.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.Person.CreateDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.Person.Involvements.custom |  |
| Constraint | C.PERSON.Person.LastModificationDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.Person.LattesId.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.Person.MetadataAccessLevel.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.Person.MetadataAccessLevel.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.Person.MetadataLicense.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.Person.MetadataLicense.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.Person.Name.maxLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.Person.Name.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.Person.Name.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.Person.ScholarId.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.PersonName.Firstname.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.PersonName.OtherName.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.PersonName.PersonNameType.maxLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.PersonName.PersonNameType.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.PersonalInfo.BirthDate.maxDate | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.PersonalInfo.Sex.maxLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.PersonalInfo.Sex.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PERSON.Prize.EffectiveDate.minDate |  |
| Constraint | C.PERSON.Prize.ResearchAreas.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.ORGANISATION_UNIT.OrganisationUnit.CreateDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.ORGANISATION_UNIT.OrganisationUnit.Description.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.ORGANISATION_UNIT.OrganisationUnit.Description.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.ORGANISATION_UNIT.OrganisationUnit.Fundref.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.ORGANISATION_UNIT.OrganisationUnit.Isni.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.ORGANISATION_UNIT.OrganisationUnit.LastModificationDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.ORGANISATION_UNIT.OrganisationUnit.Ringgold.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.ORGANISATION_UNIT.OrganisationUnit.RorIsni.unique | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.Costs.custom |  |
| Constraint | C.PROJECT.Project.CreateDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.Description.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.Description.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.Identifiers.minCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.Identifiers.unique | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.Fundings.custom |  |
| Constraint | C.PROJECT.Project.Fundings.maxCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.Fundings.minCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.LastModificationDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.MetadataAccessLevel.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.MetadataAccessLevel.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.MetadataLicense.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.MetadataLicense.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.Name.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.Organisations.custom |  |
| Constraint | C.PROJECT.Project.Organisations.maxCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.Organisations.minCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.ResearchAreas.unique | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.ResearchAreas.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.Team.custom |  |
| Constraint | C.PROJECT.Project.Team.maxCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.PROJECT.Project.Team.minCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.FUNDING.Funding.CreateDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.FUNDING.Funding.Description.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.FUNDING.Funding.Description.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.FUNDING.Funding.Identifiers.minCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.FUNDING.Funding.FromDate.maxDate | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.FUNDING.Funding.LastModificationDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.FUNDING.Funding.MetadataAccessLevel.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.FUNDING.Funding.MetadataAccessLevel.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.FUNDING.Funding.MetadataLicense.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.FUNDING.Funding.MetadataLicense.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.FUNDING.Funding.Name.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.FUNDING.Funding.ProjectInvolvement.custom |  |
| Constraint | C.FUNDING.Funding.ProjectInvolvement.minCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.FUNDING.Funding.ProjectInvolvement.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.FUNDING.Funding.ResearchAreas.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.FUNDING.Funding.ToDate.maxDate | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.OUTPUT.Document.Contributors.custom |  |
| Constraint | C.OUTPUT.Document.Contributors.minCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.OUTPUT.Document.CreateDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.OUTPUT.Document.Description.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.OUTPUT.Document.Description.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.OUTPUT.Document.Identifiers.minCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.OUTPUT.Document.Identifiers.unique | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.OUTPUT.Document.LastModificationDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.OUTPUT.Document.MetadataAccessLevel.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.OUTPUT.Document.MetadataAccessLevel.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.OUTPUT.Document.MetadataLicense.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.OUTPUT.Document.MetadataLicense.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.OUTPUT.Document.ResearchAreas.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.ACTIVITY.Involvement.ResearchAreas.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.ACTIVITY.PersonContribution.ResearchAreas.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.ACTIVITY.PersonDocumentContribution.IsCorrespondingContributor.custom |  |
| Constraint | C.ACTIVITY.PersonDocumentContribution.IsMainContributor.custom |  |
| Constraint | C.ACTIVITY.PersonDocumentContribution.Person.custom |  |
| Constraint | C.ACTIVITY.PersonEventContribution.Case.custom |  |
| Constraint | C.ACTIVITY.PersonEventContribution.LabHoursPerWeek.custom |  |
| Constraint | C.ACTIVITY.PersonEventContribution.LectureHoursPerWeek.custom |  |
| Constraint | C.ACTIVITY.PersonEventContribution.LocationJurisdiction.custom |  |
| Constraint | C.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment.custom |  |
| Constraint | C.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment.minValue | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.ACTIVITY.PersonEventContribution.OtherContactHoursPerWeek.custom |  |
| Constraint | C.ACTIVITY.PersonEventContribution.TutorialHoursPerWeek.custom |  |
| Constraint | C.SHARED_COMPONENTS.Contact.ContactEmail.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.Country.Code.maxLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.Country.Code.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.Currency.Code.maxLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.Currency.Code.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.Currency.Code.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.Currency.Symbol.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue.custom |  |
| Constraint | C.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.EntityIndicator.Subclass.custom |  |
| Constraint | C.SHARED_COMPONENTS.FlexibleDate.Day.custom |  |
| Constraint | C.SHARED_COMPONENTS.FlexibleDate.TextYear.custom |  |
| Constraint | C.SHARED_COMPONENTS.FlexibleDate.TextYear.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.GeoLocation.Latitude.maxValue | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.GeoLocation.Latitude.minValue | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.GeoLocation.Longitude.maxValue | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.GeoLocation.Longitude.minValue | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.Identifier.RegularExpression.custom |  |
| Constraint | C.SHARED_COMPONENTS.Language.LanguageCode.maxLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.Language.LanguageCode.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.Language.LanguageCode.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.LanguageTag.LanguageTag.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.MonetaryAmount.Amount.maxValue | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.MonetaryAmount.Amount.minValue | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset.minValue | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset.minValue | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | C.SHARED_COMPONENTS.ResearchArea.Name.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint Parameter | P.C.PERSON.Prize.EffectiveDate.minDate.minDate.1 | Legacy numeric minimum for a date field is ambiguous; preserved without interpretation. |
| Message | MSG.PERSON.ExpertiseOrSkill.ResearchAreas.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.Involvement.FundingPartsFunding.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.Person.Biography.minLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.Person.Biography.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.Person.CreateDate.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.Person.Involvements.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.Person.LastModificationDate.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.Person.LattesId.pattern | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.Person.MetadataAccessLevel.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.Person.MetadataAccessLevel.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.Person.MetadataLicense.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.Person.MetadataLicense.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.Person.Name.maxLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.Person.Name.minLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.Person.Name.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.Person.ScholarId.pattern | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.PersonName.Firstname.minLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.PersonName.OtherName.minLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.PersonName.PersonNameType.maxLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.PersonName.PersonNameType.minLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.PersonalInfo.BirthDate.maxDate | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.PersonalInfo.Sex.maxLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.PersonalInfo.Sex.minLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.Prize.EffectiveDate.minDate | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PERSON.Prize.ResearchAreas.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ORGANISATION_UNIT.OrganisationUnit.CreateDate.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ORGANISATION_UNIT.OrganisationUnit.Description.minLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ORGANISATION_UNIT.OrganisationUnit.Description.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ORGANISATION_UNIT.OrganisationUnit.Fundref.pattern | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ORGANISATION_UNIT.OrganisationUnit.Isni.pattern | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ORGANISATION_UNIT.OrganisationUnit.LastModificationDate.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ORGANISATION_UNIT.OrganisationUnit.Ringgold.pattern | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ORGANISATION_UNIT.OrganisationUnit.RorIsni.unique | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid.pattern | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.Costs.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.CreateDate.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.Description.minLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.Description.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.Identifiers.minCardinality | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.Identifiers.unique | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.Fundings.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.Fundings.maxCardinality | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.Fundings.minCardinality | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.LastModificationDate.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.MetadataAccessLevel.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.MetadataAccessLevel.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.MetadataLicense.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.MetadataLicense.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.Name.minLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.Organisations.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.Organisations.maxCardinality | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.Organisations.minCardinality | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.ResearchAreas.unique | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.ResearchAreas.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.Team.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.Team.maxCardinality | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.PROJECT.Project.Team.minCardinality | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.CreateDate.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.Description.minLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.Description.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.Identifiers.minCardinality | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.FromDate.maxDate | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.LastModificationDate.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.MetadataAccessLevel.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.MetadataAccessLevel.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.MetadataLicense.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.MetadataLicense.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.Name.minLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.ProjectInvolvement.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.ProjectInvolvement.minCardinality | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.ProjectInvolvement.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.ProjectReferenceId.maxLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.ProjectReferenceId.minLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.ProjectReferenceId.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.ProjectReferenceId.unique | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.ResearchAreas.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.FUNDING.Funding.ToDate.maxDate | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.OUTPUT.Document.Contributors.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.OUTPUT.Document.Contributors.minCardinality | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.OUTPUT.Document.CreateDate.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.OUTPUT.Document.Description.minLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.OUTPUT.Document.Description.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.OUTPUT.Document.Identifiers.minCardinality | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.OUTPUT.Document.Identifiers.unique | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.OUTPUT.Document.LastModificationDate.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.OUTPUT.Document.MetadataAccessLevel.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.OUTPUT.Document.MetadataAccessLevel.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.OUTPUT.Document.MetadataLicense.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.OUTPUT.Document.MetadataLicense.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.OUTPUT.Document.ResearchAreas.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ACTIVITY.Involvement.ResearchAreas.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ACTIVITY.PersonContribution.ResearchAreas.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ACTIVITY.PersonDocumentContribution.IsCorrespondingContributor.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ACTIVITY.PersonDocumentContribution.IsMainContributor.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ACTIVITY.PersonDocumentContribution.Person.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ACTIVITY.PersonEventContribution.Case.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ACTIVITY.PersonEventContribution.LabHoursPerWeek.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ACTIVITY.PersonEventContribution.LectureHoursPerWeek.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ACTIVITY.PersonEventContribution.LocationJurisdiction.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment.minValue | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ACTIVITY.PersonEventContribution.OtherContactHoursPerWeek.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.ACTIVITY.PersonEventContribution.TutorialHoursPerWeek.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.Contact.ContactEmail.pattern | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.Country.Code.maxLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.Country.Code.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.Currency.Code.maxLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.Currency.Code.pattern | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.Currency.Code.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.Currency.Symbol.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.EntityIndicator.Subclass.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.FlexibleDate.Day.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.FlexibleDate.TextYear.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.FlexibleDate.TextYear.presence | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.GeoLocation.Latitude.maxValue | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.GeoLocation.Latitude.minValue | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.GeoLocation.Longitude.maxValue | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.GeoLocation.Longitude.minValue | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.Identifier.RegularExpression.custom | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.Language.LanguageCode.maxLength | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.Language.LanguageCode.pattern | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.Language.LanguageCode.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.LanguageTag.LanguageTag.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.MonetaryAmount.Amount.maxValue | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.MonetaryAmount.Amount.minValue | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset.minValue | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset.minValue | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Message | MSG.SHARED_COMPONENTS.ResearchArea.Name.vocabulary | Generic runtime placeholders removed; one logical message retained per Constraint. |
| Governance Mapping | GM.0001 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0004 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0005 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0007 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0011 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0012 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0013 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0015 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0016 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0017 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0018 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0020 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0021 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0023 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0024 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0026 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0027 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0029 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0030 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0032 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0033 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0035 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0036 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0038 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0051 | Inferred from constraint type CUSTOM and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0052 | Inferred from constraint type MAX_CARDINALITY and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0075 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0092 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0124 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0125 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0126 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0130 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0131 | Inferred from constraint type MAX_LENGTH and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0132 | Inferred from constraint type MIN_LENGTH and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0134 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0135 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0137 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0139 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0140 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0142 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0144 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0145 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0146 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0153 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSTRUCT. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-02 using constraint type. |
| Governance Mapping | GM.0157 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSTRUCT. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-02 using constraint type. |
| Governance Mapping | GM.0161 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSTRUCT. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-02 using constraint type. |
| Governance Mapping | GM.0167 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0168 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0170 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0174 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSTRUCT. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-02 using constraint type. |
| Governance Mapping | GM.0178 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSTRUCT. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-02 using constraint type. |
| Governance Mapping | GM.0183 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSTRUCT. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-02 using constraint type. |
| Governance Mapping | GM.0185 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSTRUCT. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-02 using constraint type. |
| Governance Mapping | GM.0189 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSTRUCT. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-02 using constraint type. |
| Governance Mapping | GM.0190 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0198 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0204 | Inferred from constraint type UNIQUENESS and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. |
| Governance Mapping | GM.0209 | Inferred from constraint type MAX_CARDINALITY and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0210 | Inferred from constraint type MIN_CARDINALITY and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0211 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0217 | Inferred from constraint type MAX_LENGTH and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0218 | Inferred from constraint type MIN_LENGTH and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0220 | Inferred from constraint type REGEX and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0223 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0227 | Inferred from constraint type MAX_CARDINALITY and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0228 | Inferred from constraint type MIN_CARDINALITY and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0229 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0232 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0236 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0237 | Inferred from constraint type UNIQUENESS and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. |
| Governance Mapping | GM.0240 | Inferred from constraint type MAX_CARDINALITY and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0241 | Inferred from constraint type MIN_CARDINALITY and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0242 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0248 | Inferred from constraint type MAX_DATE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCURREN normalized to unique metric PTCRIS-F1-01DCURREN-01 using constraint type. |
| Governance Mapping | GM.0249 | Inferred from constraint type MIN_DATE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCURREN normalized to unique metric PTCRIS-F1-01DCURREN-01 using constraint type. |
| Governance Mapping | GM.0251 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0252 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0257 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0261 | Inferred from constraint type MIN_CARDINALITY and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0262 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0265 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0273 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0275 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DQUALIT. Source metric identifier PTCRIS-F1-01DQUALIT normalized to unique metric PTCRIS-F1-01DQUALIT-02 using target semantics. |
| Governance Mapping | GM.0276 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DQUALIT. Source metric identifier PTCRIS-F1-01DQUALIT normalized to unique metric PTCRIS-F1-01DQUALIT-02 using target semantics. |
| Governance Mapping | GM.0277 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DQUALIT. Source metric identifier PTCRIS-F1-01DQUALIT normalized to unique metric PTCRIS-F1-01DQUALIT-02 using target semantics. |
| Governance Mapping | GM.0280 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0282 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DSEMANT. Source metric identifier PTCRIS-F1-01DSEMANT normalized to unique metric PTCRIS-F1-01DSEMANT-06 using constraint type. |
| Governance Mapping | GM.0286 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0287 | Inferred from constraint type CUSTOM and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0295 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0298 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0304 | Inferred from constraint type UNIQUENESS and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. |
| Governance Mapping | GM.0307 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0316 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0318 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0320 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0321 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0325 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0328 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0331 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0334 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0342 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0345 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0362 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0363 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0366 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0369 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0370 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0373 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0378 | Inferred from constraint type CUSTOM and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0388 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0389 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0390 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0391 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0392 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0393 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0394 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0395 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0396 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0397 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0398 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0399 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0400 | Inferred from constraint type MAX_LENGTH and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0401 | Inferred from constraint type MIN_LENGTH and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0402 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0403 | Inferred from constraint type UNIQUENESS and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. |
| Governance Mapping | GM.0405 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0406 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0408 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0409 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0410 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0411 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0412 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-02 using constraint type. |
| Governance Mapping | GM.0413 | Confirmed by Portuguese partner feedback: PTCRIS-F1-01DCONSIST. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0414 | Inferred from constraint type CUSTOM and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0415 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0416 | Inferred from constraint type CUSTOM and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0417 | Inferred from constraint type CUSTOM and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0418 | Inferred from constraint type MAX_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0419 | Inferred from constraint type MIN_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0421 | Inferred from constraint type MAX_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0422 | Inferred from constraint type MIN_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0424 | Inferred from constraint type CUSTOM and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0426 | Inferred from constraint type MAX_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0427 | Inferred from constraint type MIN_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0429 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0430 | Inferred from constraint type MAX_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0431 | Inferred from constraint type MIN_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0433 | Inferred from constraint type MAX_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0434 | Inferred from constraint type MIN_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0436 | Inferred from constraint type CUSTOM and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0437 | Inferred from constraint type MAX_LENGTH and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0438 | Inferred from constraint type MIN_LENGTH and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0439 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0440 | Inferred from constraint type MAX_LENGTH and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0441 | Inferred from constraint type MIN_LENGTH and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0442 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0443 | Inferred from constraint type REGEX and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0444 | Inferred from constraint type UNIQUENESS and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. |
| Governance Mapping | GM.0446 | Inferred from constraint type MAX_LENGTH and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0447 | Inferred from constraint type MIN_LENGTH and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0448 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0449 | Inferred from constraint type REGEX and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0450 | Inferred from constraint type UNIQUENESS and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. |
| Governance Mapping | GM.0452 | Inferred from constraint type MAX_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0454 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Governance Mapping | GM.0455 | Inferred from constraint type MAX_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0456 | Inferred from constraint type MIN_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0458 | Inferred from constraint type MAX_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0459 | Inferred from constraint type MIN_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0461 | Inferred from constraint type MAX_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0462 | Inferred from constraint type MIN_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0464 | Inferred from constraint type MAX_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0465 | Inferred from constraint type MIN_VALUE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-04 using constraint type. |
| Governance Mapping | GM.0467 | Inferred from constraint type MAX_LENGTH and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0468 | Inferred from constraint type MIN_LENGTH and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DSTRUCT normalized to unique metric PTCRIS-F1-01DSTRUCT-01 using constraint type. |
| Governance Mapping | GM.0469 | Inferred from constraint type PRESENCE and the authoritative PTCRIS governance catalogue because the partner workbook did not provide a constraint-specific mapping. Review recommended. Source metric identifier PTCRIS-F1-01DCONSIST normalized to unique metric PTCRIS-F1-01DCONSIST-03 using requirement. |
| Implementation Binding | BIND.PT_MASTER.VT.PERSON.Involvement.FundingPartsFunding | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.PERSON.Involvement.ToDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.PERSON.Prize.ToDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.ORGANISATION_UNIT.OrganisationUnit.RorIsni | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.PROJECT.Project.Costs | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.PROJECT.Project.Identifiers | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.PROJECT.Project.Fundings | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.PROJECT.Project.Organisations | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.PROJECT.Project.ResearchAreas | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.PROJECT.Project.Team | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.PROJECT.Project.ToDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.FUNDING.Funding.DateAwarded | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.FUNDING.Funding.DateSubmitted | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.FUNDING.Funding.Identifiers | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.FUNDING.Funding.FromDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.FUNDING.Funding.ProjectInvolvement | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.FUNDING.Funding.ToDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.OUTPUT.Document.Contributors | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.OUTPUT.Document.Identifiers | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.OUTPUT.IntellectualProperty.DateEndTerm | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.OUTPUT.IntellectualProperty.DateFilingPriority | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.OUTPUT.IntellectualProperty.DateRequested | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.OUTPUT.PublicationSeriesPublisher.ToDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.OUTPUT.Thesis.ThesisDefenceDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.ACTIVITY.Involvement.FromDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.ACTIVITY.Involvement.ToDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.ACTIVITY.PersonContribution.FromDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.ACTIVITY.PersonContribution.ToDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.ACTIVITY.PersonDocumentContribution.IsCorrespondingContributor | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.ACTIVITY.PersonDocumentContribution.IsMainContributor | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.ACTIVITY.PersonDocumentContribution.Person | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.ACTIVITY.PersonEventContribution.Case | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.ACTIVITY.PersonEventContribution.LabHoursPerWeek | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.ACTIVITY.PersonEventContribution.LectureHoursPerWeek | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.ACTIVITY.PersonEventContribution.LocationJurisdiction | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.ACTIVITY.PersonEventContribution.OtherContactHoursPerWeek | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.ACTIVITY.PersonEventContribution.TutorialHoursPerWeek | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.SHARED_COMPONENTS.EntityIndicator.Subclass | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation Binding | BIND.PT_MASTER.VT.SHARED_COMPONENTS.FlexibleDate.TextYear | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
