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
| Governance Mapping | GM.0001 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0002 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0003 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0004 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0005 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0007 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0008 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0009 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0010 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0011 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0012 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0013 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0014 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0015 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0016 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0017 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0018 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0019 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0020 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0021 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0022 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0023 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0024 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0025 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0026 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0027 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0028 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0029 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0030 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0031 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0032 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0033 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0034 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0035 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0036 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0037 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0038 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0039 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0040 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0041 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0042 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0043 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0044 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0045 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0046 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0047 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0048 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0049 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0050 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0051 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0052 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0053 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0055 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0056 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0057 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0058 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0059 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0060 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0061 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0062 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0063 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0064 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0065 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0066 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0067 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0068 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0069 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0071 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0072 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0073 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0074 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0075 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0076 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0077 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0078 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0079 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0081 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0082 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0083 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0084 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0085 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0086 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0087 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0088 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0089 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0090 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0091 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0092 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0094 |  |
| Governance Mapping | GM.0096 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0097 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0098 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0099 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0100 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0101 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0102 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0103 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0104 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0105 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0107 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0108 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0109 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0110 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0112 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0113 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0114 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0115 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0116 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0117 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0118 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0121 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0122 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0123 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0124 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0125 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0126 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0127 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0130 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0131 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0132 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0134 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0135 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0136 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0137 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0138 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0139 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0140 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0141 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0142 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0143 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0144 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0145 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0146 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0147 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0148 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0149 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0150 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0151 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0152 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0153 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0154 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0155 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0156 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0157 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0158 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0159 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0160 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0161 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0162 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0163 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0164 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0165 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0166 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0167 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0168 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0169 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0170 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0171 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0172 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0173 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0174 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0175 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0176 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0177 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0178 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0179 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0180 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0181 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0182 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0183 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0184 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0185 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0186 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0187 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0188 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0189 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0190 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0191 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0192 |  |
| Governance Mapping | GM.0193 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0194 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0195 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0196 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0197 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0198 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0199 |  |
| Governance Mapping | GM.0200 |  |
| Governance Mapping | GM.0201 |  |
| Governance Mapping | GM.0204 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0205 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0206 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0209 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0210 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0211 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0212 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0213 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0214 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0215 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0216 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0217 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0218 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0220 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0221 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0222 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0223 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0224 |  |
| Governance Mapping | GM.0226 |  |
| Governance Mapping | GM.0227 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0228 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0229 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0230 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0231 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0232 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0233 |  |
| Governance Mapping | GM.0234 |  |
| Governance Mapping | GM.0235 |  |
| Governance Mapping | GM.0236 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0237 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0238 |  |
| Governance Mapping | GM.0240 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0241 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0242 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0243 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0244 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0246 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0247 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0248 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0249 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0251 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0252 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0253 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0254 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0255 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0256 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0257 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0258 |  |
| Governance Mapping | GM.0259 |  |
| Governance Mapping | GM.0260 |  |
| Governance Mapping | GM.0261 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0262 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0265 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0266 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0267 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0268 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0269 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0270 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0271 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0272 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0273 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0275 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0276 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0277 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0278 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0279 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0280 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0281 |  |
| Governance Mapping | GM.0282 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0283 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0286 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0287 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0288 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0289 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0290 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0291 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0292 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0293 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0294 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0295 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0296 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0297 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0298 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0299 |  |
| Governance Mapping | GM.0300 |  |
| Governance Mapping | GM.0301 |  |
| Governance Mapping | GM.0302 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0303 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0304 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0305 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0306 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0307 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0308 |  |
| Governance Mapping | GM.0309 |  |
| Governance Mapping | GM.0310 |  |
| Governance Mapping | GM.0311 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0312 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0313 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0314 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0315 | Legacy reference mapped at metric/dimension level; exact governance requirement was not assigned. |
| Governance Mapping | GM.0316 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0317 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0318 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0319 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0320 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0321 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0322 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0323 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0324 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0325 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0326 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0327 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0328 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0329 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0330 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0331 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0332 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0333 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0334 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0335 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0336 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0337 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0338 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0339 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0340 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0341 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0342 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0343 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0344 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0345 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0346 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0347 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0348 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0349 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0350 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0351 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0352 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0353 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0354 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0355 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0356 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0357 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0358 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0359 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0360 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0361 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0362 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0363 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0364 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0365 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0366 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0367 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0368 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0369 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0370 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0371 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0372 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0373 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0374 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0375 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0376 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0377 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0378 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0379 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0380 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0381 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0382 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0383 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0384 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0385 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0386 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0387 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0388 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0389 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0390 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0391 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0392 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0393 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0394 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0395 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0396 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0397 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0398 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0399 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0400 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0401 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0402 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0403 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0405 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0406 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0407 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0408 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0409 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0410 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0411 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0412 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0413 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0414 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0415 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0416 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0417 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0418 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0419 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0420 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0421 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0422 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0423 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0424 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0425 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0426 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0427 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0428 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0429 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0430 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0431 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0432 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0433 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0434 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0435 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0436 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0437 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0438 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0439 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0440 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0441 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0442 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0443 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0444 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0445 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0446 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0447 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0448 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0449 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0450 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0451 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0452 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0453 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0454 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0455 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0456 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0457 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0458 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0459 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0460 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0461 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0462 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0463 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0464 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0465 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0466 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0467 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0468 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0469 | No constraint-specific governance mapping could be established from the legacy reference. |
| Governance Mapping | GM.0470 | No constraint-specific governance mapping could be established from the legacy reference. |
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
