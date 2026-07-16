# TFII-to-FINOS CDM Conformance Test 001

**Technical contribution candidate**  
**Author:** Darwin Rampai, Independent Researcher  
**Version:** 1.0  
**Date:** 16 July 2026  
**Determination:** PARTIAL  
**Target:** FINOS Common Domain Model, revision `a6ffe777bc12ef3d289579cb3a86d1cbffea63d2`

## 1. Purpose

This test determines whether the inspected FINOS Common Domain Model (CDM)
revision can natively preserve the financial distinctions contained in the
Tokenized Financial Instrument Integrity (TFII) record contract.

The test is not a criticism of CDM. CDM is a transaction-lifecycle standard.
TFII tests a different but adjacent question: whether a tokenized financial
instrument can be bound to its authoritative ownership record, transfer-
effective boundary, correction hierarchy, reconciliation mechanics, evidence
state and permitted-use boundary before downstream financial use.

## 2. Test Rule

A requirement passes only when the inspected CDM revision provides a native,
typed path that preserves the requirement's decisive financial meaning.
Generic taxonomy values, free text, implementation metadata and unmodelled
external conventions do not count as native conformance.

Results are interpreted as follows:

| Result | Meaning |
|---|---|
| `PASS` | Native CDM structure preserves the tested requirement. |
| `PARTIAL` | CDM preserves part of the requirement; a typed extension or external control remains necessary. |
| `FAIL` | No native path was found under the bounded test rule. This is not an allegation that CDM is defective. |
| `UNKNOWN` | The inspected evidence does not support a determination. |

## 3. Sources And Reproducibility

The CDM source was inspected at the fixed Git revision above. The reviewed
Rosetta files cover asset identity, ancillary parties, transfer state,
workflow, valuation, collateral criteria and the collateral eligibility
function. FINOS states that CDM is a machine-readable and machine-executable
model for financial-product and transaction lifecycles and accepts proposals
through its public issue process.

The TFII test vectors are the five public records released with
[*The Token Is Not the Financial Instrument*](https://doi.org/10.5281/zenodo.21399416).
The GDF and ISDA report
[*Unlocking Capital with U.S. Tokenized Money Market Funds for Collateral Mobility*](https://www.gdf.io/wp-content/uploads/2026/07/6.07.26_Unlocking-Capital-with-U.S-Tokenized-Money-Market-Funds-for-Collateral-Mobility.pdf)
supplies the production-use context.

Machine artifacts:

- `tfii-finos-cdm-conformance-test-001.json`
- `tfii-finos-cdm-conformance-test-001.schema.json`
- `validate.py`

## 4. Conformance Matrix

| Requirement | CDM capability | Result | Remaining control |
|---|---|---:|---|
| Financial-object identity | `Asset.Instrument.Security`, identifier, taxonomy and fund type | PASS | None for base identity |
| Record-keeper roles | Transfer agent, registrar, custodian and settlement-centre roles | PASS | Identify which record controls |
| Asset transfer | Typed transfer and payer-receiver relationship | PASS | None for mechanical flow |
| Transfer status | Instructed, pending, disputed, settled and netted states | PASS | Separate status from ownership effect |
| Valuation clock | Amount, timestamp, method/source, scope and timing | PARTIAL | Bind the governing valuation calendar and source |
| Correction lineage | Correct action, prior workflow and event lineage | PARTIAL | Bind correction authority and propagation |
| Collateral schedule | Criteria, inclusion/exclusion, haircut and concentration limits | PASS | Apply record-integrity precondition |
| Authoritative ownership record | Relevant parties can be named | FAIL | Typed ledger/register authority assertion |
| Token or chain role | Security is distinct from `DigitalAsset` | FAIL | Authoritative, integrated, instructive, mirrored or supplementary role |
| Ownership-effective event | Workflow can be timed and settled | FAIL | Instrument-specific ownership boundary |
| Correction hierarchy | Correction action exists | FAIL | Controlling party and record after divergence |
| Reconciliation | No native tokenized-fund record contract found | FAIL | Compared records, cadence, exceptions and correction direction |
| Wallet or holder eligibility | Asset and issuer collateral inputs exist | FAIL | Wallet, allowlist and holder controls |
| Evidence state and Unknowns | Generic metadata and lineage exist | FAIL | Field-level source, locator, status, confidence and Unknown |
| Rights state | No native permitted-use path found | FAIL | Rights-aware lineage and delivery gate |
| Coverage and freshness | Event timing exists | FAIL | Evidence universe, gaps, boundary and freshness receipt |
| Integrity-gated collateral query | Native eligibility function returns criteria match | PARTIAL | Fail-closed TFII precheck before query execution |

The machine-recomputed totals are five `PASS`, three `PARTIAL`, nine `FAIL`
and zero `UNKNOWN` requirements.

## 5. Five Public Test Vectors

The records deliberately contain different ownership and transfer
architectures:

| TFII record | Public transfer boundary | Native CDM result |
|---|---|---:|
| Franklin OnChain U.S. Government Money Fund | Blockchain confirmation after transfer-agent processing | PARTIAL |
| JPMorgan OnChain Liquidity-Token Money Market Fund | Offchain investor-register update | PARTIAL |
| Superstate USTB Money Market Fund | Blockchain confirmation after transfer-agent processing | PARTIAL |
| Invesco Stablecoin Reserves Onchain Fund | UNKNOWN | PARTIAL |
| HSBC Hybrid Gold ETF | Blockchain transfer followed by transfer-agent book entry | PARTIAL |

CDM can represent each instrument and its transaction lifecycle. It does not,
in the inspected revision, natively preserve the decisive rule that explains
why these superficially similar token forms have different ownership and
transfer boundaries.

## 6. Determination

**PARTIAL.** FINOS CDM natively represents the financial instrument, relevant
parties, transfer flow, transfer state, valuation observation, collateral
schedule and lifecycle lineage. TFII's authoritative-record, chain-role,
ownership-effective-event, correction-authority, reconciliation, wallet-
eligibility, evidence-state, rights and coverage controls require an external
precondition or typed extension.

This result does not determine collateral eligibility, provide a legal
opinion, allege a defect in CDM or claim FINOS endorsement.

## 7. Proposed FINOS Work Item

Open a `Proposal` issue in the FINOS CDM repository requesting review of a
record-integrity precondition for tokenized funds. The initial contribution is
the requirement matrix, five public test vectors, JSON Schema and validator.

The requested technical decision is narrow:

> Should authoritative record, token role, ownership-effective event,
> correction authority, reconciliation and evidence state be represented as
> native CDM structures, a standardized extension, or implementation guidance
> applied before `CheckEligibilityByDetails`?

Any specification patch would follow FINOS governance and contributor-license
requirements. This contribution does not presume the answer.

## 8. Validation

Run:

```bash
python3 validate.py
```

The validator checks the JSON Schema, recomputes result counts, binds all test
vectors to the public TFII sample and calculation, resolves every failed
requirement and enforces the claim boundary.
