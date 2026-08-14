# Governance traceability — PTCRIS-DATAGOV-1.0.0

| Domain | Rule | Validation target | Governance requirements |
|---|---|---|---|
| ACTIVITY | RULE.ACTIVITY.Involvement.FromDate | VT.ACTIVITY.Involvement.FromDate |  |
| ACTIVITY | RULE.ACTIVITY.Involvement.ResearchAreas | VT.ACTIVITY.Involvement.ResearchAreas |  |
| ACTIVITY | RULE.ACTIVITY.Involvement.ToDate | VT.ACTIVITY.Involvement.ToDate |  |
| ACTIVITY | RULE.ACTIVITY.PersonContribution.FromDate | VT.ACTIVITY.PersonContribution.FromDate |  |
| ACTIVITY | RULE.ACTIVITY.PersonContribution.ResearchAreas | VT.ACTIVITY.PersonContribution.ResearchAreas |  |
| ACTIVITY | RULE.ACTIVITY.PersonContribution.ToDate | VT.ACTIVITY.PersonContribution.ToDate |  |
| ACTIVITY | RULE.ACTIVITY.PersonDocumentContribution.IsCorrespondingContributor | VT.ACTIVITY.PersonDocumentContribution.IsCorrespondingContributor |  |
| ACTIVITY | RULE.ACTIVITY.PersonDocumentContribution.IsMainContributor | VT.ACTIVITY.PersonDocumentContribution.IsMainContributor |  |
| ACTIVITY | RULE.ACTIVITY.PersonDocumentContribution.Person | VT.ACTIVITY.PersonDocumentContribution.Person |  |
| ACTIVITY | RULE.ACTIVITY.PersonEventContribution.Case | VT.ACTIVITY.PersonEventContribution.Case |  |
| ACTIVITY | RULE.ACTIVITY.PersonEventContribution.LabHoursPerWeek | VT.ACTIVITY.PersonEventContribution.LabHoursPerWeek |  |
| ACTIVITY | RULE.ACTIVITY.PersonEventContribution.LectureHoursPerWeek | VT.ACTIVITY.PersonEventContribution.LectureHoursPerWeek |  |
| ACTIVITY | RULE.ACTIVITY.PersonEventContribution.LocationJurisdiction | VT.ACTIVITY.PersonEventContribution.LocationJurisdiction |  |
| ACTIVITY | RULE.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment | VT.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment |  |
| ACTIVITY | RULE.ACTIVITY.PersonEventContribution.OtherContactHoursPerWeek | VT.ACTIVITY.PersonEventContribution.OtherContactHoursPerWeek |  |
| ACTIVITY | RULE.ACTIVITY.PersonEventContribution.TutorialHoursPerWeek | VT.ACTIVITY.PersonEventContribution.TutorialHoursPerWeek |  |
| FUNDING | RULE.FUNDING.Funding.Amount | VT.FUNDING.Funding.Amount |  |
| FUNDING | RULE.FUNDING.Funding.CreateDate | VT.FUNDING.Funding.CreateDate | GR.PTCRIS_F1_01DLINEAGE.metric_requirement |
| FUNDING | RULE.FUNDING.Funding.DateAwarded | VT.FUNDING.Funding.DateAwarded | GR.PTCRIS_F1_01DCURREN.award_year_required_verification |
| FUNDING | RULE.FUNDING.Funding.DateSubmitted | VT.FUNDING.Funding.DateSubmitted |  |
| FUNDING | RULE.FUNDING.Funding.Description | VT.FUNDING.Funding.Description | GR.PTCRIS_FsF_F2_01M.metric_requirement |
| FUNDING | RULE.FUNDING.Funding.Doi | VT.FUNDING.Funding.Doi | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_doi_allocation, GR.PTCRIS_F1_01DSTRUCT.doi_format_verification, GR.PTCRIS_F1_A1.resolvable_doi |
| FUNDING | RULE.FUNDING.Funding.FromDate | VT.FUNDING.Funding.FromDate | GR.PTCRIS_F1_01DCURREN.project_funding_with_suspicious_start_date |
| FUNDING | RULE.FUNDING.Funding.Identifiers | VT.FUNDING.Funding.Identifiers |  |
| FUNDING | RULE.FUNDING.Funding.LastModificationDate | VT.FUNDING.Funding.LastModificationDate | GR.PTCRIS_F1_01DLINEAGE.metric_requirement |
| FUNDING | RULE.FUNDING.Funding.MetadataAccessLevel | VT.FUNDING.Funding.MetadataAccessLevel | GR.PTCRIS_FsF_A1_01M.metric_requirement |
| FUNDING | RULE.FUNDING.Funding.MetadataLicense | VT.FUNDING.Funding.MetadataLicense | GR.PTCRIS_FsF_R1_1_01M.metric_requirement |
| FUNDING | RULE.FUNDING.Funding.Name | VT.FUNDING.Funding.Name | GR.PTCRIS_F1_01DSTRUCT.format_validation_for_award_title_name |
| FUNDING | RULE.FUNDING.Funding.ProjectInvolvement | VT.FUNDING.Funding.ProjectInvolvement |  |
| FUNDING | RULE.FUNDING.Funding.ProjectReferenceIdGrantAgreementId | VT.FUNDING.Funding.ProjectReferenceIdGrantAgreementId | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_pid_allocation, GR.PTCRIS_F1_01DSTRUCT.pid_format_verification |
| FUNDING | RULE.FUNDING.Funding.ResearchAreas | VT.FUNDING.Funding.ResearchAreas |  |
| FUNDING | RULE.FUNDING.Funding.ToDate | VT.FUNDING.Funding.ToDate | GR.PTCRIS_F1_01DCURREN.project_funding_with_suspected_end_date |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.Active | VT.ORGANISATION_UNIT.OrganisationUnit.Active |  |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.CreateDate | VT.ORGANISATION_UNIT.OrganisationUnit.CreateDate | GR.PTCRIS_F1_01DLINEAGE.metric_requirement |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.DateDissolved | VT.ORGANISATION_UNIT.OrganisationUnit.DateDissolved |  |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.DateEstablished | VT.ORGANISATION_UNIT.OrganisationUnit.DateEstablished |  |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.Description | VT.ORGANISATION_UNIT.OrganisationUnit.Description | GR.PTCRIS_FsF_F2_01M.metric_requirement |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.Fundref | VT.ORGANISATION_UNIT.OrganisationUnit.Fundref |  |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.Grid | VT.ORGANISATION_UNIT.OrganisationUnit.Grid |  |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.Isni | VT.ORGANISATION_UNIT.OrganisationUnit.Isni |  |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.LastModificationDate | VT.ORGANISATION_UNIT.OrganisationUnit.LastModificationDate | GR.PTCRIS_F1_01DLINEAGE.metric_requirement |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel | VT.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel | GR.PTCRIS_FsF_A1_01M.metric_requirement |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense | VT.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense | GR.PTCRIS_FsF_R1_1_01M.metric_requirement |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.Name | VT.ORGANISATION_UNIT.OrganisationUnit.Name |  |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId | VT.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId |  |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.PostalAddress | VT.ORGANISATION_UNIT.OrganisationUnit.PostalAddress |  |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.Ringgold | VT.ORGANISATION_UNIT.OrganisationUnit.Ringgold |  |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.Ror | VT.ORGANISATION_UNIT.OrganisationUnit.Ror |  |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.RorIsni | VT.ORGANISATION_UNIT.OrganisationUnit.RorIsni |  |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid | VT.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid |  |
| ORGANISATION_UNIT | RULE.ORGANISATION_UNIT.OrganisationUnit.Sector | VT.ORGANISATION_UNIT.OrganisationUnit.Sector |  |
| OUTPUT | RULE.OUTPUT.Document.Contributors | VT.OUTPUT.Document.Contributors |  |
| OUTPUT | RULE.OUTPUT.Document.CreateDate | VT.OUTPUT.Document.CreateDate | GR.PTCRIS_F1_01DLINEAGE.metric_requirement |
| OUTPUT | RULE.OUTPUT.Document.Description | VT.OUTPUT.Document.Description | GR.PTCRIS_FsF_F2_01M.metric_requirement |
| OUTPUT | RULE.OUTPUT.Document.DocumentDate | VT.OUTPUT.Document.DocumentDate |  |
| OUTPUT | RULE.OUTPUT.Document.Doi | VT.OUTPUT.Document.Doi | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_doi_allocation, GR.PTCRIS_F1_01DSTRUCT.doi_format_verification, GR.PTCRIS_F1_A1.resolvable_doi |
| OUTPUT | RULE.OUTPUT.Document.Handle | VT.OUTPUT.Document.Handle | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_handle_allocation, GR.PTCRIS_F1_01DSTRUCT.handle_format_verification, GR.PTCRIS_F1_A1.resolvable_handle |
| OUTPUT | RULE.OUTPUT.Document.Identifiers | VT.OUTPUT.Document.Identifiers |  |
| OUTPUT | RULE.OUTPUT.Document.LastModificationDate | VT.OUTPUT.Document.LastModificationDate | GR.PTCRIS_F1_01DLINEAGE.metric_requirement |
| OUTPUT | RULE.OUTPUT.Document.MetadataAccessLevel | VT.OUTPUT.Document.MetadataAccessLevel | GR.PTCRIS_FsF_A1_01M.metric_requirement |
| OUTPUT | RULE.OUTPUT.Document.MetadataLicense | VT.OUTPUT.Document.MetadataLicense | GR.PTCRIS_FsF_R1_1_01M.metric_requirement |
| OUTPUT | RULE.OUTPUT.Document.OpenAccess | VT.OUTPUT.Document.OpenAccess |  |
| OUTPUT | RULE.OUTPUT.Document.ResearchAreas | VT.OUTPUT.Document.ResearchAreas |  |
| OUTPUT | RULE.OUTPUT.Document.Title | VT.OUTPUT.Document.Title |  |
| OUTPUT | RULE.OUTPUT.IntellectualProperty.DateEndTerm | VT.OUTPUT.IntellectualProperty.DateEndTerm |  |
| OUTPUT | RULE.OUTPUT.IntellectualProperty.DateFilingPriority | VT.OUTPUT.IntellectualProperty.DateFilingPriority |  |
| OUTPUT | RULE.OUTPUT.IntellectualProperty.DateRequested | VT.OUTPUT.IntellectualProperty.DateRequested |  |
| OUTPUT | RULE.OUTPUT.PublicationSeriesPublisher.FromDate | VT.OUTPUT.PublicationSeriesPublisher.FromDate |  |
| OUTPUT | RULE.OUTPUT.PublicationSeriesPublisher.ToDate | VT.OUTPUT.PublicationSeriesPublisher.ToDate |  |
| OUTPUT | RULE.OUTPUT.PublicationUnit.NumberOfPages | VT.OUTPUT.PublicationUnit.NumberOfPages |  |
| OUTPUT | RULE.OUTPUT.PublicationUnitPart.NumberOfPages | VT.OUTPUT.PublicationUnitPart.NumberOfPages |  |
| OUTPUT | RULE.OUTPUT.Thesis.ThesisDefenceDate | VT.OUTPUT.Thesis.ThesisDefenceDate |  |
| OUTPUT | RULE.OUTPUT.Thesis.TopicAcceptanceDate | VT.OUTPUT.Thesis.TopicAcceptanceDate |  |
| OUTPUT | RULE.OUTPUT.ThesisPhysicalDescription.NumberOfAppendices | VT.OUTPUT.ThesisPhysicalDescription.NumberOfAppendices |  |
| OUTPUT | RULE.OUTPUT.ThesisPhysicalDescription.NumberOfChapters | VT.OUTPUT.ThesisPhysicalDescription.NumberOfChapters |  |
| OUTPUT | RULE.OUTPUT.ThesisPhysicalDescription.NumberOfGraphs | VT.OUTPUT.ThesisPhysicalDescription.NumberOfGraphs |  |
| OUTPUT | RULE.OUTPUT.ThesisPhysicalDescription.NumberOfIlustrations | VT.OUTPUT.ThesisPhysicalDescription.NumberOfIlustrations |  |
| OUTPUT | RULE.OUTPUT.ThesisPhysicalDescription.NumberOfPages | VT.OUTPUT.ThesisPhysicalDescription.NumberOfPages |  |
| OUTPUT | RULE.OUTPUT.ThesisPhysicalDescription.NumberOfReferences | VT.OUTPUT.ThesisPhysicalDescription.NumberOfReferences |  |
| OUTPUT | RULE.OUTPUT.ThesisPhysicalDescription.NumberOfTables | VT.OUTPUT.ThesisPhysicalDescription.NumberOfTables |  |
| PERSON | RULE.PERSON.Education.DegreeType | VT.PERSON.Education.DegreeType |  |
| PERSON | RULE.PERSON.Education.EducationStatus | VT.PERSON.Education.EducationStatus |  |
| PERSON | RULE.PERSON.Employment.EmploymentPositionHierarchy | VT.PERSON.Employment.EmploymentPositionHierarchy | GR.PTCRIS_F1_01DSEMANT.type_professional_path_classification_validation |
| PERSON | RULE.PERSON.ExpertiseOrSkill.ResearchAreas | VT.PERSON.ExpertiseOrSkill.ResearchAreas |  |
| PERSON | RULE.PERSON.Involvement.FromDate | VT.PERSON.Involvement.FromDate | GR.PTCRIS_F1_01DSTRUCT.validation_of_the_format_of_the_start_date_of_the_professional_career |
| PERSON | RULE.PERSON.Involvement.FundingPartsFunding | VT.PERSON.Involvement.FundingPartsFunding |  |
| PERSON | RULE.PERSON.Involvement.InvolvementType | VT.PERSON.Involvement.InvolvementType |  |
| PERSON | RULE.PERSON.Involvement.ToDate | VT.PERSON.Involvement.ToDate |  |
| PERSON | RULE.PERSON.LanguageKnowledge.AcademicReview | VT.PERSON.LanguageKnowledge.AcademicReview |  |
| PERSON | RULE.PERSON.LanguageKnowledge.AcademicWriting | VT.PERSON.LanguageKnowledge.AcademicWriting |  |
| PERSON | RULE.PERSON.LanguageKnowledge.Listening | VT.PERSON.LanguageKnowledge.Listening |  |
| PERSON | RULE.PERSON.LanguageKnowledge.Overall | VT.PERSON.LanguageKnowledge.Overall |  |
| PERSON | RULE.PERSON.LanguageKnowledge.Reading | VT.PERSON.LanguageKnowledge.Reading |  |
| PERSON | RULE.PERSON.LanguageKnowledge.Speaking | VT.PERSON.LanguageKnowledge.Speaking |  |
| PERSON | RULE.PERSON.LanguageKnowledge.Writing | VT.PERSON.LanguageKnowledge.Writing |  |
| PERSON | RULE.PERSON.Membership.MembershipType | VT.PERSON.Membership.MembershipType |  |
| PERSON | RULE.PERSON.Person.AuthenticusId | VT.PERSON.Person.AuthenticusId | GR.PTCRIS_F1_01DACURR.metric_requirement, GR.PTCRIS_F1_01DSTRUCT.metric_requirement |
| PERSON | RULE.PERSON.Person.Biography | VT.PERSON.Person.Biography | GR.PTCRIS_FsF_F2_01M.metric_requirement |
| PERSON | RULE.PERSON.Person.CreateDate | VT.PERSON.Person.CreateDate | GR.PTCRIS_F1_01DLINEAGE.metric_requirement |
| PERSON | RULE.PERSON.Person.Involvements | VT.PERSON.Person.Involvements | GR.PTCRIS_F1_01DCURREN.mandatory_start_date_of_professional_career |
| PERSON | RULE.PERSON.Person.LastModificationDate | VT.PERSON.Person.LastModificationDate | GR.PTCRIS_F1_01DLINEAGE.metric_requirement |
| PERSON | RULE.PERSON.Person.LattesId | VT.PERSON.Person.LattesId | GR.PTCRIS_F1_01DACURR.metric_requirement, GR.PTCRIS_F1_01DSTRUCT.metric_requirement |
| PERSON | RULE.PERSON.Person.MetadataAccessLevel | VT.PERSON.Person.MetadataAccessLevel | GR.PTCRIS_FsF_A1_01M.metric_requirement |
| PERSON | RULE.PERSON.Person.MetadataLicense | VT.PERSON.Person.MetadataLicense | GR.PTCRIS_FsF_R1_1_01M.metric_requirement |
| PERSON | RULE.PERSON.Person.Name | VT.PERSON.Person.Name | GR.PTCRIS_F1_01DACURR.full_name_presence_and_length_validation |
| PERSON | RULE.PERSON.Person.NationalIdCienciaId | VT.PERSON.Person.NationalIdCienciaId | GR.PTCRIS_DQ_F1_01IDUNIQ.metric_requirement, GR.PTCRIS_F1_01DACURR.global_uniqueness_of_science_id_allocation, GR.PTCRIS_F1_01DSTRUCT.metric_requirement |
| PERSON | RULE.PERSON.Person.OpenAlexId | VT.PERSON.Person.OpenAlexId | GR.PTCRIS_F1_01DACURR.metric_requirement, GR.PTCRIS_F1_01DSTRUCT.metric_requirement |
| PERSON | RULE.PERSON.Person.Orcid | VT.PERSON.Person.Orcid | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_orcid_allocation, GR.PTCRIS_F1_01DSTRUCT.open_researcher_and_contributor_id_orcid_format_verification, GR.PTCRIS_F1_A1.resolvable_pid |
| PERSON | RULE.PERSON.Person.ScholarId | VT.PERSON.Person.ScholarId | GR.PTCRIS_F1_01DACURR.metric_requirement, GR.PTCRIS_F1_01DSTRUCT.metric_requirement |
| PERSON | RULE.PERSON.Person.ScopusAuthorId | VT.PERSON.Person.ScopusAuthorId | GR.PTCRIS_F1_01DACURR.metric_requirement, GR.PTCRIS_F1_01DSTRUCT.scopus_author_id_format_validation |
| PERSON | RULE.PERSON.Person.WebOfScienceResearcherId | VT.PERSON.Person.WebOfScienceResearcherId | GR.PTCRIS_F1_01DACURR.metric_requirement, GR.PTCRIS_F1_01DSTRUCT.web_of_science_researcher_id_format_validation |
| PERSON | RULE.PERSON.PersonName.Firstname | VT.PERSON.PersonName.Firstname |  |
| PERSON | RULE.PERSON.PersonName.Lastname | VT.PERSON.PersonName.Lastname | GR.PTCRIS_F1_01DACURR.full_name_presence_and_length_validation, GR.PTCRIS_F1_01DSTRUCT.standardized_citation_name_format_verification |
| PERSON | RULE.PERSON.PersonName.OtherName | VT.PERSON.PersonName.OtherName |  |
| PERSON | RULE.PERSON.PersonName.PersonNameType | VT.PERSON.PersonName.PersonNameType |  |
| PERSON | RULE.PERSON.PersonalInfo.BirthDate | VT.PERSON.PersonalInfo.BirthDate | GR.PTCRIS_F1_01DCONSIST.non_existent_or_futuristic_birth_date_restriction, GR.PTCRIS_F1_01DCURREN.minor_underage_researcher_validation |
| PERSON | RULE.PERSON.PersonalInfo.Sex | VT.PERSON.PersonalInfo.Sex | GR.PTCRIS_F1_01DSEMANT.gender_classification_conformity |
| PERSON | RULE.PERSON.Prize.EffectiveDate | VT.PERSON.Prize.EffectiveDate |  |
| PERSON | RULE.PERSON.Prize.ResearchAreas | VT.PERSON.Prize.ResearchAreas |  |
| PERSON | RULE.PERSON.Prize.ToDate | VT.PERSON.Prize.ToDate |  |
| PERSON | RULE.PERSON.Prize.Type | VT.PERSON.Prize.Type |  |
| PROJECT | RULE.PROJECT.Project.Costs | VT.PROJECT.Project.Costs | GR.PTCRIS_F1_01DCONSIST.sum_of_linked_fundings_amounts |
| PROJECT | RULE.PROJECT.Project.CreateDate | VT.PROJECT.Project.CreateDate | GR.PTCRIS_F1_01DLINEAGE.metric_requirement |
| PROJECT | RULE.PROJECT.Project.Description | VT.PROJECT.Project.Description | GR.PTCRIS_FsF_F2_01M.metric_requirement |
| PROJECT | RULE.PROJECT.Project.Doi | VT.PROJECT.Project.Doi | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_doi_allocation, GR.PTCRIS_F1_01DSTRUCT.doi_format_verification, GR.PTCRIS_F1_A1.resolvable_doi |
| PROJECT | RULE.PROJECT.Project.FromDate | VT.PROJECT.Project.FromDate | GR.PTCRIS_F1_01DCURREN.mandatory_project_boundary_dates |
| PROJECT | RULE.PROJECT.Project.Fundings | VT.PROJECT.Project.Fundings | GR.PTCRIS_F1_01DCONSIST.different_funding_ids_in_project_and_funding |
| PROJECT | RULE.PROJECT.Project.Identifiers | VT.PROJECT.Project.Identifiers | GR.PTCRIS_F1_01DACURR.project_without_at_least_one_identifier |
| PROJECT | RULE.PROJECT.Project.LastModificationDate | VT.PROJECT.Project.LastModificationDate | GR.PTCRIS_F1_01DLINEAGE.metric_requirement |
| PROJECT | RULE.PROJECT.Project.MetadataAccessLevel | VT.PROJECT.Project.MetadataAccessLevel | GR.PTCRIS_FsF_A1_01M.metric_requirement |
| PROJECT | RULE.PROJECT.Project.MetadataLicense | VT.PROJECT.Project.MetadataLicense | GR.PTCRIS_FsF_R1_1_01M.metric_requirement |
| PROJECT | RULE.PROJECT.Project.Name | VT.PROJECT.Project.Name | GR.PTCRIS_F1_01DCONSIST.project_title_presence_requirement |
| PROJECT | RULE.PROJECT.Project.NationalIdProjectReference | VT.PROJECT.Project.NationalIdProjectReference | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_pid_allocation, GR.PTCRIS_F1_01DSTRUCT.pid_format_verification |
| PROJECT | RULE.PROJECT.Project.Organisations | VT.PROJECT.Project.Organisations | GR.PTCRIS_F1_01DCONSIST.sum_of_organizations_funding_greater_than_project_total, GR.PTCRIS_F1_01DSTRUCT.project_with_associated_organizations_but_no_coordinator, GR.PTCRIS_F1_01DSTRUCT.project_with_coordinating_organization_but_no_other_participants |
| PROJECT | RULE.PROJECT.Project.Raid | VT.PROJECT.Project.Raid | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_raid_allocation, GR.PTCRIS_F1_01DSTRUCT.raid_format_verification, GR.PTCRIS_F1_A1.resolvable_raid |
| PROJECT | RULE.PROJECT.Project.ResearchAreas | VT.PROJECT.Project.ResearchAreas | GR.PTCRIS_F1_01DCONSIST.semantic_iri_url_validation |
| PROJECT | RULE.PROJECT.Project.Team | VT.PROJECT.Project.Team | GR.PTCRIS_F1_01DSTRUCT.project_with_team_but_no_principal_investigator |
| PROJECT | RULE.PROJECT.Project.ToDate | VT.PROJECT.Project.ToDate | GR.PTCRIS_F1_01DCURREN.mandatory_project_boundary_dates |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.Contact.ContactEmail | VT.SHARED_COMPONENTS.Contact.ContactEmail |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.Contact.FaxNumber | VT.SHARED_COMPONENTS.Contact.FaxNumber |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.Contact.MobilePhoneNumber | VT.SHARED_COMPONENTS.Contact.MobilePhoneNumber |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.Contact.PhoneNumber | VT.SHARED_COMPONENTS.Contact.PhoneNumber |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.Country.Code | VT.SHARED_COMPONENTS.Country.Code | GR.PTCRIS_F1_01DSEMANT.standardized_geopolitical_country_coding |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.Currency.Code | VT.SHARED_COMPONENTS.Currency.Code |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.Currency.Symbol | VT.SHARED_COMPONENTS.Currency.Symbol |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue | VT.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.EntityIndicator.Subclass | VT.SHARED_COMPONENTS.EntityIndicator.Subclass |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.FlexibleDate.Day | VT.SHARED_COMPONENTS.FlexibleDate.Day |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.FlexibleDate.Month | VT.SHARED_COMPONENTS.FlexibleDate.Month |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.FlexibleDate.TextYear | VT.SHARED_COMPONENTS.FlexibleDate.TextYear |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.FlexibleDate.Year | VT.SHARED_COMPONENTS.FlexibleDate.Year |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.GeoLocation.Address | VT.SHARED_COMPONENTS.GeoLocation.Address |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.GeoLocation.Latitude | VT.SHARED_COMPONENTS.GeoLocation.Latitude |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.GeoLocation.Longitude | VT.SHARED_COMPONENTS.GeoLocation.Longitude |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.Identifier.RegularExpression | VT.SHARED_COMPONENTS.Identifier.RegularExpression |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.Language.LanguageCode | VT.SHARED_COMPONENTS.Language.LanguageCode |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.LanguageTag.LanguageTag | VT.SHARED_COMPONENTS.LanguageTag.LanguageTag |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.MonetaryAmount.Amount | VT.SHARED_COMPONENTS.MonetaryAmount.Amount | GR.PTCRIS_F1_01DCONSIST.negative_or_zero_funding_anomaly_detection |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.ProfilePhotoOrLogo.Height | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.Height |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.ProfilePhotoOrLogo.Width | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.Width |  |
| SHARED_COMPONENTS | RULE.SHARED_COMPONENTS.ResearchArea.Name | VT.SHARED_COMPONENTS.ResearchArea.Name |  |
