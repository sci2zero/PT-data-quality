# Governance traceability — PTCRIS-DATAGOV-1.0.0

| Domain | Constraint | Validation target | Dimension | Metric | Requirement | Status |
|---|---|---|---|---|---|---|
| ACTIVITY | C.ACTIVITY.Involvement.FromDate.maxDate | VT.ACTIVITY.Involvement.FromDate |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.Involvement.FromDate.minDate | VT.ACTIVITY.Involvement.FromDate |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.Involvement.FromDate.presence | VT.ACTIVITY.Involvement.FromDate |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.Involvement.ResearchAreas.presence | VT.ACTIVITY.Involvement.ResearchAreas |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.Involvement.ResearchAreas.vocabulary | VT.ACTIVITY.Involvement.ResearchAreas |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.Involvement.ToDate.minDate | VT.ACTIVITY.Involvement.ToDate |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.Involvement.ToDate.presence | VT.ACTIVITY.Involvement.ToDate |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonContribution.FromDate.maxDate | VT.ACTIVITY.PersonContribution.FromDate |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonContribution.FromDate.minDate | VT.ACTIVITY.PersonContribution.FromDate |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonContribution.FromDate.presence | VT.ACTIVITY.PersonContribution.FromDate |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonContribution.ResearchAreas.presence | VT.ACTIVITY.PersonContribution.ResearchAreas |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonContribution.ResearchAreas.vocabulary | VT.ACTIVITY.PersonContribution.ResearchAreas |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonContribution.ToDate.minDate | VT.ACTIVITY.PersonContribution.ToDate |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonContribution.ToDate.presence | VT.ACTIVITY.PersonContribution.ToDate |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonDocumentContribution.IsCorrespondingContributor.custom | VT.ACTIVITY.PersonDocumentContribution.IsCorrespondingContributor |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonDocumentContribution.IsCorrespondingContributor.vocabulary | VT.ACTIVITY.PersonDocumentContribution.IsCorrespondingContributor |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonDocumentContribution.IsMainContributor.custom | VT.ACTIVITY.PersonDocumentContribution.IsMainContributor |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonDocumentContribution.IsMainContributor.vocabulary | VT.ACTIVITY.PersonDocumentContribution.IsMainContributor |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonDocumentContribution.Person.custom | VT.ACTIVITY.PersonDocumentContribution.Person |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonEventContribution.Case.custom | VT.ACTIVITY.PersonEventContribution.Case |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonEventContribution.LabHoursPerWeek.custom | VT.ACTIVITY.PersonEventContribution.LabHoursPerWeek |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonEventContribution.LectureHoursPerWeek.custom | VT.ACTIVITY.PersonEventContribution.LectureHoursPerWeek |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonEventContribution.LocationJurisdiction.custom | VT.ACTIVITY.PersonEventContribution.LocationJurisdiction |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment.custom | VT.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment.maxValue | VT.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment.minValue | VT.ACTIVITY.PersonEventContribution.NumberOfReviewsOrAssessment |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonEventContribution.OtherContactHoursPerWeek.custom | VT.ACTIVITY.PersonEventContribution.OtherContactHoursPerWeek |  |  |  | UNMAPPED |
| ACTIVITY | C.ACTIVITY.PersonEventContribution.TutorialHoursPerWeek.custom | VT.ACTIVITY.PersonEventContribution.TutorialHoursPerWeek |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.Amount.presence | VT.FUNDING.Funding.Amount |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.CreateDate.presence | VT.FUNDING.Funding.CreateDate | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| FUNDING | C.FUNDING.Funding.DateAwarded.maxDate | VT.FUNDING.Funding.DateAwarded |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.DateAwarded.minDate | VT.FUNDING.Funding.DateAwarded |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.DateAwarded.presence | VT.FUNDING.Funding.DateAwarded | PTCRIS.CURRENCY | PTCRIS-F1-01DCURREN | GR.PTCRIS_F1_01DCURREN.award_year_required_verification | FULL |
| FUNDING | C.FUNDING.Funding.DateSubmitted.maxDate | VT.FUNDING.Funding.DateSubmitted |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.DateSubmitted.minDate | VT.FUNDING.Funding.DateSubmitted |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.Description.minLength | VT.FUNDING.Funding.Description |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| FUNDING | C.FUNDING.Funding.Description.presence | VT.FUNDING.Funding.Description |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| FUNDING | C.FUNDING.Funding.Doi.maxLength | VT.FUNDING.Funding.Doi |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.Doi.minLength | VT.FUNDING.Funding.Doi |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.Doi.pattern | VT.FUNDING.Funding.Doi | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.doi_format_verification | FULL |
| FUNDING | C.FUNDING.Funding.Doi.presence | VT.FUNDING.Funding.Doi |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.Doi.resolvable | VT.FUNDING.Funding.Doi |  | PTCRIS-F1, A1 | GR.PTCRIS_F1_A1.resolvable_doi | FULL |
| FUNDING | C.FUNDING.Funding.Doi.unique | VT.FUNDING.Funding.Doi | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_doi_allocation | FULL |
| FUNDING | C.FUNDING.Funding.FromDate.maxDate | VT.FUNDING.Funding.FromDate | PTCRIS.CURRENCY | PTCRIS-F1-01DCURREN | GR.PTCRIS_F1_01DCURREN.project_funding_with_suspicious_start_date | FULL |
| FUNDING | C.FUNDING.Funding.FromDate.minDate | VT.FUNDING.Funding.FromDate | PTCRIS.CURRENCY | PTCRIS-F1-01DCURREN | GR.PTCRIS_F1_01DCURREN.project_funding_with_suspicious_start_date | FULL |
| FUNDING | C.FUNDING.Funding.FromDate.presence | VT.FUNDING.Funding.FromDate |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.Identifiers.minCardinality | VT.FUNDING.Funding.Identifiers |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.Identifiers.presence | VT.FUNDING.Funding.Identifiers |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.LastModificationDate.presence | VT.FUNDING.Funding.LastModificationDate | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| FUNDING | C.FUNDING.Funding.MetadataAccessLevel.presence | VT.FUNDING.Funding.MetadataAccessLevel |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| FUNDING | C.FUNDING.Funding.MetadataAccessLevel.vocabulary | VT.FUNDING.Funding.MetadataAccessLevel |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| FUNDING | C.FUNDING.Funding.MetadataLicense.presence | VT.FUNDING.Funding.MetadataLicense |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| FUNDING | C.FUNDING.Funding.MetadataLicense.vocabulary | VT.FUNDING.Funding.MetadataLicense |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| FUNDING | C.FUNDING.Funding.Name.maxLength | VT.FUNDING.Funding.Name |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.Name.minLength | VT.FUNDING.Funding.Name |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.Name.pattern | VT.FUNDING.Funding.Name | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.format_validation_for_award_title_name | FULL |
| FUNDING | C.FUNDING.Funding.Name.presence | VT.FUNDING.Funding.Name |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.ProjectInvolvement.custom | VT.FUNDING.Funding.ProjectInvolvement |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.ProjectInvolvement.minCardinality | VT.FUNDING.Funding.ProjectInvolvement |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.ProjectInvolvement.presence | VT.FUNDING.Funding.ProjectInvolvement |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.ProjectReferenceId.maxLength | VT.FUNDING.Funding.ProjectReferenceId |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.ProjectReferenceId.minLength | VT.FUNDING.Funding.ProjectReferenceId |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.ProjectReferenceId.presence | VT.FUNDING.Funding.ProjectReferenceId |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.ProjectReferenceId.unique | VT.FUNDING.Funding.ProjectReferenceId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_pid_allocation | FULL |
| FUNDING | C.FUNDING.Funding.ResearchAreas.presence | VT.FUNDING.Funding.ResearchAreas |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.ResearchAreas.vocabulary | VT.FUNDING.Funding.ResearchAreas |  |  |  | UNMAPPED |
| FUNDING | C.FUNDING.Funding.ToDate.maxDate | VT.FUNDING.Funding.ToDate | PTCRIS.CURRENCY | PTCRIS-F1-01DCURREN | GR.PTCRIS_F1_01DCURREN.project_funding_with_suspicious_start_date | FULL |
| FUNDING | C.FUNDING.Funding.ToDate.minDate | VT.FUNDING.Funding.ToDate | PTCRIS.CURRENCY | PTCRIS-F1-01DCURREN | GR.PTCRIS_F1_01DCURREN.project_funding_with_suspicious_start_date | FULL |
| FUNDING | C.FUNDING.Funding.ToDate.presence | VT.FUNDING.Funding.ToDate |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Active.vocabulary | VT.ORGANISATION_UNIT.OrganisationUnit.Active |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.CreateDate.presence | VT.ORGANISATION_UNIT.OrganisationUnit.CreateDate | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.DateDissolved.maxDate | VT.ORGANISATION_UNIT.OrganisationUnit.DateDissolved |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.DateDissolved.minDate | VT.ORGANISATION_UNIT.OrganisationUnit.DateDissolved |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.DateEstablished.maxDate | VT.ORGANISATION_UNIT.OrganisationUnit.DateEstablished |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.DateEstablished.presence | VT.ORGANISATION_UNIT.OrganisationUnit.DateEstablished |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Description.minLength | VT.ORGANISATION_UNIT.OrganisationUnit.Description |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Description.presence | VT.ORGANISATION_UNIT.OrganisationUnit.Description |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Fundref.maxLength | VT.ORGANISATION_UNIT.OrganisationUnit.Fundref |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Fundref.minLength | VT.ORGANISATION_UNIT.OrganisationUnit.Fundref |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Fundref.pattern | VT.ORGANISATION_UNIT.OrganisationUnit.Fundref |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Fundref.unique | VT.ORGANISATION_UNIT.OrganisationUnit.Fundref |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Grid.maxLength | VT.ORGANISATION_UNIT.OrganisationUnit.Grid |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Grid.minLength | VT.ORGANISATION_UNIT.OrganisationUnit.Grid |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Grid.pattern | VT.ORGANISATION_UNIT.OrganisationUnit.Grid |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Grid.unique | VT.ORGANISATION_UNIT.OrganisationUnit.Grid |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Isni.maxLength | VT.ORGANISATION_UNIT.OrganisationUnit.Isni |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Isni.minLength | VT.ORGANISATION_UNIT.OrganisationUnit.Isni |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Isni.pattern | VT.ORGANISATION_UNIT.OrganisationUnit.Isni |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Isni.unique | VT.ORGANISATION_UNIT.OrganisationUnit.Isni |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.LastModificationDate.presence | VT.ORGANISATION_UNIT.OrganisationUnit.LastModificationDate | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel.presence | VT.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel.vocabulary | VT.ORGANISATION_UNIT.OrganisationUnit.MetadataAccessLevel |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense.presence | VT.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense.vocabulary | VT.ORGANISATION_UNIT.OrganisationUnit.MetadataLicense |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Name.maxLength | VT.ORGANISATION_UNIT.OrganisationUnit.Name |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Name.minLength | VT.ORGANISATION_UNIT.OrganisationUnit.Name |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Name.pattern | VT.ORGANISATION_UNIT.OrganisationUnit.Name |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Name.presence | VT.ORGANISATION_UNIT.OrganisationUnit.Name |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId.maxLength | VT.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId.minLength | VT.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId.pattern | VT.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId.unique | VT.ORGANISATION_UNIT.OrganisationUnit.OpenAlexId |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Ringgold.maxLength | VT.ORGANISATION_UNIT.OrganisationUnit.Ringgold |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Ringgold.minLength | VT.ORGANISATION_UNIT.OrganisationUnit.Ringgold |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Ringgold.pattern | VT.ORGANISATION_UNIT.OrganisationUnit.Ringgold |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Ringgold.unique | VT.ORGANISATION_UNIT.OrganisationUnit.Ringgold |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Ror.maxLength | VT.ORGANISATION_UNIT.OrganisationUnit.Ror |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Ror.minLength | VT.ORGANISATION_UNIT.OrganisationUnit.Ror |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Ror.pattern | VT.ORGANISATION_UNIT.OrganisationUnit.Ror |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Ror.presence | VT.ORGANISATION_UNIT.OrganisationUnit.Ror |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Ror.unique | VT.ORGANISATION_UNIT.OrganisationUnit.Ror |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.RorIsni.presence | VT.ORGANISATION_UNIT.OrganisationUnit.RorIsni |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.RorIsni.unique | VT.ORGANISATION_UNIT.OrganisationUnit.RorIsni |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid.maxLength | VT.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid.minLength | VT.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid.pattern | VT.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid.unique | VT.ORGANISATION_UNIT.OrganisationUnit.ScopusAfid |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Sector.presence | VT.ORGANISATION_UNIT.OrganisationUnit.Sector |  |  |  | UNMAPPED |
| ORGANISATION_UNIT | C.ORGANISATION_UNIT.OrganisationUnit.Sector.vocabulary | VT.ORGANISATION_UNIT.OrganisationUnit.Sector |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.Contributors.custom | VT.OUTPUT.Document.Contributors |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.Contributors.minCardinality | VT.OUTPUT.Document.Contributors |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.Contributors.presence | VT.OUTPUT.Document.Contributors |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.CreateDate.presence | VT.OUTPUT.Document.CreateDate | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| OUTPUT | C.OUTPUT.Document.Description.minLength | VT.OUTPUT.Document.Description |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| OUTPUT | C.OUTPUT.Document.Description.presence | VT.OUTPUT.Document.Description |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| OUTPUT | C.OUTPUT.Document.DocumentDate.maxDate | VT.OUTPUT.Document.DocumentDate |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.DocumentDate.minDate | VT.OUTPUT.Document.DocumentDate |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.DocumentDate.presence | VT.OUTPUT.Document.DocumentDate |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.Doi.maxLength | VT.OUTPUT.Document.Doi |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.Doi.minLength | VT.OUTPUT.Document.Doi |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.Doi.pattern | VT.OUTPUT.Document.Doi | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.doi_format_verification | FULL |
| OUTPUT | C.OUTPUT.Document.Doi.presence | VT.OUTPUT.Document.Doi |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.Doi.resolvable | VT.OUTPUT.Document.Doi |  | PTCRIS-F1, A1 | GR.PTCRIS_F1_A1.resolvable_doi | FULL |
| OUTPUT | C.OUTPUT.Document.Doi.unique | VT.OUTPUT.Document.Doi | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_doi_allocation | FULL |
| OUTPUT | C.OUTPUT.Document.Handle.maxLength | VT.OUTPUT.Document.Handle |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.Handle.minLength | VT.OUTPUT.Document.Handle |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.Handle.pattern | VT.OUTPUT.Document.Handle | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.handle_format_verification | FULL |
| OUTPUT | C.OUTPUT.Document.Handle.presence | VT.OUTPUT.Document.Handle |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.Handle.resolvable | VT.OUTPUT.Document.Handle |  | PTCRIS-F1, A1 | GR.PTCRIS_F1_A1.resolvable_handle | FULL |
| OUTPUT | C.OUTPUT.Document.Handle.unique | VT.OUTPUT.Document.Handle | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_handle_allocation | FULL |
| OUTPUT | C.OUTPUT.Document.Identifiers.minCardinality | VT.OUTPUT.Document.Identifiers |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.Identifiers.presence | VT.OUTPUT.Document.Identifiers |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.Identifiers.unique | VT.OUTPUT.Document.Identifiers |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.LastModificationDate.presence | VT.OUTPUT.Document.LastModificationDate | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| OUTPUT | C.OUTPUT.Document.MetadataAccessLevel.presence | VT.OUTPUT.Document.MetadataAccessLevel |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| OUTPUT | C.OUTPUT.Document.MetadataAccessLevel.vocabulary | VT.OUTPUT.Document.MetadataAccessLevel |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| OUTPUT | C.OUTPUT.Document.MetadataLicense.presence | VT.OUTPUT.Document.MetadataLicense |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| OUTPUT | C.OUTPUT.Document.MetadataLicense.vocabulary | VT.OUTPUT.Document.MetadataLicense |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| OUTPUT | C.OUTPUT.Document.OpenAccess.presence | VT.OUTPUT.Document.OpenAccess |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.OpenAccess.vocabulary | VT.OUTPUT.Document.OpenAccess |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.ResearchAreas.presence | VT.OUTPUT.Document.ResearchAreas |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.ResearchAreas.vocabulary | VT.OUTPUT.Document.ResearchAreas |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.Title.maxLength | VT.OUTPUT.Document.Title |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.Title.minLength | VT.OUTPUT.Document.Title |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.Title.pattern | VT.OUTPUT.Document.Title |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Document.Title.presence | VT.OUTPUT.Document.Title |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.IntellectualProperty.DateEndTerm.minDate | VT.OUTPUT.IntellectualProperty.DateEndTerm |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.IntellectualProperty.DateEndTerm.presence | VT.OUTPUT.IntellectualProperty.DateEndTerm |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.IntellectualProperty.DateFilingPriority.maxDate | VT.OUTPUT.IntellectualProperty.DateFilingPriority |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.IntellectualProperty.DateFilingPriority.minDate | VT.OUTPUT.IntellectualProperty.DateFilingPriority |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.IntellectualProperty.DateFilingPriority.presence | VT.OUTPUT.IntellectualProperty.DateFilingPriority |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.IntellectualProperty.DateRequested.maxDate | VT.OUTPUT.IntellectualProperty.DateRequested |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.IntellectualProperty.DateRequested.minDate | VT.OUTPUT.IntellectualProperty.DateRequested |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.IntellectualProperty.DateRequested.presence | VT.OUTPUT.IntellectualProperty.DateRequested |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.PublicationSeriesPublisher.FromDate.maxDate | VT.OUTPUT.PublicationSeriesPublisher.FromDate |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.PublicationSeriesPublisher.FromDate.minDate | VT.OUTPUT.PublicationSeriesPublisher.FromDate |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.PublicationSeriesPublisher.FromDate.presence | VT.OUTPUT.PublicationSeriesPublisher.FromDate |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.PublicationSeriesPublisher.ToDate.minDate | VT.OUTPUT.PublicationSeriesPublisher.ToDate |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.PublicationUnit.NumberOfPages.maxValue | VT.OUTPUT.PublicationUnit.NumberOfPages |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.PublicationUnit.NumberOfPages.minValue | VT.OUTPUT.PublicationUnit.NumberOfPages |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.PublicationUnitPart.NumberOfPages.maxValue | VT.OUTPUT.PublicationUnitPart.NumberOfPages |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.PublicationUnitPart.NumberOfPages.minValue | VT.OUTPUT.PublicationUnitPart.NumberOfPages |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Thesis.ThesisDefenceDate.maxDate | VT.OUTPUT.Thesis.ThesisDefenceDate |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Thesis.ThesisDefenceDate.minDate | VT.OUTPUT.Thesis.ThesisDefenceDate |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Thesis.ThesisDefenceDate.presence | VT.OUTPUT.Thesis.ThesisDefenceDate |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Thesis.TopicAcceptanceDate.maxDate | VT.OUTPUT.Thesis.TopicAcceptanceDate |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Thesis.TopicAcceptanceDate.minDate | VT.OUTPUT.Thesis.TopicAcceptanceDate |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.Thesis.TopicAcceptanceDate.presence | VT.OUTPUT.Thesis.TopicAcceptanceDate |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.ThesisPhysicalDescription.NumberOfAppendices.maxValue | VT.OUTPUT.ThesisPhysicalDescription.NumberOfAppendices |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.ThesisPhysicalDescription.NumberOfAppendices.minValue | VT.OUTPUT.ThesisPhysicalDescription.NumberOfAppendices |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.ThesisPhysicalDescription.NumberOfChapters.maxValue | VT.OUTPUT.ThesisPhysicalDescription.NumberOfChapters |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.ThesisPhysicalDescription.NumberOfChapters.minValue | VT.OUTPUT.ThesisPhysicalDescription.NumberOfChapters |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.ThesisPhysicalDescription.NumberOfGraphs.maxValue | VT.OUTPUT.ThesisPhysicalDescription.NumberOfGraphs |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.ThesisPhysicalDescription.NumberOfGraphs.minValue | VT.OUTPUT.ThesisPhysicalDescription.NumberOfGraphs |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.ThesisPhysicalDescription.NumberOfIlustrations.maxValue | VT.OUTPUT.ThesisPhysicalDescription.NumberOfIlustrations |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.ThesisPhysicalDescription.NumberOfIlustrations.minValue | VT.OUTPUT.ThesisPhysicalDescription.NumberOfIlustrations |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.ThesisPhysicalDescription.NumberOfPages.maxValue | VT.OUTPUT.ThesisPhysicalDescription.NumberOfPages |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.ThesisPhysicalDescription.NumberOfPages.minValue | VT.OUTPUT.ThesisPhysicalDescription.NumberOfPages |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.ThesisPhysicalDescription.NumberOfReferences.maxValue | VT.OUTPUT.ThesisPhysicalDescription.NumberOfReferences |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.ThesisPhysicalDescription.NumberOfReferences.minValue | VT.OUTPUT.ThesisPhysicalDescription.NumberOfReferences |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.ThesisPhysicalDescription.NumberOfTables.maxValue | VT.OUTPUT.ThesisPhysicalDescription.NumberOfTables |  |  |  | UNMAPPED |
| OUTPUT | C.OUTPUT.ThesisPhysicalDescription.NumberOfTables.minValue | VT.OUTPUT.ThesisPhysicalDescription.NumberOfTables |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Education.DegreeType.presence | VT.PERSON.Education.DegreeType |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Education.DegreeType.vocabulary | VT.PERSON.Education.DegreeType |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Education.EducationStatus.presence | VT.PERSON.Education.EducationStatus |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Education.EducationStatus.vocabulary | VT.PERSON.Education.EducationStatus |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Employment.EmploymentPositionHierarchy.presence | VT.PERSON.Employment.EmploymentPositionHierarchy |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Employment.EmploymentPositionHierarchy.vocabulary | VT.PERSON.Employment.EmploymentPositionHierarchy | PTCRIS.SEMANTIC | PTCRIS-F1-01DSEMANT | GR.PTCRIS_F1_01DSEMANT.type_professional_path_classification_validation | FULL |
| PERSON | C.PERSON.ExpertiseOrSkill.ResearchAreas.presence | VT.PERSON.ExpertiseOrSkill.ResearchAreas |  |  |  | UNMAPPED |
| PERSON | C.PERSON.ExpertiseOrSkill.ResearchAreas.vocabulary | VT.PERSON.ExpertiseOrSkill.ResearchAreas |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Involvement.FromDate.maxDate | VT.PERSON.Involvement.FromDate |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Involvement.FromDate.minDate | VT.PERSON.Involvement.FromDate |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Involvement.FromDate.presence | VT.PERSON.Involvement.FromDate |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Involvement.FundingPartsFunding.custom | VT.PERSON.Involvement.FundingPartsFunding |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Involvement.InvolvementType.presence | VT.PERSON.Involvement.InvolvementType |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Involvement.InvolvementType.vocabulary | VT.PERSON.Involvement.InvolvementType |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Involvement.ToDate.maxDate | VT.PERSON.Involvement.ToDate |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Involvement.ToDate.minDate | VT.PERSON.Involvement.ToDate |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.AcademicReview.maxLength | VT.PERSON.LanguageKnowledge.AcademicReview |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.AcademicReview.minLength | VT.PERSON.LanguageKnowledge.AcademicReview |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.AcademicReview.vocabulary | VT.PERSON.LanguageKnowledge.AcademicReview |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.AcademicWriting.maxLength | VT.PERSON.LanguageKnowledge.AcademicWriting |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.AcademicWriting.minLength | VT.PERSON.LanguageKnowledge.AcademicWriting |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.AcademicWriting.vocabulary | VT.PERSON.LanguageKnowledge.AcademicWriting |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.Listening.maxLength | VT.PERSON.LanguageKnowledge.Listening |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.Listening.minLength | VT.PERSON.LanguageKnowledge.Listening |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.Listening.vocabulary | VT.PERSON.LanguageKnowledge.Listening |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.Overall.maxLength | VT.PERSON.LanguageKnowledge.Overall |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.Overall.minLength | VT.PERSON.LanguageKnowledge.Overall |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.Overall.vocabulary | VT.PERSON.LanguageKnowledge.Overall |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.Reading.maxLength | VT.PERSON.LanguageKnowledge.Reading |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.Reading.minLength | VT.PERSON.LanguageKnowledge.Reading |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.Reading.vocabulary | VT.PERSON.LanguageKnowledge.Reading |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.Speaking.maxLength | VT.PERSON.LanguageKnowledge.Speaking |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.Speaking.minLength | VT.PERSON.LanguageKnowledge.Speaking |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.Speaking.vocabulary | VT.PERSON.LanguageKnowledge.Speaking |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.Writing.maxLength | VT.PERSON.LanguageKnowledge.Writing |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.Writing.minLength | VT.PERSON.LanguageKnowledge.Writing |  |  |  | UNMAPPED |
| PERSON | C.PERSON.LanguageKnowledge.Writing.vocabulary | VT.PERSON.LanguageKnowledge.Writing |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Membership.MembershipType.presence | VT.PERSON.Membership.MembershipType |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Membership.MembershipType.vocabulary | VT.PERSON.Membership.MembershipType |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Person.AuthenticusId.maxLength | VT.PERSON.Person.AuthenticusId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.AuthenticusId.maxLength | VT.PERSON.Person.AuthenticusId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.AuthenticusId.minLength | VT.PERSON.Person.AuthenticusId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.AuthenticusId.minLength | VT.PERSON.Person.AuthenticusId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.AuthenticusId.pattern | VT.PERSON.Person.AuthenticusId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.AuthenticusId.pattern | VT.PERSON.Person.AuthenticusId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.AuthenticusId.unique | VT.PERSON.Person.AuthenticusId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.AuthenticusId.unique | VT.PERSON.Person.AuthenticusId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.Biography.minLength | VT.PERSON.Person.Biography |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| PERSON | C.PERSON.Person.Biography.presence | VT.PERSON.Person.Biography |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| PERSON | C.PERSON.Person.CreateDate.presence | VT.PERSON.Person.CreateDate | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.Involvements.custom | VT.PERSON.Person.Involvements |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Person.Involvements.maxCardinality | VT.PERSON.Person.Involvements |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Person.Involvements.minCardinality | VT.PERSON.Person.Involvements |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Person.Involvements.presence | VT.PERSON.Person.Involvements | PTCRIS.CURRENCY | PTCRIS-F1-01DCURREN | GR.PTCRIS_F1_01DCURREN.mandatory_start_date_of_professional_career | FULL |
| PERSON | C.PERSON.Person.LastModificationDate.presence | VT.PERSON.Person.LastModificationDate | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.LattesId.maxLength | VT.PERSON.Person.LattesId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.LattesId.maxLength | VT.PERSON.Person.LattesId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.LattesId.minLength | VT.PERSON.Person.LattesId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.LattesId.minLength | VT.PERSON.Person.LattesId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.LattesId.pattern | VT.PERSON.Person.LattesId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.LattesId.pattern | VT.PERSON.Person.LattesId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.LattesId.unique | VT.PERSON.Person.LattesId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.LattesId.unique | VT.PERSON.Person.LattesId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.MetadataAccessLevel.presence | VT.PERSON.Person.MetadataAccessLevel |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| PERSON | C.PERSON.Person.MetadataAccessLevel.vocabulary | VT.PERSON.Person.MetadataAccessLevel |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| PERSON | C.PERSON.Person.MetadataLicense.presence | VT.PERSON.Person.MetadataLicense |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| PERSON | C.PERSON.Person.MetadataLicense.vocabulary | VT.PERSON.Person.MetadataLicense |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| PERSON | C.PERSON.Person.Name.maxLength | VT.PERSON.Person.Name |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Person.Name.minLength | VT.PERSON.Person.Name |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Person.Name.presence | VT.PERSON.Person.Name | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.full_name_presence_and_length_validation | FULL |
| PERSON | C.PERSON.Person.NationalIdCienciaId.maxLength | VT.PERSON.Person.NationalIdCienciaId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.NationalIdCienciaId.maxLength | VT.PERSON.Person.NationalIdCienciaId |  | PTCRIS-DQ-F1-01IDUNIQ |  | METRIC_ONLY |
| PERSON | C.PERSON.Person.NationalIdCienciaId.minLength | VT.PERSON.Person.NationalIdCienciaId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.NationalIdCienciaId.minLength | VT.PERSON.Person.NationalIdCienciaId |  | PTCRIS-DQ-F1-01IDUNIQ |  | METRIC_ONLY |
| PERSON | C.PERSON.Person.NationalIdCienciaId.pattern | VT.PERSON.Person.NationalIdCienciaId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.NationalIdCienciaId.pattern | VT.PERSON.Person.NationalIdCienciaId |  | PTCRIS-DQ-F1-01IDUNIQ |  | METRIC_ONLY |
| PERSON | C.PERSON.Person.NationalIdCienciaId.presence | VT.PERSON.Person.NationalIdCienciaId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.NationalIdCienciaId.presence | VT.PERSON.Person.NationalIdCienciaId |  | PTCRIS-DQ-F1-01IDUNIQ |  | METRIC_ONLY |
| PERSON | C.PERSON.Person.NationalIdCienciaId.unique | VT.PERSON.Person.NationalIdCienciaId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.NationalIdCienciaId.unique | VT.PERSON.Person.NationalIdCienciaId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_science_id_allocation | FULL |
| PERSON | C.PERSON.Person.NationalIdCienciaId.unique | VT.PERSON.Person.NationalIdCienciaId |  | PTCRIS-DQ-F1-01IDUNIQ |  | METRIC_ONLY |
| PERSON | C.PERSON.Person.OpenAlexId.maxLength | VT.PERSON.Person.OpenAlexId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.OpenAlexId.maxLength | VT.PERSON.Person.OpenAlexId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.OpenAlexId.minLength | VT.PERSON.Person.OpenAlexId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.OpenAlexId.minLength | VT.PERSON.Person.OpenAlexId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.OpenAlexId.pattern | VT.PERSON.Person.OpenAlexId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.OpenAlexId.pattern | VT.PERSON.Person.OpenAlexId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.OpenAlexId.unique | VT.PERSON.Person.OpenAlexId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.OpenAlexId.unique | VT.PERSON.Person.OpenAlexId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.Orcid.maxLength | VT.PERSON.Person.Orcid |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Person.Orcid.minLength | VT.PERSON.Person.Orcid |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Person.Orcid.pattern | VT.PERSON.Person.Orcid | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.open_researcher_and_contributor_id_orcid_format_verification | FULL |
| PERSON | C.PERSON.Person.Orcid.presence | VT.PERSON.Person.Orcid |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Person.Orcid.resolvable | VT.PERSON.Person.Orcid |  | PTCRIS-F1, A1 | GR.PTCRIS_F1_A1.resolvable_pid | FULL |
| PERSON | C.PERSON.Person.Orcid.unique | VT.PERSON.Person.Orcid | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_orcid_allocation | FULL |
| PERSON | C.PERSON.Person.ScholarId.maxLength | VT.PERSON.Person.ScholarId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.ScholarId.maxLength | VT.PERSON.Person.ScholarId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.ScholarId.minLength | VT.PERSON.Person.ScholarId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.ScholarId.minLength | VT.PERSON.Person.ScholarId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.ScholarId.pattern | VT.PERSON.Person.ScholarId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.ScholarId.pattern | VT.PERSON.Person.ScholarId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.ScholarId.unique | VT.PERSON.Person.ScholarId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.ScholarId.unique | VT.PERSON.Person.ScholarId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.ScopusAuthorId.maxLength | VT.PERSON.Person.ScopusAuthorId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.ScopusAuthorId.minLength | VT.PERSON.Person.ScopusAuthorId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.ScopusAuthorId.pattern | VT.PERSON.Person.ScopusAuthorId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.scopus_author_id_format_validation | FULL |
| PERSON | C.PERSON.Person.ScopusAuthorId.pattern | VT.PERSON.Person.ScopusAuthorId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.ScopusAuthorId.unique | VT.PERSON.Person.ScopusAuthorId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.WebOfScienceResearcherId.maxLength | VT.PERSON.Person.WebOfScienceResearcherId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.WebOfScienceResearcherId.minLength | VT.PERSON.Person.WebOfScienceResearcherId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.WebOfScienceResearcherId.pattern | VT.PERSON.Person.WebOfScienceResearcherId | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.web_of_science_researcher_id_format_validation | FULL |
| PERSON | C.PERSON.Person.WebOfScienceResearcherId.pattern | VT.PERSON.Person.WebOfScienceResearcherId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.Person.WebOfScienceResearcherId.unique | VT.PERSON.Person.WebOfScienceResearcherId | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR |  | DIMENSION_AND_METRIC |
| PERSON | C.PERSON.PersonName.Firstname.maxLength | VT.PERSON.PersonName.Firstname |  |  |  | UNMAPPED |
| PERSON | C.PERSON.PersonName.Firstname.minLength | VT.PERSON.PersonName.Firstname |  |  |  | UNMAPPED |
| PERSON | C.PERSON.PersonName.Firstname.pattern | VT.PERSON.PersonName.Firstname |  |  |  | UNMAPPED |
| PERSON | C.PERSON.PersonName.Lastname.maxLength | VT.PERSON.PersonName.Lastname |  |  |  | UNMAPPED |
| PERSON | C.PERSON.PersonName.Lastname.minLength | VT.PERSON.PersonName.Lastname |  |  |  | UNMAPPED |
| PERSON | C.PERSON.PersonName.Lastname.pattern | VT.PERSON.PersonName.Lastname | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.standardized_citation_name_format_verification | FULL |
| PERSON | C.PERSON.PersonName.Lastname.presence | VT.PERSON.PersonName.Lastname | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.full_name_presence_and_length_validation | FULL |
| PERSON | C.PERSON.PersonName.OtherName.maxLength | VT.PERSON.PersonName.OtherName |  |  |  | UNMAPPED |
| PERSON | C.PERSON.PersonName.OtherName.minLength | VT.PERSON.PersonName.OtherName |  |  |  | UNMAPPED |
| PERSON | C.PERSON.PersonName.OtherName.pattern | VT.PERSON.PersonName.OtherName |  |  |  | UNMAPPED |
| PERSON | C.PERSON.PersonName.PersonNameType.maxLength | VT.PERSON.PersonName.PersonNameType |  |  |  | UNMAPPED |
| PERSON | C.PERSON.PersonName.PersonNameType.minLength | VT.PERSON.PersonName.PersonNameType |  |  |  | UNMAPPED |
| PERSON | C.PERSON.PersonName.PersonNameType.presence | VT.PERSON.PersonName.PersonNameType |  |  |  | UNMAPPED |
| PERSON | C.PERSON.PersonName.PersonNameType.vocabulary | VT.PERSON.PersonName.PersonNameType |  |  |  | UNMAPPED |
| PERSON | C.PERSON.PersonalInfo.BirthDate.maxDate | VT.PERSON.PersonalInfo.BirthDate | PTCRIS.CONSISTENCY | PTCRIS-F1-01DCONSIST | GR.PTCRIS_F1_01DCONSIST.non_existent_or_futuristic_birth_date_restriction | FULL |
| PERSON | C.PERSON.PersonalInfo.BirthDate.minDate | VT.PERSON.PersonalInfo.BirthDate | PTCRIS.CONSISTENCY | PTCRIS-F1-01DCONSIST | GR.PTCRIS_F1_01DCONSIST.non_existent_or_futuristic_birth_date_restriction | FULL |
| PERSON | C.PERSON.PersonalInfo.BirthDate.presence | VT.PERSON.PersonalInfo.BirthDate |  |  |  | UNMAPPED |
| PERSON | C.PERSON.PersonalInfo.Sex.maxLength | VT.PERSON.PersonalInfo.Sex |  |  |  | UNMAPPED |
| PERSON | C.PERSON.PersonalInfo.Sex.minLength | VT.PERSON.PersonalInfo.Sex |  |  |  | UNMAPPED |
| PERSON | C.PERSON.PersonalInfo.Sex.vocabulary | VT.PERSON.PersonalInfo.Sex | PTCRIS.SEMANTIC | PTCRIS-F1-01DSEMANT | GR.PTCRIS_F1_01DSEMANT.gender_classification_conformity | FULL |
| PERSON | C.PERSON.Prize.EffectiveDate.maxDate | VT.PERSON.Prize.EffectiveDate |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Prize.EffectiveDate.minDate | VT.PERSON.Prize.EffectiveDate |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Prize.EffectiveDate.presence | VT.PERSON.Prize.EffectiveDate |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Prize.ResearchAreas.presence | VT.PERSON.Prize.ResearchAreas |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Prize.ResearchAreas.vocabulary | VT.PERSON.Prize.ResearchAreas |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Prize.ToDate.minDate | VT.PERSON.Prize.ToDate |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Prize.Type.presence | VT.PERSON.Prize.Type |  |  |  | UNMAPPED |
| PERSON | C.PERSON.Prize.Type.vocabulary | VT.PERSON.Prize.Type |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.Costs.custom | VT.PROJECT.Project.Costs | PTCRIS.CONSISTENCY | PTCRIS-F1-01DCONSIST | GR.PTCRIS_F1_01DCONSIST.sum_of_linked_fundings_amounts | FULL |
| PROJECT | C.PROJECT.Project.CreateDate.presence | VT.PROJECT.Project.CreateDate | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| PROJECT | C.PROJECT.Project.Description.minLength | VT.PROJECT.Project.Description |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| PROJECT | C.PROJECT.Project.Description.presence | VT.PROJECT.Project.Description |  | PTCRIS-FsF-F2-01M |  | METRIC_ONLY |
| PROJECT | C.PROJECT.Project.Doi.maxLength | VT.PROJECT.Project.Doi |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.Doi.minLength | VT.PROJECT.Project.Doi |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.Doi.pattern | VT.PROJECT.Project.Doi | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.doi_format_verification | FULL |
| PROJECT | C.PROJECT.Project.Doi.presence | VT.PROJECT.Project.Doi |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.Doi.resolvable | VT.PROJECT.Project.Doi |  | PTCRIS-F1, A1 | GR.PTCRIS_F1_A1.resolvable_doi | FULL |
| PROJECT | C.PROJECT.Project.Doi.unique | VT.PROJECT.Project.Doi | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_doi_allocation | FULL |
| PROJECT | C.PROJECT.Project.FromDate.maxDate | VT.PROJECT.Project.FromDate |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.FromDate.minDate | VT.PROJECT.Project.FromDate |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.FromDate.presence | VT.PROJECT.Project.FromDate | PTCRIS.CURRENCY | PTCRIS-F1-01DCURREN | GR.PTCRIS_F1_01DCURREN.mandatory_project_boundary_dates | FULL |
| PROJECT | C.PROJECT.Project.Fundings.custom | VT.PROJECT.Project.Fundings | PTCRIS.CONSISTENCY | PTCRIS-F1-01DCONSIST | GR.PTCRIS_F1_01DCONSIST.different_funding_ids_in_project_and_funding | FULL |
| PROJECT | C.PROJECT.Project.Fundings.maxCardinality | VT.PROJECT.Project.Fundings |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.Fundings.minCardinality | VT.PROJECT.Project.Fundings |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.Fundings.presence | VT.PROJECT.Project.Fundings |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.Identifiers.minCardinality | VT.PROJECT.Project.Identifiers | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.project_without_at_least_one_identifier | FULL |
| PROJECT | C.PROJECT.Project.Identifiers.presence | VT.PROJECT.Project.Identifiers | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.project_without_at_least_one_identifier | FULL |
| PROJECT | C.PROJECT.Project.Identifiers.unique | VT.PROJECT.Project.Identifiers |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.LastModificationDate.presence | VT.PROJECT.Project.LastModificationDate | PTCRIS.LINEAGE | PTCRIS-F1-01DLINEAGE |  | DIMENSION_AND_METRIC |
| PROJECT | C.PROJECT.Project.MetadataAccessLevel.presence | VT.PROJECT.Project.MetadataAccessLevel |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| PROJECT | C.PROJECT.Project.MetadataAccessLevel.vocabulary | VT.PROJECT.Project.MetadataAccessLevel |  | PTCRIS-FsF-A1-01M |  | METRIC_ONLY |
| PROJECT | C.PROJECT.Project.MetadataLicense.presence | VT.PROJECT.Project.MetadataLicense |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| PROJECT | C.PROJECT.Project.MetadataLicense.vocabulary | VT.PROJECT.Project.MetadataLicense |  | PTCRIS-FsF-R1.1-01M |  | METRIC_ONLY |
| PROJECT | C.PROJECT.Project.Name.maxLength | VT.PROJECT.Project.Name |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.Name.minLength | VT.PROJECT.Project.Name |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.Name.pattern | VT.PROJECT.Project.Name |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.Name.presence | VT.PROJECT.Project.Name | PTCRIS.CONSISTENCY | PTCRIS-F1-01DCONSIST | GR.PTCRIS_F1_01DCONSIST.project_title_presence_requirement | FULL |
| PROJECT | C.PROJECT.Project.NationalIdProjectReference.maxLength | VT.PROJECT.Project.NationalIdProjectReference |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.NationalIdProjectReference.minLength | VT.PROJECT.Project.NationalIdProjectReference |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.NationalIdProjectReference.presence | VT.PROJECT.Project.NationalIdProjectReference |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.NationalIdProjectReference.unique | VT.PROJECT.Project.NationalIdProjectReference | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_pid_allocation | FULL |
| PROJECT | C.PROJECT.Project.Organisations.custom | VT.PROJECT.Project.Organisations | PTCRIS.CONSISTENCY | PTCRIS-F1-01DCONSIST | GR.PTCRIS_F1_01DCONSIST.sum_of_organizations_funding_greater_than_project_total | FULL |
| PROJECT | C.PROJECT.Project.Organisations.custom | VT.PROJECT.Project.Organisations | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.project_with_coordinating_organization_but_no_other_participants | FULL |
| PROJECT | C.PROJECT.Project.Organisations.maxCardinality | VT.PROJECT.Project.Organisations |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.Organisations.minCardinality | VT.PROJECT.Project.Organisations |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.Organisations.presence | VT.PROJECT.Project.Organisations |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.Raid.maxLength | VT.PROJECT.Project.Raid |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.Raid.minLength | VT.PROJECT.Project.Raid |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.Raid.pattern | VT.PROJECT.Project.Raid | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.raid_format_verification | FULL |
| PROJECT | C.PROJECT.Project.Raid.presence | VT.PROJECT.Project.Raid |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.Raid.resolvable | VT.PROJECT.Project.Raid |  | PTCRIS-F1, A1 | GR.PTCRIS_F1_A1.resolvable_raid | FULL |
| PROJECT | C.PROJECT.Project.Raid.unique | VT.PROJECT.Project.Raid | PTCRIS.ACCURACY | PTCRIS-F1-01DACURR | GR.PTCRIS_F1_01DACURR.global_uniqueness_of_raid_allocation | FULL |
| PROJECT | C.PROJECT.Project.ResearchAreas.presence | VT.PROJECT.Project.ResearchAreas |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.ResearchAreas.unique | VT.PROJECT.Project.ResearchAreas |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.ResearchAreas.vocabulary | VT.PROJECT.Project.ResearchAreas | PTCRIS.CONSISTENCY | PTCRIS-F1-01DCONSIST | GR.PTCRIS_F1_01DCONSIST.semantic_iri_url_validation | FULL |
| PROJECT | C.PROJECT.Project.Team.custom | VT.PROJECT.Project.Team | PTCRIS.STRUCTURAL_CONSISTENCY | PTCRIS-F1-01DSTRUCT | GR.PTCRIS_F1_01DSTRUCT.project_with_team_but_no_principal_investigator | FULL |
| PROJECT | C.PROJECT.Project.Team.maxCardinality | VT.PROJECT.Project.Team |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.Team.minCardinality | VT.PROJECT.Project.Team |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.Team.presence | VT.PROJECT.Project.Team |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.ToDate.maxDate | VT.PROJECT.Project.ToDate |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.ToDate.minDate | VT.PROJECT.Project.ToDate |  |  |  | UNMAPPED |
| PROJECT | C.PROJECT.Project.ToDate.presence | VT.PROJECT.Project.ToDate | PTCRIS.CURRENCY | PTCRIS-F1-01DCURREN | GR.PTCRIS_F1_01DCURREN.mandatory_project_boundary_dates | FULL |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Contact.ContactEmail.maxLength | VT.SHARED_COMPONENTS.Contact.ContactEmail |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Contact.ContactEmail.minLength | VT.SHARED_COMPONENTS.Contact.ContactEmail |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Contact.ContactEmail.pattern | VT.SHARED_COMPONENTS.Contact.ContactEmail |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Contact.FaxNumber.maxLength | VT.SHARED_COMPONENTS.Contact.FaxNumber |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Contact.FaxNumber.minLength | VT.SHARED_COMPONENTS.Contact.FaxNumber |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Contact.FaxNumber.pattern | VT.SHARED_COMPONENTS.Contact.FaxNumber |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Contact.MobilePhoneNumber.maxLength | VT.SHARED_COMPONENTS.Contact.MobilePhoneNumber |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Contact.MobilePhoneNumber.minLength | VT.SHARED_COMPONENTS.Contact.MobilePhoneNumber |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Contact.MobilePhoneNumber.pattern | VT.SHARED_COMPONENTS.Contact.MobilePhoneNumber |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Contact.PhoneNumber.maxLength | VT.SHARED_COMPONENTS.Contact.PhoneNumber |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Contact.PhoneNumber.minLength | VT.SHARED_COMPONENTS.Contact.PhoneNumber |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Contact.PhoneNumber.pattern | VT.SHARED_COMPONENTS.Contact.PhoneNumber |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Country.Code.maxLength | VT.SHARED_COMPONENTS.Country.Code |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Country.Code.minLength | VT.SHARED_COMPONENTS.Country.Code |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Country.Code.presence | VT.SHARED_COMPONENTS.Country.Code |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Country.Code.unique | VT.SHARED_COMPONENTS.Country.Code |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Country.Code.vocabulary | VT.SHARED_COMPONENTS.Country.Code | PTCRIS.SEMANTIC | PTCRIS-F1-01DSEMANT | GR.PTCRIS_F1_01DSEMANT.standardized_geopolitical_country_coding | FULL |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Currency.Code.maxLength | VT.SHARED_COMPONENTS.Currency.Code |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Currency.Code.minLength | VT.SHARED_COMPONENTS.Currency.Code |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Currency.Code.pattern | VT.SHARED_COMPONENTS.Currency.Code |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Currency.Code.presence | VT.SHARED_COMPONENTS.Currency.Code |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Currency.Code.unique | VT.SHARED_COMPONENTS.Currency.Code |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Currency.Code.vocabulary | VT.SHARED_COMPONENTS.Currency.Code |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Currency.Symbol.maxLength | VT.SHARED_COMPONENTS.Currency.Symbol |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Currency.Symbol.minLength | VT.SHARED_COMPONENTS.Currency.Symbol |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Currency.Symbol.vocabulary | VT.SHARED_COMPONENTS.Currency.Symbol |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue.custom | VT.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue.presence | VT.SHARED_COMPONENTS.EntityIndicator.NumericValueBooleanValueTextualValue |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.EntityIndicator.Subclass.custom | VT.SHARED_COMPONENTS.EntityIndicator.Subclass |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.FlexibleDate.Day.custom | VT.SHARED_COMPONENTS.FlexibleDate.Day |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.FlexibleDate.Day.maxValue | VT.SHARED_COMPONENTS.FlexibleDate.Day |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.FlexibleDate.Day.minValue | VT.SHARED_COMPONENTS.FlexibleDate.Day |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.FlexibleDate.Day.presence | VT.SHARED_COMPONENTS.FlexibleDate.Day |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.FlexibleDate.Month.maxValue | VT.SHARED_COMPONENTS.FlexibleDate.Month |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.FlexibleDate.Month.minValue | VT.SHARED_COMPONENTS.FlexibleDate.Month |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.FlexibleDate.Month.presence | VT.SHARED_COMPONENTS.FlexibleDate.Month |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.FlexibleDate.TextYear.custom | VT.SHARED_COMPONENTS.FlexibleDate.TextYear |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.FlexibleDate.TextYear.presence | VT.SHARED_COMPONENTS.FlexibleDate.TextYear |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.FlexibleDate.Year.maxValue | VT.SHARED_COMPONENTS.FlexibleDate.Year |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.FlexibleDate.Year.minValue | VT.SHARED_COMPONENTS.FlexibleDate.Year |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.FlexibleDate.Year.presence | VT.SHARED_COMPONENTS.FlexibleDate.Year |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.GeoLocation.Address.presence | VT.SHARED_COMPONENTS.GeoLocation.Address |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.GeoLocation.Latitude.maxValue | VT.SHARED_COMPONENTS.GeoLocation.Latitude |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.GeoLocation.Latitude.minValue | VT.SHARED_COMPONENTS.GeoLocation.Latitude |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.GeoLocation.Latitude.presence | VT.SHARED_COMPONENTS.GeoLocation.Latitude |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.GeoLocation.Longitude.maxValue | VT.SHARED_COMPONENTS.GeoLocation.Longitude |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.GeoLocation.Longitude.minValue | VT.SHARED_COMPONENTS.GeoLocation.Longitude |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.GeoLocation.Longitude.presence | VT.SHARED_COMPONENTS.GeoLocation.Longitude |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Identifier.RegularExpression.custom | VT.SHARED_COMPONENTS.Identifier.RegularExpression |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Identifier.RegularExpression.maxLength | VT.SHARED_COMPONENTS.Identifier.RegularExpression |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Identifier.RegularExpression.minLength | VT.SHARED_COMPONENTS.Identifier.RegularExpression |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Identifier.RegularExpression.presence | VT.SHARED_COMPONENTS.Identifier.RegularExpression |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Language.LanguageCode.maxLength | VT.SHARED_COMPONENTS.Language.LanguageCode |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Language.LanguageCode.minLength | VT.SHARED_COMPONENTS.Language.LanguageCode |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Language.LanguageCode.pattern | VT.SHARED_COMPONENTS.Language.LanguageCode |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Language.LanguageCode.presence | VT.SHARED_COMPONENTS.Language.LanguageCode |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Language.LanguageCode.unique | VT.SHARED_COMPONENTS.Language.LanguageCode |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.Language.LanguageCode.vocabulary | VT.SHARED_COMPONENTS.Language.LanguageCode |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.LanguageTag.LanguageTag.maxLength | VT.SHARED_COMPONENTS.LanguageTag.LanguageTag |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.LanguageTag.LanguageTag.minLength | VT.SHARED_COMPONENTS.LanguageTag.LanguageTag |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.LanguageTag.LanguageTag.pattern | VT.SHARED_COMPONENTS.LanguageTag.LanguageTag |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.LanguageTag.LanguageTag.presence | VT.SHARED_COMPONENTS.LanguageTag.LanguageTag |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.LanguageTag.LanguageTag.unique | VT.SHARED_COMPONENTS.LanguageTag.LanguageTag |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.LanguageTag.LanguageTag.vocabulary | VT.SHARED_COMPONENTS.LanguageTag.LanguageTag |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.MonetaryAmount.Amount.maxValue | VT.SHARED_COMPONENTS.MonetaryAmount.Amount |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.MonetaryAmount.Amount.minValue | VT.SHARED_COMPONENTS.MonetaryAmount.Amount |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.MonetaryAmount.Amount.presence | VT.SHARED_COMPONENTS.MonetaryAmount.Amount |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.ProfilePhotoOrLogo.Height.maxValue | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.Height |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.ProfilePhotoOrLogo.Height.minValue | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.Height |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.ProfilePhotoOrLogo.Height.presence | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.Height |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset.maxValue | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset.minValue | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset.presence | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.LeftOffset |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset.maxValue | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset.minValue | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset.presence | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.TopOffset |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.ProfilePhotoOrLogo.Width.maxValue | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.Width |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.ProfilePhotoOrLogo.Width.minValue | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.Width |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.ProfilePhotoOrLogo.Width.presence | VT.SHARED_COMPONENTS.ProfilePhotoOrLogo.Width |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.ResearchArea.Name.maxLength | VT.SHARED_COMPONENTS.ResearchArea.Name |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.ResearchArea.Name.minLength | VT.SHARED_COMPONENTS.ResearchArea.Name |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.ResearchArea.Name.presence | VT.SHARED_COMPONENTS.ResearchArea.Name |  |  |  | UNMAPPED |
| SHARED_COMPONENTS | C.SHARED_COMPONENTS.ResearchArea.Name.vocabulary | VT.SHARED_COMPONENTS.ResearchArea.Name |  |  |  | UNMAPPED |
