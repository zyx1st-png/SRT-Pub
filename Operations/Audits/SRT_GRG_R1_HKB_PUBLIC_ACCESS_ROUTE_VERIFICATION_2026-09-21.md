---
id: SRT-GRG-R1-HKB-PUBLIC-ACCESS-ROUTE-VERIFICATION-20260921
type: audit
status: active
record_stage: public_access_route_verification_complete
date: 2026-09-21
layer: operations
epistemic_layer: experimental
claim_mode: audit
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Audits/SRT_GRG_R1_HKB_SOURCE_PROTOCOL_ACCESS_FEASIBILITY_2026-09-21.md
  - Operations/Proposals/SRT_GRG_R1_HKB_EXISTING_DATA_ACCESS_REQUEST_PACKAGE_2026-09-21.md
  - Materials/2026/SRC_2026_09_21_HKB_Post2020_Normalization_Reanalysis.md
tags: [GRG, GRGR1, HKB, DataAccess, PublicSearch, ContactVerification, LegacyData]
---

# GRG-R1 HKB public access-route verification — 2026-09-21

## 0. Verdict

~~~text
PUBLIC RAW 300-HZ BILATERAL TRAJECTORY ACCESS
= STILL NOT LOCATED

2020 SUPPLEMENTARY MATERIAL
= PARTICIPANT-LEVEL OUTCOME TABLE ONLY / INSUFFICIENT

CURRENT AUTHOR CONTACT ROUTE
= VERIFIED

INSTITUTIONAL LEGACY-DATA FALLBACK
= IDENTIFIED

REQUEST ACTUALLY SENT
= NO

RAW DATA OPENED
= NO

R1c EXECUTION
= HOLD
R1d / O4
= BLOCKED
~~~

This is a bounded public-access verification, not proof that the historical raw data no longer exist.

## 1. Public article and supplementary-material check

Primary 2020 reanalysis:

~~~text
de Poel HJ, Roerdink M, Peper CLE, Beek PJ
Brain Sciences 10(10):724
DOI 10.3390/brainsci10100724
~~~

The paper's published supplementary-material statement identifies:

~~~text
Table S1: Outcome values for the individual participants
~~~

No raw bilateral angular-displacement trajectory archive is identified in the article's public supplementary-material route.

The 2020 paper also states in its acknowledgements that Auke Post conducted the original experiment and made the data available for the reanalysis.

Author-contribution metadata assigns:

~~~text
resources = Peper + Beek
data curation = de Poel + Peper + Beek
~~~

Therefore the strongest current inference remains:

~~~text
historical reusable data object existed
but
current public raw trajectory route is not established.
~~~

Primary public sources:

- https://doi.org/10.3390/brainsci10100724
- https://research.rug.nl/en/publications/a-re-appraisal-of-the-effect-of-amplitude-on-the-stability-of-int
- https://research.vu.nl/en/publications/a-re-appraisal-of-the-effect-of-amplitude-on-the-stability-of-int/

## 2. Repository / portal discovery check

Targeted public searches were run across:

- VU Research Portal publication and dataset surfaces;
- University of Groningen / UMCG Research Portal;
- DataverseNL-oriented search;
- OSF-oriented search;
- Zenodo-oriented search;
- Figshare-oriented search;
- exact DOI / title / author combinations.

Located:

- 2000 publications;
- 2020 reanalysis full text;
- 2020 participant-level supplementary outcome material;
- current institutional author profiles;
- current VU research-data support routes.

Not located:

~~~text
original left/right 300-Hz trajectory files
trial-level perturbation timing files
original condition/trial manifest
raw-data DOI / accession / Dataverse / OSF / Zenodo / Figshare record
~~~

Absence from this bounded discovery pass is not evidence that no institutional or private archive exists.

## 3. Current primary author route verified

### Harjo J. de Poel

Current University of Groningen / UMCG profile identifies:

~~~text
Harjo de Poel
Assistant Professor
Faculty of Medical Sciences / UMCG
email: h.j.de.poel@umcg.nl
~~~

