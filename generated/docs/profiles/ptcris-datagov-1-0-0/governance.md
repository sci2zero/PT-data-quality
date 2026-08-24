# Governance mapping — PTCRIS-DATAGOV-1.0.0

| Constraint | Dimension | Metric | Requirement | Status |
|---|---|---|---|---|
| C.PERSON.Education.DegreeType.presence |  |  |  | UNMAPPED |
| C.PERSON.Education.DegreeType.vocabulary |  |  |  | UNMAPPED |
| C.PERSON.Education.EducationStatus.presence |  |  |  | UNMAPPED |
| C.PERSON.Education.EducationStatus.vocabulary |  |  |  | UNMAPPED |
| C.PERSON.Employment.EmploymentPositionHierarchy.presence |  |  |  | UNMAPPED |
| C.PERSON.Employment.EmploymentPositionHierarchy.vocabulary | PTCRIS.SEMANTIC | PTCRIS-F1-01DSEMANT | GR.PTCRIS_F1_01DSEMANT.type_professional_path_classification_validation | FULL |
| C.PERSON.ExpertiseOrSkill.ResearchAreas.presence |  |  |  | UNMAPPED |
| C.PERSON.ExpertiseOrSkill.ResearchAreas.vocabulary |  |  |  | UNMAPPED |
| C.PERSON.Involvement.FromDate.maxDate |  |  |  | UNMAPPED |
| C.PERSON.Involvement.FromDate.minDate |  |  |  | UNMAPPED |
| C.PERSON.Involvement.FromDate.presence |  |  |  | UNMAPPED |
| C.PERSON.Involvement.FundingPartsFunding.custom |  |  |  | UNMAPPED |
| C.PERSON.Involvement.InvolvementType.presence |  |  |  | UNMAPPED |
| C.PERSON.Involvement.InvolvementType.vocabulary |  |  |  | UNMAPPED |
| C.PERSON.Involvement.ToDate.maxDate |  |  |  | UNMAPPED |
| C.PERSON.Involvement.ToDate.minDate |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.AcademicReview.maxLength |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.AcademicReview.minLength |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.AcademicReview.vocabulary |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.AcademicWriting.maxLength |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.AcademicWriting.minLength |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.AcademicWriting.vocabulary |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.Listening.maxLength |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.Listening.minLength |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.Listening.vocabulary |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.Overall.maxLength |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.Overall.minLength |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.Overall.vocabulary |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.Reading.maxLength |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.Reading.minLength |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.Reading.vocabulary |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.Speaking.maxLength |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.Speaking.minLength |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.Speaking.vocabulary |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.Writing.maxLength |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.Writing.minLength |  |  |  | UNMAPPED |
| C.PERSON.LanguageKnowledge.Writing.vocabulary |  |  |  | UNMAPPED |
| C.PERSON.Membership.MembershipType.presence |  |  |  | UNMAPPED |
| C.PERSON.Membership.MembershipType.vocabulary |  |  |  | UNMAPPED |
| C.PERSON.Person.AuthenticusId.maxLength | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.AuthenticusId.maxLength | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.AuthenticusId.minLength | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.AuthenticusId.minLength | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.AuthenticusId.pattern | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.AuthenticusId.pattern | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.AuthenticusId.unique | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.AuthenticusId.unique | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.Biography.minLength |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| C.PERSON.Person.Biography.presence |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| C.PERSON.Person.CreateDate.presence | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.Involvements.custom |  |  |  | UNMAPPED |
| C.PERSON.Person.Involvements.maxCardinality |  |  |  | UNMAPPED |
| C.PERSON.Person.Involvements.minCardinality |  |  |  | UNMAPPED |
| C.PERSON.Person.Involvements.presence | PTCRIS.CURRENCY | PTCRIS-F1-01DCURREN | GR.PTCRIS_F1_01DCURREN.mandatory_start_date_of_professional_career | FULL |
| C.PERSON.Person.LastModificationDate.presence | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.LattesId.maxLength | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.LattesId.maxLength | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.LattesId.minLength | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.LattesId.minLength | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.LattesId.pattern | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.LattesId.pattern | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.LattesId.unique | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.LattesId.unique | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.MetadataAccessLevel.presence |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| C.PERSON.Person.MetadataAccessLevel.vocabulary |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| C.PERSON.Person.MetadataLicense.presence |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| C.PERSON.Person.MetadataLicense.vocabulary |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| C.PERSON.Person.Name.maxLength |  |  |  | UNMAPPED |
| C.PERSON.Person.Name.minLength |  |  |  | UNMAPPED |
| C.PERSON.Person.Name.presence | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.full_name_presence_and_length_validation | FULL |
| C.PERSON.Person.NationalIdCienciaId.maxLength | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.NationalIdCienciaId.maxLength |  | PTCRIS-DQ-F1-01IDUNIQ |  | METRIC_ONLY |
| C.PERSON.Person.NationalIdCienciaId.minLength | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.NationalIdCienciaId.minLength |  | PTCRIS-DQ-F1-01IDUNIQ |  | METRIC_ONLY |
| C.PERSON.Person.NationalIdCienciaId.presence | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.NationalIdCienciaId.presence |  | PTCRIS-DQ-F1-01IDUNIQ |  | METRIC_ONLY |
| C.PERSON.Person.NationalIdCienciaId.pattern | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.NationalIdCienciaId.pattern |  | PTCRIS-DQ-F1-01IDUNIQ |  | METRIC_ONLY |
| C.PERSON.Person.NationalIdCienciaId.unique | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.NationalIdCienciaId.unique | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_science_id_allocation | FULL |
| C.PERSON.Person.NationalIdCienciaId.unique |  | PTCRIS-DQ-F1-01IDUNIQ |  | METRIC_ONLY |
| C.PERSON.Person.OpenAlexId.maxLength | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.OpenAlexId.maxLength | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.OpenAlexId.minLength | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.OpenAlexId.minLength | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.OpenAlexId.pattern | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.OpenAlexId.pattern | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.OpenAlexId.unique | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.OpenAlexId.unique | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.Orcid.maxLength |  |  |  | UNMAPPED |
| C.PERSON.Person.Orcid.minLength |  |  |  | UNMAPPED |
| C.PERSON.Person.Orcid.presence |  |  |  | UNMAPPED |
| C.PERSON.Person.Orcid.pattern | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.open_researcher_and_contributor_id_orcid_format_verification | FULL |
| C.PERSON.Person.Orcid.resolvable |  | PTCRIS-F1, A1 | GR.PTCRIS_F1_A1.resolvable_pid | FULL |
| C.PERSON.Person.Orcid.unique | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_orcid_allocation | FULL |
| C.PERSON.Person.ScholarId.maxLength | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.ScholarId.maxLength | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.ScholarId.minLength | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.ScholarId.minLength | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.ScholarId.pattern | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.ScholarId.pattern | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.ScholarId.unique | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.ScholarId.unique | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.ScopusAuthorId.maxLength | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.ScopusAuthorId.minLength | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.ScopusAuthorId.pattern | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.scopus_author_id_format_validation | FULL |
| C.PERSON.Person.ScopusAuthorId.pattern | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.ScopusAuthorId.unique | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.WebOfScienceResearcherId.maxLength | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.WebOfScienceResearcherId.minLength | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.WebOfScienceResearcherId.pattern | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.web_of_science_researcher_id_format_validation | FULL |
| C.PERSON.Person.WebOfScienceResearcherId.pattern | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.Person.WebOfScienceResearcherId.unique | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| C.PERSON.PersonName.Firstname.maxLength |  |  |  | UNMAPPED |
| C.PERSON.PersonName.Firstname.minLength |  |  |  | UNMAPPED |
| C.PERSON.PersonName.Firstname.pattern |  |  |  | UNMAPPED |
| C.PERSON.PersonName.Lastname.maxLength |  |  |  | UNMAPPED |
| C.PERSON.PersonName.Lastname.minLength |  |  |  | UNMAPPED |
| C.PERSON.PersonName.Lastname.presence | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.full_name_presence_and_length_validation | FULL |
| C.PERSON.PersonName.Lastname.pattern | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.standardized_citation_name_format_verification | FULL |
| C.PERSON.PersonName.OtherName.maxLength |  |  |  | UNMAPPED |
| C.PERSON.PersonName.OtherName.minLength |  |  |  | UNMAPPED |
| C.PERSON.PersonName.OtherName.pattern |  |  |  | UNMAPPED |
| C.PERSON.PersonName.PersonNameType.maxLength |  |  |  | UNMAPPED |
| C.PERSON.PersonName.PersonNameType.minLength |  |  |  | UNMAPPED |
| C.PERSON.PersonName.PersonNameType.presence |  |  |  | UNMAPPED |
| C.PERSON.PersonName.PersonNameType.vocabulary |  |  |  | UNMAPPED |
| C.PERSON.PersonalInfo.BirthDate.maxDate | PTCRIS.CONSISTENCY | PTCRIS-F1-01DCONSIST | GR.PTCRIS_F1_01DCONSIST.non_existent_or_futuristic_birth_date_restriction | FULL |
| C.PERSON.PersonalInfo.BirthDate.minDate | PTCRIS.CONSISTENCY | PTCRIS-F1-01DCONSIST | GR.PTCRIS_F1_01DCONSIST.non_existent_or_futuristic_birth_date_restriction | FULL |
| C.PERSON.PersonalInfo.BirthDate.presence |  |  |  | UNMAPPED |
| C.PERSON.PersonalInfo.Sex.maxLength |  |  |  | UNMAPPED |
| C.PERSON.PersonalInfo.Sex.minLength |  |  |  | UNMAPPED |
| C.PERSON.PersonalInfo.Sex.vocabulary | PTCRIS.SEMANTIC | PTCRIS-F1-01DSEMANT | GR.PTCRIS_F1_01DSEMANT.gender_classification_conformity | FULL |
| C.PERSON.Prize.EffectiveDate.maxDate |  |  |  | UNMAPPED |
| C.PERSON.Prize.EffectiveDate.minDate |  |  |  | UNMAPPED |
| C.PERSON.Prize.EffectiveDate.presence |  |  |  | UNMAPPED |
| C.PERSON.Prize.ResearchAreas.presence |  |  |  | UNMAPPED |
| C.PERSON.Prize.ResearchAreas.vocabulary |  |  |  | UNMAPPED |
| C.PERSON.Prize.ToDate.minDate |  |  |  | UNMAPPED |
| C.PERSON.Prize.Type.presence |  |  |  | UNMAPPED |
| C.PERSON.Prize.Type.vocabulary |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Active.vocabulary |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.CreateDate.presence | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| C.ORGANISATION_UNIT.OrganisationUnit.DateDissolved.maxDate |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.DateDissolved.minDate |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.DateEstablished.maxDate |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.DateEstablished.presence |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Description.minLength |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| C.ORGANISATION_UNIT.OrganisationUnit.Description.presence |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| C.ORGANISATION_UNIT.OrganisationUnit.Fundref.maxLength |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Fundref.minLength |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Fundref.pattern |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Fundref.unique |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Grid.maxLength |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Grid.minLength |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Grid.pattern |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Grid.unique |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Isni.maxLength |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Isni.minLength |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Isni.pattern |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Isni.unique |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.LastModificationDate.presence | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| C.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel.presence |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| C.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel.vocabulary |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| C.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense.presence |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| C.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense.vocabulary |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| C.ORGANISATION_UNIT.OrganisationUnit.Name.maxLength |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Name.minLength |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Name.presence |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Name.pattern |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId.maxLength |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId.minLength |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId.pattern |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId.unique |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Ringgold.maxLength |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Ringgold.minLength |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Ringgold.pattern |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Ringgold.unique |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Ror.maxLength |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Ror.minLength |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Ror.presence |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Ror.pattern |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Ror.unique |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.RorIsni.presence |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.RorIsni.unique |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid.maxLength |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid.minLength |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid.pattern |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid.unique |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Sector.presence |  |  |  | UNMAPPED |
| C.ORGANISATION_UNIT.OrganisationUnit.Sector.vocabulary |  |  |  | UNMAPPED |
| C.PROJECT.Project.Costs.custom | PTCRIS.CONSISTENCY | PTCRIS-F1-01DCONSIST | GR.PTCRIS_F1_01DCONSIST.sum_of_linked_fundings_amounts | FULL |
| C.PROJECT.Project.CreateDate.presence | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| C.PROJECT.Project.Description.minLength |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| C.PROJECT.Project.Description.presence |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| C.PROJECT.Project.Doi.maxLength |  |  |  | UNMAPPED |
| C.PROJECT.Project.Doi.minLength |  |  |  | UNMAPPED |
| C.PROJECT.Project.Doi.presence |  |  |  | UNMAPPED |
| C.PROJECT.Project.Doi.pattern | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.doi_format_verification | FULL |
| C.PROJECT.Project.Doi.resolvable |  | PTCRIS-F1, A1 | GR.PTCRIS_F1_A1.resolvable_doi | FULL |
| C.PROJECT.Project.Doi.unique | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_doi_allocation | FULL |
| C.PROJECT.Project.Identifiers.minCardinality | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.project_without_at_least_one_identifier | FULL |
| C.PROJECT.Project.Identifiers.presence | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.project_without_at_least_one_identifier | FULL |
| C.PROJECT.Project.Identifiers.unique |  |  |  | UNMAPPED |
| C.PROJECT.Project.FromDate.maxDate |  |  |  | UNMAPPED |
| C.PROJECT.Project.FromDate.minDate |  |  |  | UNMAPPED |
| C.PROJECT.Project.FromDate.presence | PTCRIS.CURRENCY | PTCRIS-F1-01DCURREN | GR.PTCRIS_F1_01DCURREN.mandatory_project_boundary_dates | FULL |
| C.PROJECT.Project.Fundings.custom | PTCRIS.CONSISTENCY | PTCRIS-F1-01DCONSIST | GR.PTCRIS_F1_01DCONSIST.different_funding_ids_in_project_and_funding | FULL |
| C.PROJECT.Project.Fundings.maxCardinality |  |  |  | UNMAPPED |
| C.PROJECT.Project.Fundings.minCardinality |  |  |  | UNMAPPED |
| C.PROJECT.Project.Fundings.presence |  |  |  | UNMAPPED |
| C.PROJECT.Project.LastModificationDate.presence | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| C.PROJECT.Project.MetadataAccessLevel.presence |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| C.PROJECT.Project.MetadataAccessLevel.vocabulary |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| C.PROJECT.Project.MetadataLicense.presence |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| C.PROJECT.Project.MetadataLicense.vocabulary |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| C.PROJECT.Project.Name.maxLength |  |  |  | UNMAPPED |
| C.PROJECT.Project.Name.minLength |  |  |  | UNMAPPED |
| C.PROJECT.Project.Name.presence | PTCRIS.CONSISTENCY | PTCRIS-F1-01DCONSIST | GR.PTCRIS_F1_01DCONSIST.project_title_presence_requirement | FULL |
| C.PROJECT.Project.Name.pattern |  |  |  | UNMAPPED |
| C.PROJECT.Project.NationalIdProjectReference.maxLength |  |  |  | UNMAPPED |
| C.PROJECT.Project.NationalIdProjectReference.minLength |  |  |  | UNMAPPED |
| C.PROJECT.Project.NationalIdProjectReference.presence |  |  |  | UNMAPPED |
| C.PROJECT.Project.NationalIdProjectReference.unique | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_pid_allocation | FULL |
| C.PROJECT.Project.Organisations.custom | PTCRIS.CONSISTENCY | PTCRIS-F1-01DCONSIST | GR.PTCRIS_F1_01DCONSIST.sum_of_organizations_funding_greater_than_project_total | FULL |
| C.PROJECT.Project.Organisations.custom | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.project_with_coordinating_organization_but_no_other_participants | FULL |
| C.PROJECT.Project.Organisations.maxCardinality |  |  |  | UNMAPPED |
| C.PROJECT.Project.Organisations.minCardinality |  |  |  | UNMAPPED |
| C.PROJECT.Project.Organisations.presence |  |  |  | UNMAPPED |
| C.PROJECT.Project.Raid.maxLength |  |  |  | UNMAPPED |
| C.PROJECT.Project.Raid.minLength |  |  |  | UNMAPPED |
| C.PROJECT.Project.Raid.presence |  |  |  | UNMAPPED |
| C.PROJECT.Project.Raid.pattern | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.raid_format_verification | FULL |
| C.PROJECT.Project.Raid.resolvable |  | PTCRIS-F1, A1 | GR.PTCRIS_F1_A1.resolvable_raid | FULL |
| C.PROJECT.Project.Raid.unique | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_raid_allocation | FULL |
| C.PROJECT.Project.ResearchAreas.presence |  |  |  | UNMAPPED |
| C.PROJECT.Project.ResearchAreas.unique |  |  |  | UNMAPPED |
| C.PROJECT.Project.ResearchAreas.vocabulary | PTCRIS.CONSISTENCY | PTCRIS-F1-01DCONSIST | GR.PTCRIS_F1_01DCONSIST.semantic_iri_url_validation | FULL |
| C.PROJECT.Project.Team.custom | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.project_with_team_but_no_principal_investigator | FULL |
| C.PROJECT.Project.Team.maxCardinality |  |  |  | UNMAPPED |
| C.PROJECT.Project.Team.minCardinality |  |  |  | UNMAPPED |
| C.PROJECT.Project.Team.presence |  |  |  | UNMAPPED |
| C.PROJECT.Project.ToDate.maxDate |  |  |  | UNMAPPED |
| C.PROJECT.Project.ToDate.minDate |  |  |  | UNMAPPED |
| C.PROJECT.Project.ToDate.presence | PTCRIS.CURRENCY | PTCRIS-F1-01DCURREN | GR.PTCRIS_F1_01DCURREN.mandatory_project_boundary_dates | FULL |
| C.FUNDING.Funding.Amount.presence |  |  |  | UNMAPPED |
| C.FUNDING.Funding.CreateDate.presence | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| C.FUNDING.Funding.DateAwarded.maxDate |  |  |  | UNMAPPED |
| C.FUNDING.Funding.DateAwarded.minDate |  |  |  | UNMAPPED |
| C.FUNDING.Funding.DateAwarded.presence | PTCRIS.CURRENCY | PTCRIS-F1-01DCURREN | GR.PTCRIS_F1_01DCURREN.award_year_required_verification | FULL |
| C.FUNDING.Funding.DateSubmitted.maxDate |  |  |  | UNMAPPED |
| C.FUNDING.Funding.DateSubmitted.minDate |  |  |  | UNMAPPED |
| C.FUNDING.Funding.Description.minLength |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| C.FUNDING.Funding.Description.presence |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| C.FUNDING.Funding.Doi.maxLength |  |  |  | UNMAPPED |
| C.FUNDING.Funding.Doi.minLength |  |  |  | UNMAPPED |
| C.FUNDING.Funding.Doi.presence |  |  |  | UNMAPPED |
| C.FUNDING.Funding.Doi.pattern | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.doi_format_verification | FULL |
| C.FUNDING.Funding.Doi.resolvable |  | PTCRIS-F1, A1 | GR.PTCRIS_F1_A1.resolvable_doi | FULL |
| C.FUNDING.Funding.Doi.unique | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_doi_allocation | FULL |
| C.FUNDING.Funding.Identifiers.minCardinality |  |  |  | UNMAPPED |
| C.FUNDING.Funding.Identifiers.presence |  |  |  | UNMAPPED |
| C.FUNDING.Funding.FromDate.maxDate | PTCRIS.CURRENCY | PTCRIS-F1-01DCURREN | GR.PTCRIS_F1_01DCURREN.project_funding_with_suspicious_start_date | FULL |
| C.FUNDING.Funding.FromDate.minDate | PTCRIS.CURRENCY | PTCRIS-F1-01DCURREN | GR.PTCRIS_F1_01DCURREN.project_funding_with_suspicious_start_date | FULL |
| C.FUNDING.Funding.FromDate.presence |  |  |  | UNMAPPED |
| C.FUNDING.Funding.LastModificationDate.presence | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| C.FUNDING.Funding.MetadataAccessLevel.presence |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| C.FUNDING.Funding.MetadataAccessLevel.vocabulary |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| C.FUNDING.Funding.MetadataLicense.presence |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| C.FUNDING.Funding.MetadataLicense.vocabulary |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| C.FUNDING.Funding.Name.maxLength |  |  |  | UNMAPPED |
| C.FUNDING.Funding.Name.minLength |  |  |  | UNMAPPED |
| C.FUNDING.Funding.Name.presence |  |  |  | UNMAPPED |
| C.FUNDING.Funding.Name.pattern | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.format_validation_for_award_title_name | FULL |
| C.FUNDING.Funding.ProjectInvolvement.custom |  |  |  | UNMAPPED |
| C.FUNDING.Funding.ProjectInvolvement.minCardinality |  |  |  | UNMAPPED |
| C.FUNDING.Funding.ProjectInvolvement.presence |  |  |  | UNMAPPED |
| C.FUNDING.Funding.ProjectReferenceId.maxLength |  |  |  | UNMAPPED |
| C.FUNDING.Funding.ProjectReferenceId.minLength |  |  |  | UNMAPPED |
| C.FUNDING.Funding.ProjectReferenceId.presence |  |  |  | UNMAPPED |
| C.FUNDING.Funding.ProjectReferenceId.unique | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_pid_allocation | FULL |
| C.FUNDING.Funding.ResearchAreas.presence |  |  |  | UNMAPPED |
| C.FUNDING.Funding.ResearchAreas.vocabulary |  |  |  | UNMAPPED |
| C.FUNDING.Funding.ToDate.maxDate | PTCRIS.CURRENCY | PTCRIS-F1-01DCURREN | GR.PTCRIS_F1_01DCURREN.project_funding_with_suspicious_start_date | FULL |
| C.FUNDING.Funding.ToDate.minDate | PTCRIS.CURRENCY | PTCRIS-F1-01DCURREN | GR.PTCRIS_F1_01DCURREN.project_funding_with_suspicious_start_date | FULL |
| C.FUNDING.Funding.ToDate.presence |  |  |  | UNMAPPED |
| C.OUTPUT.Document.Contributors.custom |  |  |  | UNMAPPED |
| C.OUTPUT.Document.Contributors.minCardinality |  |  |  | UNMAPPED |
| C.OUTPUT.Document.Contributors.presence |  |  |  | UNMAPPED |
| C.OUTPUT.Document.CreateDate.presence | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| C.OUTPUT.Document.Description.minLength |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| C.OUTPUT.Document.Description.presence |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| C.OUTPUT.Document.DocumentDate.maxDate |  |  |  | UNMAPPED |
| C.OUTPUT.Document.DocumentDate.minDate |  |  |  | UNMAPPED |
| C.OUTPUT.Document.DocumentDate.presence |  |  |  | UNMAPPED |
| C.OUTPUT.Document.Doi.maxLength |  |  |  | UNMAPPED |
| C.OUTPUT.Document.Doi.minLength |  |  |  | UNMAPPED |
| C.OUTPUT.Document.Doi.presence |  |  |  | UNMAPPED |
| C.OUTPUT.Document.Doi.pattern | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.doi_format_verification | FULL |
| C.OUTPUT.Document.Doi.resolvable |  | PTCRIS-F1, A1 | GR.PTCRIS_F1_A1.resolvable_doi | FULL |
| C.OUTPUT.Document.Doi.unique | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_doi_allocation | FULL |
| C.OUTPUT.Document.Identifiers.minCardinality |  |  |  | UNMAPPED |
| C.OUTPUT.Document.Identifiers.presence |  |  |  | UNMAPPED |
| C.OUTPUT.Document.Identifiers.unique |  |  |  | UNMAPPED |
| C.OUTPUT.Document.Handle.maxLength |  |  |  | UNMAPPED |
| C.OUTPUT.Document.Handle.minLength |  |  |  | UNMAPPED |
| C.OUTPUT.Document.Handle.presence |  |  |  | UNMAPPED |
| C.OUTPUT.Document.Handle.pattern | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.handle_format_verification | FULL |
| C.OUTPUT.Document.Handle.resolvable |  | PTCRIS-F1, A1 | GR.PTCRIS_F1_A1.resolvable_handle | FULL |
| C.OUTPUT.Document.Handle.unique | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_handle_allocation | FULL |
| C.OUTPUT.Document.LastModificationDate.presence | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| C.OUTPUT.Document.MetadataAccessLevel.presence |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| C.OUTPUT.Document.MetadataAccessLevel.vocabulary |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| C.OUTPUT.Document.MetadataLicense.presence |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| C.OUTPUT.Document.MetadataLicense.vocabulary |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| C.OUTPUT.Document.OpenAccess.presence |  |  |  | UNMAPPED |
| C.OUTPUT.Document.OpenAccess.vocabulary |  |  |  | UNMAPPED |
| C.OUTPUT.Document.ResearchAreas.presence |  |  |  | UNMAPPED |
| C.OUTPUT.Document.ResearchAreas.vocabulary |  |  |  | UNMAPPED |
| C.OUTPUT.Document.Title.maxLength |  |  |  | UNMAPPED |
| C.OUTPUT.Document.Title.minLength |  |  |  | UNMAPPED |
| C.OUTPUT.Document.Title.presence |  |  |  | UNMAPPED |
| C.OUTPUT.Document.Title.pattern |  |  |  | UNMAPPED |
| C.OUTPUT.IntellectualProperty.DateEndTerm.minDate |  |  |  | UNMAPPED |
| C.OUTPUT.IntellectualProperty.DateEndTerm.presence |  |  |  | UNMAPPED |
| C.OUTPUT.IntellectualProperty.DateFilingPriority.maxDate |  |  |  | UNMAPPED |
| C.OUTPUT.IntellectualProperty.DateFilingPriority.minDate |  |  |  | UNMAPPED |
| C.OUTPUT.IntellectualProperty.DateFilingPriority.presence |  |  |  | UNMAPPED |
| C.OUTPUT.IntellectualProperty.DateRequested.maxDate |  |  |  | UNMAPPED |
| C.OUTPUT.IntellectualProperty.DateRequested.minDate |  |  |  | UNMAPPED |
| C.OUTPUT.IntellectualProperty.DateRequested.presence |  |  |  | UNMAPPED |
| C.OUTPUT.PublicationSeriesPublisher.FromDate.maxDate |  |  |  | UNMAPPED |
| C.OUTPUT.PublicationSeriesPublisher.FromDate.minDate |  |  |  | UNMAPPED |
| C.OUTPUT.PublicationSeriesPublisher.FromDate.presence |  |  |  | UNMAPPED |
| C.OUTPUT.PublicationSeriesPublisher.ToDate.minDate |  |  |  | UNMAPPED |
| C.OUTPUT.PublicationUnit.NumberOfPages.maxValue |  |  |  | UNMAPPED |
| C.OUTPUT.PublicationUnit.NumberOfPages.minValue |  |  |  | UNMAPPED |
| C.OUTPUT.PublicationUnitPart.NumberOfPages.maxValue |  |  |  | UNMAPPED |
| C.OUTPUT.PublicationUnitPart.NumberOfPages.minValue |  |  |  | UNMAPPED |
| C.OUTPUT.Thesis.ThesisDefenceDate.maxDate |  |  |  | UNMAPPED |
| C.OUTPUT.Thesis.ThesisDefenceDate.minDate |  |  |  | UNMAPPED |
| C.OUTPUT.Thesis.ThesisDefenceDate.presence |  |  |  | UNMAPPED |
| C.OUTPUT.Thesis.TopicAcceptanceDate.maxDate |  |  |  | UNMAPPED |
| C.OUTPUT.Thesis.TopicAcceptanceDate.minDate |  |  |  | UNMAPPED |
| C.OUTPUT.Thesis.TopicAcceptanceDate.presence |  |  |  | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfAppendices.maxValue |  |  |  | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfAppendices.minValue |  |  |  | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfChapters.maxValue |  |  |  | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfChapters.minValue |  |  |  | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfGraphs.maxValue |  |  |  | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfGraphs.minValue |  |  |  | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfIlustrations.maxValue |  |  |  | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfIlustrations.minValue |  |  |  | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfPages.maxValue |  |  |  | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfPages.minValue |  |  |  | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfReferences.maxValue |  |  |  | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfReferences.minValue |  |  |  | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfTables.maxValue |  |  |  | UNMAPPED |
| C.OUTPUT.ThesisPhysicalDescription.NumberOfTables.minValue |  |  |  | UNMAPPED |
| C.ACTIVITY.Involvement.FromDate.maxDate |  |  |  | UNMAPPED |
| C.ACTIVITY.Involvement.FromDate.minDate |  |  |  | UNMAPPED |
| C.ACTIVITY.Involvement.FromDate.presence |  |  |  | UNMAPPED |
| C.ACTIVITY.Involvement.ResearchAreas.presence |  |  |  | UNMAPPED |
| C.ACTIVITY.Involvement.ResearchAreas.vocabulary |  |  |  | UNMAPPED |
| C.ACTIVITY.Involvement.ToDate.minDate |  |  |  | UNMAPPED |
| C.ACTIVITY.Involvement.ToDate.presence |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonContribution.FromDate.maxDate |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonContribution.FromDate.minDate |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonContribution.FromDate.presence |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonContribution.ResearchAreas.presence |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonContribution.ResearchAreas.vocabulary |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonContribution.ToDate.minDate |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonContribution.ToDate.presence |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonDocumentContribution.IsCorrespondingContributor.custom |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonDocumentContribution.IsCorrespondingContributor.vocabulary |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonDocumentContribution.IsMainContributor.custom |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonDocumentContribution.IsMainContributor.vocabulary |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonDocumentContribution.Person.custom |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonEventContribution.Case.custom |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonEventContribution.LabHoursPerWeek.custom |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonEventContribution.LectureHoursPerWeek.custom |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonEventContribution.LocationJurisdiction.custom |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment.custom |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment.maxValue |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment.minValue |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonEventContribution.OtherContactHoursPerWeek.custom |  |  |  | UNMAPPED |
| C.ACTIVITY.PersonEventContribution.TutorialHoursPerWeek.custom |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.ContactEmail.maxLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.ContactEmail.minLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.ContactEmail.pattern |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.FaxNumber.maxLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.FaxNumber.minLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.FaxNumber.pattern |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.MobilePhoneNumber.maxLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.MobilePhoneNumber.minLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.MobilePhoneNumber.pattern |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.PhoneNumber.maxLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.PhoneNumber.minLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Contact.PhoneNumber.pattern |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Country.Code.maxLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Country.Code.minLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Country.Code.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Country.Code.unique |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Country.Code.vocabulary | PTCRIS.SEMANTIC | PTCRIS-F1-01DSEMANT | GR.PTCRIS_F1_01DSEMANT.standardized_geopolitical_country_coding | FULL |
| C.SHARED_COMPONENTS.Currency.Code.maxLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Currency.Code.minLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Currency.Code.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Currency.Code.pattern |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Currency.Code.unique |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Currency.Code.vocabulary |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Currency.Symbol.maxLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Currency.Symbol.minLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Currency.Symbol.vocabulary |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue.custom |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.EntityIndicator.Subclass.custom |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.Day.custom |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.Day.maxValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.Day.minValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.Day.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.Month.maxValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.Month.minValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.Month.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.TextYear.custom |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.TextYear.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.Year.maxValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.Year.minValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.FlexibleDate.Year.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.GeoLocation.Address.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.GeoLocation.Latitude.maxValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.GeoLocation.Latitude.minValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.GeoLocation.Latitude.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.GeoLocation.Longitude.maxValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.GeoLocation.Longitude.minValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.GeoLocation.Longitude.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Identifier.RegularExpression.custom |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Identifier.RegularExpression.maxLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Identifier.RegularExpression.minLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Identifier.RegularExpression.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Language.LanguageCode.maxLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Language.LanguageCode.minLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Language.LanguageCode.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Language.LanguageCode.pattern |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Language.LanguageCode.unique |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.Language.LanguageCode.vocabulary |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.LanguageTag.LanguageTag.maxLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.LanguageTag.LanguageTag.minLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.LanguageTag.LanguageTag.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.LanguageTag.LanguageTag.pattern |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.LanguageTag.LanguageTag.unique |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.LanguageTag.LanguageTag.vocabulary |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.MonetaryAmount.Amount.maxValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.MonetaryAmount.Amount.minValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.MonetaryAmount.Amount.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.Height.maxValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.Height.minValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.Height.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset.maxValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset.minValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset.maxValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset.minValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.Width.maxValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.Width.minValue |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.ProfilePhotoOrLogo.Width.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.ResearchArea.Name.maxLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.ResearchArea.Name.minLength |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.ResearchArea.Name.presence |  |  |  | UNMAPPED |
| C.SHARED_COMPONENTS.ResearchArea.Name.vocabulary |  |  |  | UNMAPPED |
