# The Token Is Not the Financial Instrument

**Darwin Rampai, Independent Researcher**  
**Version 1.0 | 16 July 2026**

This repository is the canonical public evidence record for TFII research,
technical determinations, executable controls, and bounded machine-readable
evidence produced by Darwin Rampai.

## Current Determination

### Movement Is Not Admission

The July 2026 GDF and ISDA tokenized-money-market-fund sandbox demonstrated
collateral movement under assumed eligibility. It did not test whether a live
tokenized fund satisfied the production admission boundary.

| Control | Result |
|---|---:|
| Native FINOS CDM representation | PARTIAL: 5 PASS / 3 PARTIAL / 9 FAIL |
| FINOS CDM plus TFII Record Integrity Profile | PASS: 17 / 17 |
| Admission-control branches | PASS / FAIL / UNKNOWN executed |
| Public tokenized-fund records | 5 UNKNOWN / 0 decisions manufactured |

- [Read the web determination](docs/movement-is-not-admission.html)
- [Open the complete version 1.0 record](Determinations/Movement%20Is%20Not%20Admission/v1.0/README.md)
- [Download the PDF](Determinations/Movement%20Is%20Not%20Admission/v1.0/Determination/Movement_Is_Not_Admission_Darwin_Rampai_2026_v1.0.pdf)
- [Inspect the machine-readable evidence](Determinations/Movement%20Is%20Not%20Admission/v1.0/Evidence/)
- [Verify the file hashes](Determinations/Movement%20Is%20Not%20Admission/v1.0/SHA256SUMS.txt)

Five public records remain UNKNOWN because receiver-specific ownership,
control, reconciliation, valuation, haircut, custody, and default-access
evidence was unavailable. UNKNOWN is not a finding that an instrument is
unsafe or ineligible.

## Apply the Control to Production

The public record proves the control and its bounded execution. A production
owner can commission the same control for one named instrument, one named
collateral workflow and one fixed observation boundary.

- result: `PASS`, `PARTIAL`, `FAIL` or `UNKNOWN`;
- fixed fee: USD 3,000 prepaid;
- delivery target: three business days after payment and complete authorized
  inputs; and
- no unpaid production pilot.

[Open the production-inspection scope and exact intake instructions](PRODUCTION_INSPECTION.md).

## Foundational Paper

*The Token Is Not the Financial Instrument: Five Tokenized Funds, Five Record
Architectures, and the Control Boundary Between Blockchain Transfer and
Financial Ownership* establishes the underlying record-integrity problem.

## Supported Result

Five United States primary filings describe five materially different
relationships among token movement, authoritative ownership records,
transfer-effectiveness boundaries, reconciliation and correction. Similar
tokenized-share forms therefore cannot be normalized as one ownership or
transfer model without preserving source-native authority and timing.

## Read

- [Permanent DOI record](https://doi.org/10.5281/zenodo.21399416)
- [Research paper (PDF)](The_Token_Is_Not_the_Financial_Instrument_Darwin_Rampai_2026_v1.0.pdf)
- [Web-readable paper](docs/paper.html)
- [Complete bounded public evidence package](The_Token_Is_Not_the_Financial_Instrument_v1.0_Public_Evidence_Package.zip)
- [TFII technical contributions](Technical%20Contributions/README.md)
- [FINOS issue 4956 five-minute agenda brief](Technical%20Contributions/FINOS-CDM-Issue-4956-Agenda-Decision-Brief.md)
- [Release manifest](release/v1.0/RELEASE%20MANIFEST.json)
- [SHA-256 checksums](release/v1.0/SHA256SUMS.txt)

## Technical Contributions

The 16 July 2026 technical contribution applies the public TFII records to three
production questions:

- **FINOS CDM conformance:** 17 requirements tested; overall result `PARTIAL`.
- **CDM plus TFII Record Integrity Profile:** all 17 representability
  requirements pass across five public records without inferring private facts.
- **Admission-control execution:** fixed vectors execute `PASS`, `FAIL` and
  `UNKNOWN`; two bounded eligibility-reference queries run successfully.
- **Tokenized-fund collateral admission:** five instruments held for missing
  program evidence; zero CDM eligibility queries run; result `UNKNOWN`.

The contribution includes JSON Schemas, machine-readable results, frozen public
fixtures and a validator. It does not alter the frozen version 1.0 paper or
evidence package.

## Evidence Package

The versioned release contains:

- the paper in PDF, DOCX, HTML and Markdown;
- a bounded five-record machine-readable sample;
- a reduced claim-to-evidence matrix;
- a deterministic transfer-boundary classification example;
- two black-and-white evidence figures;
- the public record contract, source-use basis and correction policy;
- a public correction register; and
- a hash-bound release manifest.

## Reproduce

1. Open the public sample in `release/v1.0/Public Evidence/`.
2. Apply the rules in the transfer-boundary calculation example.
3. Confirm that the five records resolve into four observed timing groups and
   one explicit Unknown.
4. Compare the output with the claim-to-evidence matrix and paper.
5. Verify every packaged artifact against `release/v1.0/SHA256SUMS.txt`.

## Controlled Boundary

The complete maintained registry, normalized source receipts, calculation
receipts, correction feed, source-monitor implementation, complete source
locators and customer delivery package are not public. Commercial or production
use requires written terms and applicable source rights.

## Limits

This is a bounded independent research result. It is not a legal opinion,
valuation source, regulated benchmark, audit, investment recommendation,
trading signal or allegation of wrongdoing. Private transfer-agent,
administrator, custodian, customer and collateral records are excluded.
Unknowns remain Unknown.

## Corrections

See [the correction procedure](release/v1.0/Corrections/CORRECTIONS.md). Supported
corrections are versioned and never silently overwrite a released artifact.

## Integrity

Public evidence package SHA-256:

`4d0b79302aa300deced0c04d286eb3d647030773fbf14fbc7d0fc01b2463653f`

## Citation

Rampai, Darwin. 2026. *The Token Is Not the Financial Instrument: Five
Tokenized Funds, Five Record Architectures, and the Control Boundary Between
Blockchain Transfer and Financial Ownership*. Version 1.0. Independent
Research.

DOI: [10.5281/zenodo.21399416](https://doi.org/10.5281/zenodo.21399416)

## Rights

Copyright Darwin Rampai 2026. Public reading, quotation and citation of the
paper and bounded evidence package are permitted with attribution. See
[RIGHTS.md](RIGHTS.md) for the public and controlled-use boundary.