Current profile:

https://www.rug.nl/staff/h.j.de.poel/?lang=en

Research portal:

https://research.rug.nl/en/persons/harjo-de-poel/

Why this remains the preferred first route:

- corresponding author of the 2020 reanalysis;
- 2020 data-curation role;
- current work remains in coordination dynamics / coupled oscillators;
- current institutional contact is publicly verified.

## 4. Current VU data-custody route verified

### C. Lieke E. Peper

Current VU Neurocontrol staff page lists:

~~~text
Lieke Peper
Lecturer
email: l.peper@vu.nl
~~~

Current source:

https://vu.nl/en/research/more-about/research-section-neurocontrol

Why Peper should move ahead of a generic coauthor route for legacy-data custody:

- author of the original 2000 experiment;
- 2020 resources role;
- 2020 data-curation role;
- remains current VU Human Movement Sciences / Neurocontrol staff.

### Melvyn Roerdink

Current VU pages confirm:

~~~text
Melvyn Roerdink
Associate Professor / Technology in Motion
email: m.roerdink@vu.nl
~~~

Current source:

https://vu.nl/en/about-vu/more-about/credential-melvyn-roerdink

Roerdink remains a valid scientific routing contact but the 2020 contribution record provides less direct evidence of legacy-data custody than for de Poel / Peper.

## 5. Institutional archive fallback

VU Faculty of Behavioural and Movement Sciences currently maintains dedicated research-data support.

Current official route:

~~~text
Senior / faculty research-data stewardship:
research.data.fgb@vu.nl
~~~

Source:

https://vu.nl/en/employee/research-data-support/contact-your-data-steward

Faculty RDM page:

https://vu.nl/en/employee/research-data-management-fbms

The VU Research Portal also has a dedicated Faculty of Behavioural and Movement Sciences datasets/software collection:

https://research.vu.nl/en/organisations/faculty-of-behavioural-and-movement-sciences-2/datasets/

No matching Post/de Poel raw trajectory dataset was located in the bounded public search, but the data-steward route is useful if authors believe a legacy institutional archive may exist or if ownership / sharing authority is unclear.

## 6. Recommended access sequence

Current preferred order:

~~~text
Route 1:
Harjo de Poel
h.j.de.poel@umcg.nl
ask whether the original data still exist and who controls access

Route 2:
Lieke Peper
l.peper@vu.nl
legacy original-study + 2020 resources/data-curation route

Route 3:
Melvyn Roerdink
m.roerdink@vu.nl
2020 coauthor / current VU coordination-science route

Route 4:
VU FGB Research Data Steward
research.data.fgb@vu.nl
institutional archive / ownership / reuse routing fallback
~~~

These are routes, not claims that any recipient possesses or can release the data.

## 7. What not to do

Do not:

- infer data loss from public-search failure;
- substitute Table S1 for trajectory-level analysis;
- scrape or reconstruct pseudo-trajectories from figures;
- combine unrelated coordination datasets and call them the Post dataset;
- send broad mass outreach;
- open any received outcome data before a raw-data analysis charter;
- treat an informal file transfer as sufficient reuse authorization.

## 8. Access decision

The public discovery pass does not change the empirical gate:

~~~text
PUBLIC RAW ACCESS = NO-GO / NOT LOCATED
CURRENT AUTHORIZED RAW ACCESS = NOT ESTABLISHED
~~~

It does improve the execution route:

~~~text
author route = current and verified
legacy-data custody priority = de Poel -> Peper -> Roerdink
institutional fallback = VU FGB research-data stewardship
~~~

The next external action, if the author chooses it, is one bounded data-access request.

This audit does not authorize sending that request automatically.

## 9. Programme consequence

~~~text
HKB remains the live non-RNN R1c candidate.
No weaker public-data substitute is authorized.
No new human experiment is authorized.
Simulation is not confirmation.
R1d / O4 remains blocked.
Canonical edit = NO.
~~~
