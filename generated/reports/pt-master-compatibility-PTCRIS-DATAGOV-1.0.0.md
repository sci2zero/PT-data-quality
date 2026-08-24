# PT Master runtime compatibility — PTCRIS-DATAGOV-1.0.0

This report compares the generated runtime projection with the deployed legacy JSON fixture.
Message/title text is intentionally excluded because RSR v2 consolidates and localizes messages differently.

- Legacy remarks: **162**
- Generated remarks: **445**
- Preserved keys with unchanged runtime semantics: **0**
- Preserved keys with changed runtime semantics: **115**
- Removed legacy keys: **47**
- Added keys: **330**

| Runtime key | Status | Changed fields |
|---|---|---|
| activityResearchAreasMissing | CHANGED | severity, blocking, points |
| activityStartDateTooFarInFuture | CHANGED | points, constraints |
| biographyMissing | CHANGED | severity, blocking, points |
| birthDateBefore | CHANGED | points, constraints |
| birthDateMissing | CHANGED | points |
| caseOnlyForTrial | CHANGED | points, constraints |
| contactEmailTooLong | CHANGED | points |
| contributorsMissing | CHANGED | severity, blocking, points |
| countryCodeMissing | CHANGED | severity, blocking, points |
| dateEndTermBefore | CHANGED | points, constraints |
| dateEndTermMissing | CHANGED | points |
| dateFilingPriorityBefore | CHANGED | points, constraints |
| dateFilingPriorityMissing | CHANGED | points |
| dateRequestedBefore | CHANGED | points, constraints |
| dateRequestedMissing | CHANGED | points |
| defenceTooFarInFuture | CHANGED | points, constraints |
| descriptionMissing | CHANGED | severity, blocking, points |
| documentDateBefore | CHANGED | points, constraints |
| documentDateMissing | CHANGED | severity, blocking, points |
| documentDateTooFarInFuture | CHANGED | points, constraints |
| doiNotResolvable | CHANGED | points, constraints |
| doiTooLong | CHANGED | points |
| doiTooShort | CHANGED | points |
| duplicateAuthenticusId | CHANGED | points |
| duplicateCountryCode | CHANGED | points |
| duplicateDoi | CHANGED | points |
| duplicateGoogleScholarId | CHANGED | points |
| duplicateGrid | CHANGED | points |
| duplicateHandle | CHANGED | points |
| duplicateIsni | CHANGED | points |
| duplicateLanguageTag | CHANGED | points |
| duplicateOpenAlexId | CHANGED | points |
| duplicateOrcid | CHANGED | points |
| duplicateRinggold | CHANGED | points |
| duplicateRor | CHANGED | points |
| duplicateScopusAfid | CHANGED | points |
| duplicateScopusAuthorId | CHANGED | points |
| duplicateWebOfScienceResearcherId | CHANGED | points |
| faxNumberTooLong | CHANGED | points, constraints |
| handleNotResolvable | CHANGED | points, constraints |
| handleTooLong | CHANGED | points |
| handleTooShort | CHANGED | points |
| identifierRegularExpressionTooLong | CHANGED | points |
| invalidCienciaIdFormat | CHANGED | points, constraints |
| invalidContactEmailFormat | CHANGED | points, constraints |
| invalidDoiFormat | CHANGED | points |
| invalidFaxNumberFormat | CHANGED | points, constraints |
| invalidFundrefFormat | CHANGED | points, constraints |
| invalidGoogleScholarIdFormat | CHANGED | points, constraints |
| invalidGridFormat | CHANGED | points, constraints |
| invalidHandleFormat | CHANGED | points, constraints |
| invalidIdentifierRegularExpression | CHANGED | dimension, points, constraints |
| invalidIsniFormat | CHANGED | points, constraints |
| invalidLanguageNameFormat | CHANGED | points, constraints |
| invalidLanguageTagFormat | CHANGED | points, constraints |
| invalidMobilePhoneNumberFormat | CHANGED | points, constraints |
| invalidOpenAlexIdFormat | CHANGED | points, constraints |
| invalidOrcidFormat | CHANGED | points |
| invalidOrganisationUnitNameFormat | CHANGED | points, constraints |
| invalidPhoneNumberFormat | CHANGED | points, constraints |
| invalidRinggoldFormat | CHANGED | points, constraints |
| invalidRorFormat | CHANGED | points, constraints |
| invalidScopusAfidFormat | CHANGED | points, constraints |
| invalidScopusAuthorIdFormat | CHANGED | points, constraints |
| invalidTitleFormat | CHANGED | points, constraints |
| invalidWebOfScienceResearcherIdFormat | CHANGED | points, constraints |
| languageNameMissing | CHANGED | severity, blocking, points |
| languageNameTooLong | CHANGED | points, constraints |
| languageTagMissing | CHANGED | severity, blocking, points |
| languageTagTooLong | CHANGED | points |
| latitudeMissing | CHANGED | severity, blocking, points |
| latitudeOutOfRange | CHANGED | points, constraints |
| lectureHoursOnlyForCourse | CHANGED | points, constraints |
| locationJurisdictionOnlyForTrial | CHANGED | points, constraints |
| longitudeMissing | CHANGED | severity, blocking, points |
| longitudeOutOfRange | CHANGED | points, constraints |
| metadataLicenseMissing | CHANGED | severity, blocking, points |
| mobilePhoneNumberTooLong | CHANGED | points, constraints |
| noDoiPresent | CHANGED | severity, points |
| noHandlePresent | CHANGED | severity, points |
| noIdentifierPresent | CHANGED | blocking, points |
| noOrcidPresent | CHANGED | severity, blocking, points |
| numberOfAppendicesAboveMaximum | CHANGED | dimension, points, constraints |
| numberOfAppendicesBelowMinimum | CHANGED | dimension, points, constraints |
| numberOfChaptersAboveMaximum | CHANGED | dimension, points, constraints |
| numberOfChaptersBelowMinimum | CHANGED | dimension, points, constraints |
| numberOfGraphsAboveMaximum | CHANGED | dimension, points, constraints |
| numberOfGraphsBelowMinimum | CHANGED | dimension, points, constraints |
| numberOfIllustrationsAboveMaximum | CHANGED | dimension, points, constraints |
| numberOfIllustrationsBelowMinimum | CHANGED | dimension, points, constraints |
| numberOfPagesAboveMaximum | CHANGED | dimension, points, constraints |
| numberOfPagesBelowMinimum | CHANGED | dimension, points, constraints |
| numberOfReferencesAboveMaximum | CHANGED | dimension, points, constraints |
| numberOfReferencesBelowMinimum | CHANGED | dimension, points, constraints |
| numberOfReviewsOnlyForConferenceReviewer | CHANGED | points, constraints |
| numberOfReviewsTooHigh | CHANGED | dimension, points, constraints |
| numberOfTablesAboveMaximum | CHANGED | dimension, points, constraints |
| numberOfTablesBelowMinimum | CHANGED | dimension, points, constraints |
| openAccessMissing | CHANGED | points |
| organisationUnitDescriptionMissing | CHANGED | severity, blocking, points |
| organisationUnitNameMissing | CHANGED | severity, blocking, points |
| organisationUnitNameTooLong | CHANGED | points |
| otherContactHoursOnlyForCourse | CHANGED | points, constraints |
| phoneNumberTooLong | CHANGED | points, constraints |
| researchAreaNameMissing | CHANGED | severity, blocking, points |
| researchAreaNameTooLong | CHANGED | points |
| researchAreasMissing | CHANGED | severity, blocking, points |
| thesisDefenceDateMissing | CHANGED | points |
| titleMissing | CHANGED | severity, blocking, points |
| titleTooLong | CHANGED | points |
| topicAcceptanceDateBefore | CHANGED | points, constraints |
| topicAcceptanceDateMissing | CHANGED | points |
| tutorialHoursOnlyForCourse | CHANGED | points, constraints |
| webOfScienceResearcherIdTooLong | CHANGED | points |
| webOfScienceResearcherIdTooShort | CHANGED | points |
| activityEndDateBeforeStartDate | REMOVED |  |
| activityEndDateMissing | REMOVED |  |
| activityStartDateBefore | REMOVED |  |
| activityStartDateBeforeMinAge | REMOVED |  |
| activityStartDateMissing | REMOVED |  |
| addressTooLong | REMOVED |  |
| birthDateInFuture | REMOVED |  |
| contactWebsiteTooLong | REMOVED |  |
| countryCodeInvalidLength | REMOVED |  |
| countryNameMissing | REMOVED |  |
| countryNameTooLong | REMOVED |  |
| dateDissolvedBeforeEstablished | REMOVED |  |
| dateEndTermInvalid | REMOVED |  |
| dateFilingPriorityAfterRequestDate | REMOVED |  |
| dateFilingPriorityInvalid | REMOVED |  |
| dateRequestedAfterCurrentDate | REMOVED |  |
| dateRequestedInvalid | REMOVED |  |
| defenceBeforeAcceptance | REMOVED |  |
| documentBeforePersonBirth | REMOVED |  |
| duplicateResearchAreaUri | REMOVED |  |
| firstNameMissing | REMOVED |  |
| firstNameTooLong | REMOVED |  |
| identifierTypeMissing | REMOVED |  |
| identifierTypeTooLong | REMOVED |  |
| identifierUriTooLong | REMOVED |  |
| identifierValueMissing | REMOVED |  |
| identifierValueTooLong | REMOVED |  |
| invalidAddressFormat | REMOVED |  |
| invalidContactWebsiteFormat | REMOVED |  |
| invalidCorrespondingContributorFlag | REMOVED |  |
| invalidCountryCodeFormat | REMOVED |  |
| invalidCountryNameFormat | REMOVED |  |
| invalidDocumentDateFormat | REMOVED |  |
| invalidFirstNameFormat | REMOVED |  |
| invalidIdentifierUriFormat | REMOVED |  |
| invalidLastNameFormat | REMOVED |  |
| invalidLattesIdFormat | REMOVED |  |
| invalidMainContributorFlag | REMOVED |  |
| invalidResearchAreaNameFormat | REMOVED |  |
| invalidResearchAreaUriFormat | REMOVED |  |
| labHoursOnlyForCourse | REMOVED |  |
| lastNameMissing | REMOVED |  |
| lastNameTooLong | REMOVED |  |
| nameMissing | REMOVED |  |
| noManagedContributor | REMOVED |  |
| researchAreaUriTooLong | REMOVED |  |
| topicAcceptanceDateFuture | REMOVED |  |
| activityInvolvementFromDateAfterMaximumDate | ADDED |  |
| activityInvolvementFromDateBeforeMinimumDate | ADDED |  |
| activityInvolvementFromDateMissing | ADDED |  |
| activityInvolvementResearchAreasInvalidVocabulary | ADDED |  |
| activityInvolvementToDateBeforeMinimumDate | ADDED |  |
| activityInvolvementToDateMissing | ADDED |  |
| activityPersonContributionFromDateAfterMaximumDate | ADDED |  |
| activityPersonContributionFromDateBeforeMinimumDate | ADDED |  |
| activityPersonContributionFromDateMissing | ADDED |  |
| activityPersonContributionResearchAreasInvalidVocabulary | ADDED |  |
| activityPersonContributionResearchAreasMissing | ADDED |  |
| activityPersonContributionToDateBeforeMinimumDate | ADDED |  |
| activityPersonContributionToDateMissing | ADDED |  |
| activityPersonDocumentContributionIsCorrespondingContributorCustomValidation | ADDED |  |
| activityPersonDocumentContributionIsCorrespondingContributorInvalidVocabulary | ADDED |  |
| activityPersonDocumentContributionIsMainContributorCustomValidation | ADDED |  |
| activityPersonDocumentContributionIsMainContributorInvalidVocabulary | ADDED |  |
| activityPersonDocumentContributionPersonCustomValidation | ADDED |  |
| activityPersonEventContributionLabHoursPerWeekCustomValidation | ADDED |  |
| activityPersonEventContributionNumberOfReviewsOrAssessmentBelowMinimum | ADDED |  |
| fundingFundingAmountMissing | ADDED |  |
| fundingFundingCreateDateMissing | ADDED |  |
| fundingFundingDateAwardedAfterMaximumDate | ADDED |  |
| fundingFundingDateAwardedBeforeMinimumDate | ADDED |  |
| fundingFundingDateAwardedMissing | ADDED |  |
| fundingFundingDateSubmittedAfterMaximumDate | ADDED |  |
| fundingFundingDateSubmittedBeforeMinimumDate | ADDED |  |
| fundingFundingDescriptionMissing | ADDED |  |
| fundingFundingDescriptionTooShort | ADDED |  |
| fundingFundingDoiDuplicate | ADDED |  |
| fundingFundingDoiGrantAgreementIdOtherIdentifiersMissing | ADDED |  |
| fundingFundingDoiGrantAgreementIdOtherIdentifiersTooFewValues | ADDED |  |
| fundingFundingDoiInvalidFormat | ADDED |  |
| fundingFundingDoiMissing | ADDED |  |
| fundingFundingDoiNotResolvable | ADDED |  |
| fundingFundingDoiTooLong | ADDED |  |
| fundingFundingDoiTooShort | ADDED |  |
| fundingFundingFromDateAfterMaximumDate | ADDED |  |
| fundingFundingFromDateBeforeMinimumDate | ADDED |  |
| fundingFundingFromDateMissing | ADDED |  |
| fundingFundingLastModificationDateMissing | ADDED |  |
| fundingFundingMetadataAccessLevelInvalidVocabulary | ADDED |  |
| fundingFundingMetadataAccessLevelMissing | ADDED |  |
| fundingFundingMetadataLicenseInvalidVocabulary | ADDED |  |
| fundingFundingMetadataLicenseMissing | ADDED |  |
| fundingFundingNameInvalidFormat | ADDED |  |
| fundingFundingNameMissing | ADDED |  |
| fundingFundingNameTooLong | ADDED |  |
| fundingFundingNameTooShort | ADDED |  |
| fundingFundingProjectInvolvementCustomValidation | ADDED |  |
| fundingFundingProjectInvolvementMissing | ADDED |  |
| fundingFundingProjectInvolvementTooFewValues | ADDED |  |
| fundingFundingProjectReferenceIdDuplicate | ADDED |  |
| fundingFundingProjectReferenceIdMissing | ADDED |  |
| fundingFundingProjectReferenceIdTooLong | ADDED |  |
| fundingFundingProjectReferenceIdTooShort | ADDED |  |
| fundingFundingResearchAreasInvalidVocabulary | ADDED |  |
| fundingFundingResearchAreasMissing | ADDED |  |
| fundingFundingToDateAfterMaximumDate | ADDED |  |
| fundingFundingToDateBeforeMinimumDate | ADDED |  |
| fundingFundingToDateMissing | ADDED |  |
| organisationUnitOrganisationUnitActiveInvalidVocabulary | ADDED |  |
| organisationUnitOrganisationUnitCreateDateMissing | ADDED |  |
| organisationUnitOrganisationUnitDateDissolvedAfterMaximumDate | ADDED |  |
| organisationUnitOrganisationUnitDateDissolvedBeforeMinimumDate | ADDED |  |
| organisationUnitOrganisationUnitDateEstablishedAfterMaximumDate | ADDED |  |
| organisationUnitOrganisationUnitDateEstablishedMissing | ADDED |  |
| organisationUnitOrganisationUnitDescriptionTooShort | ADDED |  |
| organisationUnitOrganisationUnitFundrefDuplicate | ADDED |  |
| organisationUnitOrganisationUnitFundrefTooLong | ADDED |  |
| organisationUnitOrganisationUnitFundrefTooShort | ADDED |  |
| organisationUnitOrganisationUnitGridTooLong | ADDED |  |
| organisationUnitOrganisationUnitGridTooShort | ADDED |  |
| organisationUnitOrganisationUnitIsniTooLong | ADDED |  |
| organisationUnitOrganisationUnitIsniTooShort | ADDED |  |
| organisationUnitOrganisationUnitLastModificationDateMissing | ADDED |  |
| organisationUnitOrganisationUnitMetadataAccessLevelInvalidVocabulary | ADDED |  |
| organisationUnitOrganisationUnitMetadataAccessLevelMissing | ADDED |  |
| organisationUnitOrganisationUnitMetadataLicenseInvalidVocabulary | ADDED |  |
| organisationUnitOrganisationUnitMetadataLicenseMissing | ADDED |  |
| organisationUnitOrganisationUnitNameTooShort | ADDED |  |
| organisationUnitOrganisationUnitOpenAlexIdDuplicate | ADDED |  |
| organisationUnitOrganisationUnitOpenAlexIdInvalidFormat | ADDED |  |
| organisationUnitOrganisationUnitOpenAlexIdTooLong | ADDED |  |
| organisationUnitOrganisationUnitOpenAlexIdTooShort | ADDED |  |
| organisationUnitOrganisationUnitRinggoldTooLong | ADDED |  |
| organisationUnitOrganisationUnitRinggoldTooShort | ADDED |  |
| organisationUnitOrganisationUnitRorIsniDuplicate | ADDED |  |
| organisationUnitOrganisationUnitRorIsniMissing | ADDED |  |
| organisationUnitOrganisationUnitRorMissing | ADDED |  |
| organisationUnitOrganisationUnitRorTooLong | ADDED |  |
| organisationUnitOrganisationUnitRorTooShort | ADDED |  |
| organisationUnitOrganisationUnitScopusAfidTooLong | ADDED |  |
| organisationUnitOrganisationUnitScopusAfidTooShort | ADDED |  |
| organisationUnitOrganisationUnitSectorInvalidVocabulary | ADDED |  |
| organisationUnitOrganisationUnitSectorMissing | ADDED |  |
| outputDocumentContributorsCustomValidation | ADDED |  |
| outputDocumentContributorsTooFewValues | ADDED |  |
| outputDocumentCreateDateMissing | ADDED |  |
| outputDocumentDescriptionTooShort | ADDED |  |
| outputDocumentDoiHandleOtherIdentifiersDuplicate | ADDED |  |
| outputDocumentDoiHandleOtherIdentifiersTooFewValues | ADDED |  |
| outputDocumentLastModificationDateMissing | ADDED |  |
| outputDocumentMetadataAccessLevelInvalidVocabulary | ADDED |  |
| outputDocumentMetadataAccessLevelMissing | ADDED |  |
| outputDocumentMetadataLicenseInvalidVocabulary | ADDED |  |
| outputDocumentOpenAccessInvalidVocabulary | ADDED |  |
| outputDocumentResearchAreasInvalidVocabulary | ADDED |  |
| outputDocumentTitleTooShort | ADDED |  |
| outputIntellectualPropertyDateRequestedAfterMaximumDate | ADDED |  |
| outputPublicationSeriesPublisherFromDateAfterMaximumDate | ADDED |  |
| outputPublicationSeriesPublisherFromDateBeforeMinimumDate | ADDED |  |
| outputPublicationSeriesPublisherFromDateMissing | ADDED |  |
| outputPublicationSeriesPublisherToDateBeforeMinimumDate | ADDED |  |
| outputPublicationUnitPartNumberOfPagesAboveMaximum | ADDED |  |
| outputPublicationUnitPartNumberOfPagesBelowMinimum | ADDED |  |
| outputThesisPhysicalDescriptionNumberOfPagesAboveMaximum | ADDED |  |
| outputThesisPhysicalDescriptionNumberOfPagesBelowMinimum | ADDED |  |
| outputThesisThesisDefenceDateAfterMaximumDate | ADDED |  |
| outputThesisThesisDefenceDateBeforeMinimumDate | ADDED |  |
| outputThesisTopicAcceptanceDateAfterMaximumDate | ADDED |  |
| personEducationDegreeTypeInvalidVocabulary | ADDED |  |
| personEducationDegreeTypeMissing | ADDED |  |
| personEducationEducationStatusInvalidVocabulary | ADDED |  |
| personEducationEducationStatusMissing | ADDED |  |
| personEmploymentEmploymentPositionHierarchyInvalidVocabulary | ADDED |  |
| personEmploymentEmploymentPositionHierarchyMissing | ADDED |  |
| personExpertiseOrSkillResearchAreasInvalidVocabulary | ADDED |  |
| personExpertiseOrSkillResearchAreasMissing | ADDED |  |
| personInvolvementFromDateBeforeMinimumDate | ADDED |  |
| personInvolvementFromDateMissing | ADDED |  |
| personInvolvementFundingPartsFundingCustomValidation | ADDED |  |
| personInvolvementInvolvementTypeInvalidVocabulary | ADDED |  |
| personInvolvementInvolvementTypeMissing | ADDED |  |
| personInvolvementToDateAfterMaximumDate | ADDED |  |
| personInvolvementToDateBeforeMinimumDate | ADDED |  |
| personLanguageKnowledgeAcademicReviewInvalidVocabulary | ADDED |  |
| personLanguageKnowledgeAcademicReviewTooLong | ADDED |  |
| personLanguageKnowledgeAcademicReviewTooShort | ADDED |  |
| personLanguageKnowledgeAcademicWritingInvalidVocabulary | ADDED |  |
| personLanguageKnowledgeAcademicWritingTooLong | ADDED |  |
| personLanguageKnowledgeAcademicWritingTooShort | ADDED |  |
| personLanguageKnowledgeListeningInvalidVocabulary | ADDED |  |
| personLanguageKnowledgeListeningTooLong | ADDED |  |
| personLanguageKnowledgeListeningTooShort | ADDED |  |
| personLanguageKnowledgeOverallInvalidVocabulary | ADDED |  |
| personLanguageKnowledgeOverallTooLong | ADDED |  |
| personLanguageKnowledgeOverallTooShort | ADDED |  |
| personLanguageKnowledgeReadingInvalidVocabulary | ADDED |  |
| personLanguageKnowledgeReadingTooLong | ADDED |  |
| personLanguageKnowledgeReadingTooShort | ADDED |  |
| personLanguageKnowledgeSpeakingInvalidVocabulary | ADDED |  |
| personLanguageKnowledgeSpeakingTooLong | ADDED |  |
| personLanguageKnowledgeSpeakingTooShort | ADDED |  |
| personLanguageKnowledgeWritingInvalidVocabulary | ADDED |  |
| personLanguageKnowledgeWritingTooLong | ADDED |  |
| personLanguageKnowledgeWritingTooShort | ADDED |  |
| personMembershipMembershipTypeInvalidVocabulary | ADDED |  |
| personMembershipMembershipTypeMissing | ADDED |  |
| personPersonAuthenticusIdInvalidFormat | ADDED |  |
| personPersonAuthenticusIdTooLong | ADDED |  |
| personPersonAuthenticusIdTooShort | ADDED |  |
| personPersonBiographyTooShort | ADDED |  |
| personPersonCreateDateMissing | ADDED |  |
| personPersonInvolvementsCustomValidation | ADDED |  |
| personPersonInvolvementsMissing | ADDED |  |
| personPersonInvolvementsTooFewValues | ADDED |  |
| personPersonInvolvementsTooManyValues | ADDED |  |
| personPersonLastModificationDateMissing | ADDED |  |
| personPersonLattesIdDuplicate | ADDED |  |
| personPersonLattesIdInvalidFormat | ADDED |  |
| personPersonLattesIdTooLong | ADDED |  |
| personPersonLattesIdTooShort | ADDED |  |
| personPersonMetadataAccessLevelInvalidVocabulary | ADDED |  |
| personPersonMetadataAccessLevelMissing | ADDED |  |
| personPersonMetadataLicenseInvalidVocabulary | ADDED |  |
| personPersonMetadataLicenseMissing | ADDED |  |
| personPersonNameFirstnameInvalidFormat | ADDED |  |
| personPersonNameFirstnameTooLong | ADDED |  |
| personPersonNameFirstnameTooShort | ADDED |  |
| personPersonNameLastnameInvalidFormat | ADDED |  |
| personPersonNameLastnameMissing | ADDED |  |
| personPersonNameLastnameTooLong | ADDED |  |
| personPersonNameLastnameTooShort | ADDED |  |
| personPersonNameMissing | ADDED |  |
| personPersonNameOtherNameInvalidFormat | ADDED |  |
| personPersonNameOtherNameTooLong | ADDED |  |
| personPersonNameOtherNameTooShort | ADDED |  |
| personPersonNamePersonNameTypeInvalidVocabulary | ADDED |  |
| personPersonNamePersonNameTypeMissing | ADDED |  |
| personPersonNamePersonNameTypeTooLong | ADDED |  |
| personPersonNamePersonNameTypeTooShort | ADDED |  |
| personPersonNameTooLong | ADDED |  |
| personPersonNameTooShort | ADDED |  |
| personPersonNationalIdCienciaIdDuplicate | ADDED |  |
| personPersonNationalIdCienciaIdMissing | ADDED |  |
| personPersonNationalIdCienciaIdTooLong | ADDED |  |
| personPersonNationalIdCienciaIdTooShort | ADDED |  |
| personPersonOpenAlexIdTooLong | ADDED |  |
| personPersonOpenAlexIdTooShort | ADDED |  |
| personPersonOrcidNotResolvable | ADDED |  |
| personPersonOrcidTooLong | ADDED |  |
| personPersonOrcidTooShort | ADDED |  |
| personPersonScholarIdTooLong | ADDED |  |
| personPersonScholarIdTooShort | ADDED |  |
| personPersonScopusAuthorIdTooLong | ADDED |  |
| personPersonScopusAuthorIdTooShort | ADDED |  |
| personPersonalInfoBirthDateAfterMaximumDate | ADDED |  |
| personPersonalInfoSexInvalidVocabulary | ADDED |  |
| personPersonalInfoSexTooLong | ADDED |  |
| personPersonalInfoSexTooShort | ADDED |  |
| personPrizeEffectiveDateAfterMaximumDate | ADDED |  |
| personPrizeEffectiveDateBeforeMinimumDate | ADDED |  |
| personPrizeEffectiveDateMissing | ADDED |  |
| personPrizeResearchAreasInvalidVocabulary | ADDED |  |
| personPrizeResearchAreasMissing | ADDED |  |
| personPrizeToDateBeforeMinimumDate | ADDED |  |
| personPrizeTypeInvalidVocabulary | ADDED |  |
| personPrizeTypeMissing | ADDED |  |
| projectProjectCostsCustomValidation | ADDED |  |
| projectProjectCreateDateMissing | ADDED |  |
| projectProjectDescriptionMissing | ADDED |  |
| projectProjectDescriptionTooShort | ADDED |  |
| projectProjectDoiDuplicate | ADDED |  |
| projectProjectDoiInvalidFormat | ADDED |  |
| projectProjectDoiMissing | ADDED |  |
| projectProjectDoiNotResolvable | ADDED |  |
| projectProjectDoiRaidProjectReferenceOtherIdentifiersDuplicate | ADDED |  |
| projectProjectDoiRaidProjectReferenceOtherIdentifiersMissing | ADDED |  |
| projectProjectDoiRaidProjectReferenceOtherIdentifiersTooFewValues | ADDED |  |
| projectProjectDoiTooLong | ADDED |  |
| projectProjectDoiTooShort | ADDED |  |
| projectProjectFromDateAfterMaximumDate | ADDED |  |
| projectProjectFromDateBeforeMinimumDate | ADDED |  |
| projectProjectFromDateMissing | ADDED |  |
| projectProjectFundingsCustomValidation | ADDED |  |
| projectProjectFundingsMissing | ADDED |  |
| projectProjectFundingsTooFewValues | ADDED |  |
| projectProjectFundingsTooManyValues | ADDED |  |
| projectProjectLastModificationDateMissing | ADDED |  |
| projectProjectMetadataAccessLevelInvalidVocabulary | ADDED |  |
| projectProjectMetadataAccessLevelMissing | ADDED |  |
| projectProjectMetadataLicenseInvalidVocabulary | ADDED |  |
| projectProjectMetadataLicenseMissing | ADDED |  |
| projectProjectNameInvalidFormat | ADDED |  |
| projectProjectNameMissing | ADDED |  |
| projectProjectNameTooLong | ADDED |  |
| projectProjectNameTooShort | ADDED |  |
| projectProjectNationalIdProjectReferenceDuplicate | ADDED |  |
| projectProjectNationalIdProjectReferenceMissing | ADDED |  |
| projectProjectNationalIdProjectReferenceTooLong | ADDED |  |
| projectProjectNationalIdProjectReferenceTooShort | ADDED |  |
| projectProjectOrganisationsCustomValidation | ADDED |  |
| projectProjectOrganisationsMissing | ADDED |  |
| projectProjectOrganisationsTooFewValues | ADDED |  |
| projectProjectOrganisationsTooManyValues | ADDED |  |
| projectProjectRaidDuplicate | ADDED |  |
| projectProjectRaidInvalidFormat | ADDED |  |
| projectProjectRaidMissing | ADDED |  |
| projectProjectRaidNotResolvable | ADDED |  |
| projectProjectRaidTooLong | ADDED |  |
| projectProjectRaidTooShort | ADDED |  |
| projectProjectResearchAreasDuplicate | ADDED |  |
| projectProjectResearchAreasInvalidVocabulary | ADDED |  |
| projectProjectResearchAreasMissing | ADDED |  |
| projectProjectTeamCustomValidation | ADDED |  |
| projectProjectTeamMissing | ADDED |  |
| projectProjectTeamTooFewValues | ADDED |  |
| projectProjectTeamTooManyValues | ADDED |  |
| projectProjectToDateAfterMaximumDate | ADDED |  |
| projectProjectToDateBeforeMinimumDate | ADDED |  |
| projectProjectToDateMissing | ADDED |  |
| sharedComponentsContactContactEmailTooShort | ADDED |  |
| sharedComponentsContactFaxNumberTooShort | ADDED |  |
| sharedComponentsContactMobilePhoneNumberTooShort | ADDED |  |
| sharedComponentsContactPhoneNumberTooShort | ADDED |  |
| sharedComponentsCountryCodeInvalidVocabulary | ADDED |  |
| sharedComponentsCountryCodeTooLong | ADDED |  |
| sharedComponentsCountryCodeTooShort | ADDED |  |
| sharedComponentsCurrencyCodeDuplicate | ADDED |  |
| sharedComponentsCurrencyCodeInvalidFormat | ADDED |  |
| sharedComponentsCurrencyCodeInvalidVocabulary | ADDED |  |
| sharedComponentsCurrencyCodeMissing | ADDED |  |
| sharedComponentsCurrencyCodeTooLong | ADDED |  |
| sharedComponentsCurrencyCodeTooShort | ADDED |  |
| sharedComponentsCurrencySymbolInvalidVocabulary | ADDED |  |
| sharedComponentsCurrencySymbolTooLong | ADDED |  |
| sharedComponentsCurrencySymbolTooShort | ADDED |  |
| sharedComponentsEntityIndicatorNumericValueBooleanValueTextualValueCustomValidation | ADDED |  |
| sharedComponentsEntityIndicatorNumericValueBooleanValueTextualValueMissing | ADDED |  |
| sharedComponentsEntityIndicatorSubclassCustomValidation | ADDED |  |
| sharedComponentsFlexibleDateDayAboveMaximum | ADDED |  |
| sharedComponentsFlexibleDateDayBelowMinimum | ADDED |  |
| sharedComponentsFlexibleDateDayCustomValidation | ADDED |  |
| sharedComponentsFlexibleDateDayMissing | ADDED |  |
| sharedComponentsFlexibleDateMonthAboveMaximum | ADDED |  |
| sharedComponentsFlexibleDateMonthBelowMinimum | ADDED |  |
| sharedComponentsFlexibleDateMonthMissing | ADDED |  |
| sharedComponentsFlexibleDateTextYearCustomValidation | ADDED |  |
| sharedComponentsFlexibleDateTextYearMissing | ADDED |  |
| sharedComponentsFlexibleDateYearAboveMaximum | ADDED |  |
| sharedComponentsFlexibleDateYearBelowMinimum | ADDED |  |
| sharedComponentsFlexibleDateYearMissing | ADDED |  |
| sharedComponentsGeoLocationAddressMissing | ADDED |  |
| sharedComponentsGeoLocationLatitudeAboveMaximum | ADDED |  |
| sharedComponentsGeoLocationLongitudeAboveMaximum | ADDED |  |
| sharedComponentsIdentifierRegularExpressionMissing | ADDED |  |
| sharedComponentsIdentifierRegularExpressionTooShort | ADDED |  |
| sharedComponentsLanguageLanguageCodeDuplicate | ADDED |  |
| sharedComponentsLanguageLanguageCodeInvalidVocabulary | ADDED |  |
| sharedComponentsLanguageLanguageCodeTooShort | ADDED |  |
| sharedComponentsLanguageTagLanguageTagInvalidVocabulary | ADDED |  |
| sharedComponentsLanguageTagLanguageTagTooShort | ADDED |  |
| sharedComponentsMonetaryAmountAmountAboveMaximum | ADDED |  |
| sharedComponentsMonetaryAmountAmountBelowMinimum | ADDED |  |
| sharedComponentsMonetaryAmountAmountMissing | ADDED |  |
| sharedComponentsProfilePhotoOrLogoHeightAboveMaximum | ADDED |  |
| sharedComponentsProfilePhotoOrLogoHeightBelowMinimum | ADDED |  |
| sharedComponentsProfilePhotoOrLogoHeightMissing | ADDED |  |
| sharedComponentsProfilePhotoOrLogoLeftOffsetAboveMaximum | ADDED |  |
| sharedComponentsProfilePhotoOrLogoLeftOffsetBelowMinimum | ADDED |  |
| sharedComponentsProfilePhotoOrLogoLeftOffsetMissing | ADDED |  |
| sharedComponentsProfilePhotoOrLogoTopOffsetAboveMaximum | ADDED |  |
| sharedComponentsProfilePhotoOrLogoTopOffsetBelowMinimum | ADDED |  |
| sharedComponentsProfilePhotoOrLogoTopOffsetMissing | ADDED |  |
| sharedComponentsProfilePhotoOrLogoWidthAboveMaximum | ADDED |  |
| sharedComponentsProfilePhotoOrLogoWidthBelowMinimum | ADDED |  |
| sharedComponentsProfilePhotoOrLogoWidthMissing | ADDED |  |
| sharedComponentsResearchAreaNameInvalidVocabulary | ADDED |  |
| sharedComponentsResearchAreaNameTooShort | ADDED |  |
