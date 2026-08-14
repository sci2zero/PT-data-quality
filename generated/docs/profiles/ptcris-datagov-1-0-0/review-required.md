# Review-required items — PTCRIS-DATAGOV-1.0.0

| Type | Domain | ID | Reason / notes |
|---|---|---|---|
| Validation target | PERSON | VT.PERSON.Involvement.ToDate | dateDissolved not present in PTCRIS, this constraint is for future use, if dateDissolved is introduced in future |
| Validation target | PERSON | VT.PERSON.PersonalInfo.Sex | Female, Male (maybe to introduce Other) |
| Validation target | ORGANISATION_UNIT | VT.ORGANISATION_UNIT.OrganisationUnit.PostalAddress | If postalAddress is provided, and location is provided, can it be checked whether it is aligned |
| Validation target | FUNDING | VT.FUNDING.Funding.ProjectReferenceIdGrantAgreementId |  |
| Constraint | PERSON | C.PERSON.ExpertiseOrSkill.ResearchAreas.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.Involvement.FundingPartsFunding.custom | If fundingParts and funding are specified, then involvement.fundingParts.funding should be same as involvement.funding |
| Constraint | PERSON | C.PERSON.Person.Biography.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.Person.Biography.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.Person.CreateDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.Person.Involvements.custom | At least one employment should be linked with Portuguese researcher with startDate, it represents Start Date of Professional Career. Moreover, linked Employment should include employment position. |
| Constraint | PERSON | C.PERSON.Person.Involvements.maxValueOrLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.Person.Involvements.minValueOrLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.Person.LastModificationDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.Person.LattesId.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.Person.MetadataAccessLevel.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.Person.MetadataAccessLevel.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.Person.MetadataLicense.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.Person.MetadataLicense.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.Person.Name.maxLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.Person.Name.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.Person.Name.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.Person.ScholarId.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.PersonName.Firstname.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.PersonName.OtherName.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.PersonName.PersonNameType.maxLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.PersonName.PersonNameType.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.PersonalInfo.BirthDate.maxDate | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.PersonalInfo.Sex.maxLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.PersonalInfo.Sex.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.Prize.ResearchAreas.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PERSON | C.PERSON.Prize.ToDate.maxDate | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.CreateDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Description.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Description.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Fundref.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Isni.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.LastModificationDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Ringgold.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Ror.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.RorIsni.unique | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.Costs.custom | Sum of linked fundings.amount.amount is lower or equal to project.costs.amount. |
| Constraint | PROJECT | C.PROJECT.Project.CreateDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.Description.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.Description.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.Identifiers.minCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.Identifiers.unique | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.Fundings.custom | In the ETL process, the funding ID registered at the project level should be compared with the ID registered in the associated funding entity, values must match perfectly in order to establish relation. |
| Constraint | PROJECT | C.PROJECT.Project.Fundings.maxCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.Fundings.minCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.LastModificationDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.MetadataAccessLevel.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.MetadataAccessLevel.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.MetadataLicense.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.MetadataLicense.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.Name.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.Organisations.custom | The sum of fundingPart.amount of all organisations can not be bigger than Project.funding.amount<br><br>If in the consortium list is one specified as COORDINATOR (contributionType field), there should be also other CONSORTIUM_MEMBER. <br><br>Moreover, if there is more members, and neither of them is a COORDINATOR, it can be also an issue with data. |
| Constraint | PROJECT | C.PROJECT.Project.Organisations.maxCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.Organisations.minCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.ResearchAreas.unique | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.ResearchAreas.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.Team.custom | If team members are specified, there should be at least one researcher who is PRINCIPAL_INVESTIGATOR |
| Constraint | PROJECT | C.PROJECT.Project.Team.maxCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | PROJECT | C.PROJECT.Project.Team.minCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | FUNDING | C.FUNDING.Funding.CreateDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | FUNDING | C.FUNDING.Funding.Description.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | FUNDING | C.FUNDING.Funding.Description.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | FUNDING | C.FUNDING.Funding.Identifiers.minCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | FUNDING | C.FUNDING.Funding.FromDate.maxDate | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | FUNDING | C.FUNDING.Funding.LastModificationDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | FUNDING | C.FUNDING.Funding.MetadataAccessLevel.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | FUNDING | C.FUNDING.Funding.MetadataAccessLevel.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | FUNDING | C.FUNDING.Funding.MetadataLicense.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | FUNDING | C.FUNDING.Funding.MetadataLicense.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | FUNDING | C.FUNDING.Funding.Name.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | FUNDING | C.FUNDING.Funding.ProjectInvolvement.custom | The Funding should linking either Project, or paid job position (Employment) or it might represent scholarship for Education, i.e. it should linking Education |
| Constraint | FUNDING | C.FUNDING.Funding.ProjectInvolvement.minCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | FUNDING | C.FUNDING.Funding.ProjectInvolvement.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | FUNDING | C.FUNDING.Funding.ResearchAreas.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | FUNDING | C.FUNDING.Funding.ToDate.maxDate | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | OUTPUT | C.OUTPUT.Document.Contributors.custom | At least one managed person should be linked with Document, with the exception if it is source for other document (for instance proceedings, edited monograph, etc.) |
| Constraint | OUTPUT | C.OUTPUT.Document.Contributors.minCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | OUTPUT | C.OUTPUT.Document.CreateDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | OUTPUT | C.OUTPUT.Document.Description.minLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | OUTPUT | C.OUTPUT.Document.Description.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | OUTPUT | C.OUTPUT.Document.Identifiers.minCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | OUTPUT | C.OUTPUT.Document.Identifiers.unique | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | OUTPUT | C.OUTPUT.Document.LastModificationDate.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | OUTPUT | C.OUTPUT.Document.MetadataAccessLevel.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | OUTPUT | C.OUTPUT.Document.MetadataAccessLevel.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | OUTPUT | C.OUTPUT.Document.MetadataLicense.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | OUTPUT | C.OUTPUT.Document.MetadataLicense.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | OUTPUT | C.OUTPUT.Document.ResearchAreas.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | OUTPUT | C.OUTPUT.Document.Title.minCardinality | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | ACTIVITY | C.ACTIVITY.Involvement.ResearchAreas.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | ACTIVITY | C.ACTIVITY.PersonContribution.ResearchAreas.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | ACTIVITY | C.ACTIVITY.PersonDocumentContribution.IsCorrespondingContributor.custom | Can be true only if contributionType is in [AUTHOR, PRESENTER, EDITOR]. |
| Constraint | ACTIVITY | C.ACTIVITY.PersonDocumentContribution.IsMainContributor.custom | Can be true only if contributionType is in [AUTHOR, PRESENTER, EDITOR, ADVISOR, ARGUER, BOARD_MEMBER]. |
| Constraint | ACTIVITY | C.ACTIVITY.PersonDocumentContribution.Person.custom | A document can't be linked with Person if documentDate is not after Person birthDate.<br><br>In the case of Thesis all dates should be after birthDate (thesisDefenceDate, topicAcceptanceDate, and documentDate). |
| Constraint | ACTIVITY | C.ACTIVITY.PersonEventContribution.Case.custom | Only can be there is PersonEventContribution is linked with an OtherEvent instance with type=TRIAL |
| Constraint | ACTIVITY | C.ACTIVITY.PersonEventContribution.LabHoursPerWeek.custom | Only can be there if PersonEventContribution is linked with a Course |
| Constraint | ACTIVITY | C.ACTIVITY.PersonEventContribution.LectureHoursPerWeek.custom | Only can be there if PersonEventContribution is linked with a Course |
| Constraint | ACTIVITY | C.ACTIVITY.PersonEventContribution.LocationJurisdiction.custom | Only can be there is PersonEventContribution is linked with an OtherEvent instance with type=TRIAL |
| Constraint | ACTIVITY | C.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment.custom | Only can be there if PersonEventContribution is linked with a Conference, and contributionType is a REVIEWER |
| Constraint | ACTIVITY | C.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment.minValue | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | ACTIVITY | C.ACTIVITY.PersonEventContribution.OtherContactHoursPerWeek.custom | Only can be there if PersonEventContribution is linked with a Course |
| Constraint | ACTIVITY | C.ACTIVITY.PersonEventContribution.TutorialHoursPerWeek.custom | Only can be there if PersonEventContribution is linked with a Course |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.Contact.ContactEmail.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.Country.Code.maxLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.Country.Code.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.Currency.Code.maxLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.Currency.Code.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.Currency.Code.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.Currency.Symbol.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue.custom | At least one of those fields should be present in concrete subclass (DocumentIndicator for instance) depending on linked Indicator.contentType |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.EntityIndicator.Subclass.custom | Subclass type has to be aligned with entityIndicator.indicator.applicableTypes |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.FlexibleDate.Day.custom | Values 31, 30, 29 should be checked whether are available for the certain month |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.FlexibleDate.TextYear.custom | For any  date should be defined at least year, or if there is no year, then textual representation should be there (e.g. in print, indefinately, 3rd century, etc.) |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.FlexibleDate.TextYear.presence | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.GeoLocation.Latitude.maxValue | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.GeoLocation.Latitude.minValue | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.GeoLocation.Longitude.maxValue | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.GeoLocation.Longitude.minValue | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.Identifier.RegularExpression.custom | It should be a valid regular expression |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.Language.LanguageCode.maxLength | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.Language.LanguageCode.pattern | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.Language.LanguageCode.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.LanguageTag.LanguageTag.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.MonetaryAmount.Amount.maxValue | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.MonetaryAmount.Amount.minValue | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset.minValue | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset.minValue | No distinct legacy message segment matched; message generated from constraint metadata. |
| Constraint | SHARED_COMPONENTS | C.SHARED_COMPONENTS.ResearchArea.Name.vocabulary | No distinct legacy message segment matched; message generated from constraint metadata. |
| Governance requirement | — | GR.PTCRIS_F1_01DSTRUCT.doi_format_verification | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_doi_allocation | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_F1_A1.resolvable_doi | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_F1_01DSTRUCT.pid_format_verification | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_pid_allocation | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_FsF_F2_01M.metric_requirement | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_FsF_R1_1_01M.metric_requirement | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_FsF_A1_01M.metric_requirement | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_F1_01DLINEAGE.metric_requirement | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_F1_01DSTRUCT.raid_format_verification | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_raid_allocation | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_F1_A1.resolvable_raid | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_F1_01DCONSIST.semantic_iri_url_validation | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_F1_01DSTRUCT.project_with_coordinating_organization_but_no_other_participants | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_F1_01DCONSIST.sum_of_linked_fundings_amounts | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_F1_A1.resolvable_pid | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_F1_01DACURR.metric_requirement | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_F1_01DSTRUCT.metric_requirement | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_DQ_F1_01IDUNIQ.metric_requirement | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_F1_01DSTRUCT.handle_format_verification | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_handle_allocation | Verify against the authoritative PTCRIS governance source. |
| Governance requirement | — | GR.PTCRIS_F1_A1.resolvable_handle | Verify against the authoritative PTCRIS governance source. |
| Implementation binding | PERSON | BIND.PT_MASTER.VT.PERSON.Involvement.FundingPartsFunding | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | PERSON | BIND.PT_MASTER.VT.PERSON.Involvement.ToDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | PERSON | BIND.PT_MASTER.VT.PERSON.Prize.ToDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | ORGANISATION_UNIT | BIND.PT_MASTER.VT.ORGANISATION_UNIT.OrganisationUnit.RorIsni | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | PROJECT | BIND.PT_MASTER.VT.PROJECT.Project.Costs | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | PROJECT | BIND.PT_MASTER.VT.PROJECT.Project.Identifiers | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | PROJECT | BIND.PT_MASTER.VT.PROJECT.Project.Fundings | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | PROJECT | BIND.PT_MASTER.VT.PROJECT.Project.Organisations | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | PROJECT | BIND.PT_MASTER.VT.PROJECT.Project.ResearchAreas | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | PROJECT | BIND.PT_MASTER.VT.PROJECT.Project.Team | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | PROJECT | BIND.PT_MASTER.VT.PROJECT.Project.ToDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | FUNDING | BIND.PT_MASTER.VT.FUNDING.Funding.DateAwarded | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | FUNDING | BIND.PT_MASTER.VT.FUNDING.Funding.DateSubmitted | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | FUNDING | BIND.PT_MASTER.VT.FUNDING.Funding.Identifiers | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | FUNDING | BIND.PT_MASTER.VT.FUNDING.Funding.FromDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | FUNDING | BIND.PT_MASTER.VT.FUNDING.Funding.ProjectInvolvement | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | FUNDING | BIND.PT_MASTER.VT.FUNDING.Funding.ProjectReferenceIdGrantAgreementId | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | FUNDING | BIND.PT_MASTER.VT.FUNDING.Funding.ToDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | OUTPUT | BIND.PT_MASTER.VT.OUTPUT.Document.Contributors | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | OUTPUT | BIND.PT_MASTER.VT.OUTPUT.Document.Identifiers | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | OUTPUT | BIND.PT_MASTER.VT.OUTPUT.IntellectualProperty.DateEndTerm | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | OUTPUT | BIND.PT_MASTER.VT.OUTPUT.IntellectualProperty.DateFilingPriority | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | OUTPUT | BIND.PT_MASTER.VT.OUTPUT.IntellectualProperty.DateRequested | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | OUTPUT | BIND.PT_MASTER.VT.OUTPUT.PublicationSeriesPublisher.ToDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | OUTPUT | BIND.PT_MASTER.VT.OUTPUT.Thesis.ThesisDefenceDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | ACTIVITY | BIND.PT_MASTER.VT.ACTIVITY.Involvement.FromDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | ACTIVITY | BIND.PT_MASTER.VT.ACTIVITY.Involvement.ToDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | ACTIVITY | BIND.PT_MASTER.VT.ACTIVITY.PersonContribution.FromDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | ACTIVITY | BIND.PT_MASTER.VT.ACTIVITY.PersonContribution.ToDate | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | ACTIVITY | BIND.PT_MASTER.VT.ACTIVITY.PersonDocumentContribution.IsCorrespondingContributor | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | ACTIVITY | BIND.PT_MASTER.VT.ACTIVITY.PersonDocumentContribution.IsMainContributor | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | ACTIVITY | BIND.PT_MASTER.VT.ACTIVITY.PersonDocumentContribution.Person | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | ACTIVITY | BIND.PT_MASTER.VT.ACTIVITY.PersonEventContribution.Case | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | ACTIVITY | BIND.PT_MASTER.VT.ACTIVITY.PersonEventContribution.LabHoursPerWeek | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | ACTIVITY | BIND.PT_MASTER.VT.ACTIVITY.PersonEventContribution.LectureHoursPerWeek | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | ACTIVITY | BIND.PT_MASTER.VT.ACTIVITY.PersonEventContribution.LocationJurisdiction | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | ACTIVITY | BIND.PT_MASTER.VT.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | ACTIVITY | BIND.PT_MASTER.VT.ACTIVITY.PersonEventContribution.OtherContactHoursPerWeek | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | ACTIVITY | BIND.PT_MASTER.VT.ACTIVITY.PersonEventContribution.TutorialHoursPerWeek | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | SHARED_COMPONENTS | BIND.PT_MASTER.VT.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | SHARED_COMPONENTS | BIND.PT_MASTER.VT.SHARED_COMPONENTS.EntityIndicator.Subclass | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
| Implementation binding | SHARED_COMPONENTS | BIND.PT_MASTER.VT.SHARED_COMPONENTS.FlexibleDate.TextYear | Composite/cross-field target requires an explicit runtime binding before exact JSON generation. |
