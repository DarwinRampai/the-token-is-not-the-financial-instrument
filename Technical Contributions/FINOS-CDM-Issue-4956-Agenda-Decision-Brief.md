# FINOS CDM Issue 4956: Five-Minute Agenda Decision Brief

**Contributor:** Darwin Rampai, Independent Researcher  
**Issue:** [FINOS Common Domain Model 4956](https://github.com/finos/common-domain-model/issues/4956)  
**Technical record:** [Movement Is Not Admission](https://doi.org/10.5281/zenodo.21401045)  
**Requested forum:** FINOS Tokenized Assets Working Group

## Decision Requested

Classify the record-integrity requirements identified in issue 4956 as one or
more of the following:

1. native FINOS CDM fields;
2. a standardized tokenized-asset record-integrity profile; or
3. implementation guidance outside the native model.

The requested outcome is a recorded scope decision, an accountable owner and a
next artifact. The working group is not being asked to determine collateral
eligibility or endorse TFII.

## 0:00-0:40 - The Boundary

The inspected sandbox demonstrated that collateral could move under eligibility
assumed in advance. Movement is an operational fact. Production admission is a
separate determination that requires instrument identity, authoritative record,
ownership effectiveness, control, valuation, correction, rights and evidence
completeness.

## 0:40-1:30 - The Test

Seventeen record-integrity requirements were tested against FINOS CDM revision
`a6ffe777bc12ef3d289579cb3a86d1cbffea63d2`.

| Result | Requirements |
|---|---:|
| PASS | 5 |
| PARTIAL | 3 |
| FAIL | 9 |

`FAIL` means that no native typed path was identified under the published test
rule. It does not mean that CDM is defective.

## 1:30-2:20 - What Native CDM Represented

Native CDM represented:

- the fund share as a financial instrument;
- relevant record-processing parties;
- mechanical asset transfer;
- operational transfer state; and
- collateral criteria, haircuts and concentration limits.

Native support was partial for valuation authority and timing, correction
lineage, and integrity-gated eligibility.

## 2:20-3:15 - What Required the TFII Profile

No native typed path was identified for:

1. the authoritative ownership record;
2. the blockchain or token's role relative to that record;
3. the instrument-specific ownership-effective event;
4. correction authority and record precedence;
5. cross-record reconciliation;
6. wallet and holder eligibility controls;
7. field-level evidence states and explicit Unknowns;
8. source and downstream permitted-use rights; and
9. coverage, gaps and freshness.

The typed TFII Record Integrity Profile represented all seventeen requirements
across five frozen public records without inferring private facts. This is a
representability result, not an admission result.

## 3:15-4:10 - Why UNKNOWN Must Stop Admission

A boolean eligibility result cannot distinguish a failed criterion from a
criterion that was never lawfully or evidentially established. If mandatory
ownership, custody, control, reconciliation or valuation evidence is absent,
running the eligibility query converts missing evidence into apparent
certainty.

The fail-closed control therefore applies this sequence:

`record-integrity precheck -> CDM eligibility query -> admission determination`

Three fixed vectors executed `PASS`, `FAIL` and `UNKNOWN`. The incomplete vector
stopped before eligibility query. Five public tokenized-fund records remained
`UNKNOWN`; zero admission decisions were manufactured.

## 4:10-5:00 - Exact Working-Group Resolution

For each of the nine failed and three partial requirements, record:

| Required decision | Output |
|---|---|
| In native CDM scope? | Yes / No / Deferred |
| If not native, standardized profile? | Yes / No / Deferred |
| If neither, implementation guidance? | Named document and owner |
| Next artifact | Issue, proposal, profile or guidance text |
| Accountable owner | Named maintainer or working-group lead |

Proposed resolution:

> The Tokenized Assets Working Group accepts issue 4956 for scope
> classification and will determine whether each unresolved record-integrity
> requirement belongs in native CDM, a standardized profile or implementation
> guidance. This resolution does not determine instrument eligibility.

## Claim Boundary

This brief does not allege a CDM defect, classify any instrument as eligible or
ineligible, provide a legal opinion or infer unavailable production evidence.
