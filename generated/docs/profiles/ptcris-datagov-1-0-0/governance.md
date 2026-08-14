# Governance alignment — PTCRIS-DATAGOV-1.0.0

## PTCRIS Data Governance dimensions

| Dimension | Metric | Description |
|---|---|---|
| Accuracy | PTCRIS-F1-01DACURR | Ensures that data elements support acceptable data values and prevents unwanted or out-of-scope values. |
| Consistency | PTCRIS-F1-01DCONSIST | Requires data elements to conform to defined presentation formats and defined handling of absent values. |
| Lineage | PTCRIS-F1-01DLINEAGE | Requires source and date provenance attributes so that data origin and audit trails are preserved. |
| Structural Consistency | PTCRIS-F1-01DSTRUCT | Requires conformity with enterprise length and type standards without semantic shifts in stored representations. |
| Qualitative | PTCRIS-F1-01DQUALIT | Requires authoritative references for definition/reference data and appropriate identifier assignment. |
| Semantic | PTCRIS-F1-01DSEMANT | Requires standard naming conventions and standard terms aligned with business concepts. |
| Currency | PTCRIS-F1-01DCURREN | Addresses temporal consistency, expired lifetimes and chronological dependency rules. |

## Governance requirements and implemented rules

| Requirement | Metric | Dimension | Implementing artefacts | Review required |
|---|---|---|---|---|
| GR.PTCRIS_F1_01DSTRUCT.standardized_citation_name_format_verification | PTCRIS-F1-01DSTRUCT | PTCRIS.STRUCTURAL_CONSISTENCY | RULE.PERSON.PersonName.Lastname | False |
| GR.PTCRIS_F1_01DACURR.full_name_presence_and_length_validation | PTCRIS-F1-01DACURR | PTCRIS.ACCURACY | RULE.PERSON.Person.Name, RULE.PERSON.PersonName.Lastname | False |
| GR.PTCRIS_F1_01DSEMANT.standardized_geopolitical_country_coding | PTCRIS-F1-01DSEMANT | PTCRIS.SEMANTIC | RULE.SHARED_COMPONENTS.Country.Code | False |
| GR.PTCRIS_F1_01DSEMANT.gender_classification_conformity | PTCRIS-F1-01DSEMANT | PTCRIS.SEMANTIC | RULE.PERSON.PersonalInfo.Sex | False |
| GR.PTCRIS_F1_01DCURREN.minor_underage_researcher_validation | PTCRIS-F1-01DCURREN | PTCRIS.CURRENCY | RULE.PERSON.PersonalInfo.BirthDate | False |
| GR.PTCRIS_F1_01DCONSIST.non_existent_or_futuristic_birth_date_restriction | PTCRIS-F1-01DCONSIST | PTCRIS.CONSISTENCY | RULE.PERSON.PersonalInfo.BirthDate | False |
| GR.PTCRIS_F1_01DSTRUCT.open_researcher_and_contributor_id_orcid_format_verification | PTCRIS-F1-01DSTRUCT | PTCRIS.STRUCTURAL_CONSISTENCY | RULE.PERSON.Person.Orcid | False |
| GR.PTCRIS_F1_01DSTRUCT.web_of_science_researcher_id_format_validation | PTCRIS-F1-01DSTRUCT | PTCRIS.STRUCTURAL_CONSISTENCY | RULE.PERSON.Person.WebOfScienceResearcherId | False |
| GR.PTCRIS_F1_01DSTRUCT.scopus_author_id_format_validation | PTCRIS-F1-01DSTRUCT | PTCRIS.STRUCTURAL_CONSISTENCY | RULE.PERSON.Person.ScopusAuthorId | False |
| GR.PTCRIS_F1_01DACURR.global_uniqueness_of_orcid_allocation | PTCRIS-F1-01DACURR | PTCRIS.ACCURACY | RULE.PERSON.Person.Orcid | False |
| GR.PTCRIS_F1_01DACURR.global_uniqueness_of_science_id_allocation | PTCRIS-F1-01DACURR | PTCRIS.ACCURACY | RULE.PERSON.Person.NationalIdCienciaId | False |
| GR.PTCRIS_F1_01DCURREN.mandatory_start_date_of_professional_career | PTCRIS-F1-01DCURREN | PTCRIS.CURRENCY | RULE.PERSON.Person.Involvements | False |
| GR.PTCRIS_F1_01DSTRUCT.validation_of_the_format_of_the_start_date_of_the_professional_career | PTCRIS-F1-01DSTRUCT | PTCRIS.STRUCTURAL_CONSISTENCY | RULE.PERSON.Involvement.FromDate | False |
| GR.PTCRIS_F1_01DSEMANT.type_professional_path_classification_validation | PTCRIS-F1-01DSEMANT | PTCRIS.SEMANTIC | RULE.PERSON.Employment.EmploymentPositionHierarchy | False |
| GR.PTCRIS_F1_01DSTRUCT.format_validation_for_award_title_name | PTCRIS-F1-01DSTRUCT | PTCRIS.STRUCTURAL_CONSISTENCY | RULE.FUNDING.Funding.Name | False |
| GR.PTCRIS_F1_01DCURREN.award_year_required_verification | PTCRIS-F1-01DCURREN | PTCRIS.CURRENCY | RULE.FUNDING.Funding.DateAwarded | False |
| GR.PTCRIS_F1_01DCONSIST.project_title_presence_requirement | PTCRIS-F1-01DCONSIST | PTCRIS.CONSISTENCY | RULE.PROJECT.Project.Name | False |
| GR.PTCRIS_F1_01DACURR.project_without_at_least_one_identifier | PTCRIS-F1-01DACURR | PTCRIS.ACCURACY | RULE.PROJECT.Project.Identifiers | False |
| GR.PTCRIS_F1_01DCURREN.mandatory_project_boundary_dates | PTCRIS-F1-01DCURREN | PTCRIS.CURRENCY | RULE.PROJECT.Project.FromDate, RULE.PROJECT.Project.ToDate | False |
| GR.PTCRIS_F1_01DCONSIST.negative_or_zero_funding_anomaly_detection | PTCRIS-F1-01DCONSIST | PTCRIS.CONSISTENCY | RULE.SHARED_COMPONENTS.MonetaryAmount.Amount | False |
| GR.PTCRIS_F1_01DCONSIST.sum_of_organizations_funding_greater_than_project_total | PTCRIS-F1-01DCONSIST | PTCRIS.CONSISTENCY | RULE.PROJECT.Project.Organisations | False |
| GR.PTCRIS_F1_01DCONSIST.different_funding_ids_in_project_and_funding | PTCRIS-F1-01DCONSIST | PTCRIS.CONSISTENCY | RULE.PROJECT.Project.Fundings | False |
| GR.PTCRIS_F1_01DCURREN.project_funding_with_suspicious_start_date | PTCRIS-F1-01DCURREN | PTCRIS.CURRENCY | RULE.FUNDING.Funding.FromDate | False |
| GR.PTCRIS_F1_01DCURREN.project_funding_with_suspected_end_date | PTCRIS-F1-01DCURREN | PTCRIS.CURRENCY | RULE.FUNDING.Funding.ToDate | False |
| GR..project_with_coordinating_organization_but_no_other_participants |  |  |  | False |
| GR.PTCRIS_F1_01DSTRUCT.project_with_associated_organizations_but_no_coordinator | PTCRIS-F1-01DSTRUCT | PTCRIS.STRUCTURAL_CONSISTENCY | RULE.PROJECT.Project.Organisations | False |
| GR.PTCRIS_F1_01DSTRUCT.project_with_team_but_no_principal_investigator | PTCRIS-F1-01DSTRUCT | PTCRIS.STRUCTURAL_CONSISTENCY | RULE.PROJECT.Project.Team | False |
| GR.PTCRIS_F1_01DSEMANT.ontological_disjointness_rejection_constraint | PTCRIS-F1-01DSEMANT | PTCRIS.SEMANTIC |  | False |
| GR.PTCRIS_F1_01DSEMANT.axiomatic_graph_clustering_directive | PTCRIS-F1-01DSEMANT | PTCRIS.SEMANTIC |  | False |
| GR.PTCRIS_F1_01DACURR.hierarchical_name_specificity_conflict_resolution | PTCRIS-F1-01DACURR | PTCRIS.ACCURACY |  | False |
| GR.PTCRIS_F1_01DCONSIST.topological_coauthor_splitting_constraint | PTCRIS-F1-01DCONSIST | PTCRIS.CONSISTENCY |  | False |
| GR.PTCRIS_F1_01DSEMANT.organizational_hierarchy_decomposition_and_abbreviation_expansion | PTCRIS-F1-01DSEMANT | PTCRIS.SEMANTIC |  | False |
| GR.PTCRIS_F1_01DACURR.affiliation_levenshtein_distance_boundary | PTCRIS-F1-01DACURR | PTCRIS.ACCURACY |  | False |
| GR.PTCRIS_F1_01DQUALIT.canonical_uri_and_functional_property_priority_selection | PTCRIS-F1-01DQUALIT | PTCRIS.QUALITATIVE |  | False |
| GR.PTCRIS_F1_01DLINEAGE.erroneous_re_ingest_prevention_via_trace_logging | PTCRIS-F1-01DLINEAGE | PTCRIS.LINEAGE |  | False |
| GR.PTCRIS_F1_01DSTRUCT.doi_format_verification | PTCRIS-F1-01DSTRUCT | PTCRIS.STRUCTURAL_CONSISTENCY | RULE.FUNDING.Funding.Doi, RULE.OUTPUT.Document.Doi, RULE.PROJECT.Project.Doi | True |
| GR.PTCRIS_F1_01DACURR.global_uniqueness_of_doi_allocation | PTCRIS-F1-01DACURR | PTCRIS.ACCURACY | RULE.FUNDING.Funding.Doi, RULE.OUTPUT.Document.Doi, RULE.PROJECT.Project.Doi | True |
| GR.PTCRIS_F1_A1.resolvable_doi | PTCRIS-F1, A1 |  | RULE.FUNDING.Funding.Doi, RULE.OUTPUT.Document.Doi, RULE.PROJECT.Project.Doi | True |
| GR.PTCRIS_F1_01DSTRUCT.pid_format_verification | PTCRIS-F1-01DSTRUCT | PTCRIS.STRUCTURAL_CONSISTENCY | RULE.FUNDING.Funding.ProjectReferenceIdGrantAgreementId, RULE.PROJECT.Project.NationalIdProjectReference | True |
| GR.PTCRIS_F1_01DACURR.global_uniqueness_of_pid_allocation | PTCRIS-F1-01DACURR | PTCRIS.ACCURACY | RULE.FUNDING.Funding.ProjectReferenceIdGrantAgreementId, RULE.PROJECT.Project.NationalIdProjectReference | True |
| GR.PTCRIS_FsF_F2_01M.metric_requirement | PTCRIS-FsF-F2-01M |  | RULE.FUNDING.Funding.Description, RULE.ORGANISATION_UNIT.OrganisationUnit.Description, RULE.OUTPUT.Document.Description, RULE.PERSON.Person.Biography, RULE.PROJECT.Project.Description | True |
| GR.PTCRIS_FsF_R1_1_01M.metric_requirement | PTCRIS-FsF-R1.1-01M |  | RULE.FUNDING.Funding.MetadataLicense, RULE.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense, RULE.OUTPUT.Document.MetadataLicense, RULE.PERSON.Person.MetadataLicense, RULE.PROJECT.Project.MetadataLicense | True |
| GR.PTCRIS_FsF_A1_01M.metric_requirement | PTCRIS-FsF-A1-01M |  | RULE.FUNDING.Funding.MetadataAccessLevel, RULE.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel, RULE.OUTPUT.Document.MetadataAccessLevel, RULE.PERSON.Person.MetadataAccessLevel, RULE.PROJECT.Project.MetadataAccessLevel | True |
| GR.PTCRIS_F1_01DLINEAGE.metric_requirement | PTCRIS-F1-01DLINEAGE | PTCRIS.LINEAGE | RULE.FUNDING.Funding.CreateDate, RULE.FUNDING.Funding.LastModificationDate, RULE.ORGANISATION_UNIT.OrganisationUnit.CreateDate, RULE.ORGANISATION_UNIT.OrganisationUnit.LastModificationDate, RULE.OUTPUT.Document.CreateDate, RULE.OUTPUT.Document.LastModificationDate, RULE.PERSON.Person.CreateDate, RULE.PERSON.Person.LastModificationDate, RULE.PROJECT.Project.CreateDate, RULE.PROJECT.Project.LastModificationDate | True |
| GR.PTCRIS_F1_01DSTRUCT.raid_format_verification | PTCRIS-F1-01DSTRUCT | PTCRIS.STRUCTURAL_CONSISTENCY | RULE.PROJECT.Project.Raid | True |
| GR.PTCRIS_F1_01DACURR.global_uniqueness_of_raid_allocation | PTCRIS-F1-01DACURR | PTCRIS.ACCURACY | RULE.PROJECT.Project.Raid | True |
| GR.PTCRIS_F1_A1.resolvable_raid | PTCRIS-F1, A1 |  | RULE.PROJECT.Project.Raid | True |
| GR.PTCRIS_F1_01DCONSIST.semantic_iri_url_validation | PTCRIS-F1-01DCONSIST | PTCRIS.CONSISTENCY | RULE.PROJECT.Project.ResearchAreas | True |
| GR.PTCRIS_F1_01DSTRUCT.project_with_coordinating_organization_but_no_other_participants | PTCRIS-F1-01DSTRUCT | PTCRIS.STRUCTURAL_CONSISTENCY | RULE.PROJECT.Project.Organisations | True |
| GR.PTCRIS_F1_01DCONSIST.sum_of_linked_fundings_amounts | PTCRIS-F1-01DCONSIST | PTCRIS.CONSISTENCY | RULE.PROJECT.Project.Costs | True |
| GR.PTCRIS_F1_A1.resolvable_pid | PTCRIS-F1, A1 |  | RULE.PERSON.Person.Orcid | True |
| GR.PTCRIS_F1_01DACURR.metric_requirement | PTCRIS-F1-01DACURR | PTCRIS.ACCURACY | RULE.PERSON.Person.AuthenticusId, RULE.PERSON.Person.LattesId, RULE.PERSON.Person.OpenAlexId, RULE.PERSON.Person.ScholarId, RULE.PERSON.Person.ScopusAuthorId, RULE.PERSON.Person.WebOfScienceResearcherId | True |
| GR.PTCRIS_F1_01DSTRUCT.metric_requirement | PTCRIS-F1-01DSTRUCT | PTCRIS.STRUCTURAL_CONSISTENCY | RULE.PERSON.Person.AuthenticusId, RULE.PERSON.Person.LattesId, RULE.PERSON.Person.NationalIdCienciaId, RULE.PERSON.Person.OpenAlexId, RULE.PERSON.Person.ScholarId | True |
| GR.PTCRIS_DQ_F1_01IDUNIQ.metric_requirement | PTCRIS-DQ-F1-01IDUNIQ |  | RULE.PERSON.Person.NationalIdCienciaId | True |
| GR.PTCRIS_F1_01DSTRUCT.handle_format_verification | PTCRIS-F1-01DSTRUCT | PTCRIS.STRUCTURAL_CONSISTENCY | RULE.OUTPUT.Document.Handle | True |
| GR.PTCRIS_F1_01DACURR.global_uniqueness_of_handle_allocation | PTCRIS-F1-01DACURR | PTCRIS.ACCURACY | RULE.OUTPUT.Document.Handle | True |
| GR.PTCRIS_F1_A1.resolvable_handle | PTCRIS-F1, A1 |  | RULE.OUTPUT.Document.Handle | True |
