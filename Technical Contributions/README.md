# Tokenized-Fund Record Integrity And Collateral Admission

**Contributor:** Darwin Rampai, Independent Researcher  
**Published:** 16 July 2026  
**Source paper:** [The Token Is Not the Financial Instrument](https://doi.org/10.5281/zenodo.21399416)

This directory contains four executable technical contributions.

## 1. TFII-to-FINOS CDM Conformance Test 001

The test asks whether the inspected FINOS Common Domain Model revision can
natively preserve the financial distinctions in a Tokenized Financial
Instrument Integrity record.

Result:

- requirements: 17;
- PASS: 5;
- PARTIAL: 3;
- FAIL: 9;
- UNKNOWN: 0; and
- overall determination: **PARTIAL**.

CDM represents the instrument, parties, transfer workflow, valuation,
collateral criteria and lineage. The inspected revision does not natively
preserve authoritative-record, token-role, ownership-effective-event,
correction-authority, reconciliation, wallet-control, evidence-state, rights
and coverage controls.

`FAIL` means no native typed path was found under the published test rule. It
does not allege that CDM is defective.

## 2. TFII CDM Record Integrity Profile 001

The profile adds typed, evidence-bearing fields for the nine missing native
control areas and completes the three partial areas without changing CDM's
native result.

Result:

- native CDM: **PARTIAL**;
- CDM plus TFII record-integrity profile: **PASS**;
- profile-valid public records: 5 of 5; and
- private facts inferred: 0.

The `PASS` is a representability result. It means the combined data contract
can carry every required field, including explicit Unknowns. It is not a
collateral admission decision.

## 3. TFII Collateral Admission Control Execution Test 001

Three fixed synthetic vectors execute the complete control:

- complete, matching evidence: `PASS`;
- complete, non-matching evidence: `FAIL`;
- missing mandatory evidence: `UNKNOWN`;
- eligibility reference queries run: 2; and
- all execution branches: **PASS**.

The evaluator is explicitly labelled as a bounded parity replay of FINOS CDM
criteria logic, not generated CDM runtime and not a real-instrument decision.

## 4. TFII Tokenized-Fund Collateral Admission Control 001

The control applies a fail-closed integrity precheck before a FINOS CDM
collateral eligibility query.

Public-evidence result:

- instruments: 5;
- partial architecture prechecks: 5;
- ready for CDM eligibility query: 0;
- held for missing evidence: 5;
- CDM queries run: 0;
- admission decisions made: 0; and
- external determination: **UNKNOWN**.

This does not declare any instrument eligible, ineligible, safe or unsafe. It
shows that public token and filing evidence alone does not establish the
program-specific evidence required for a real collateral admission decision.

## Contents

- [FINOS issue 4956 five-minute agenda decision brief](FINOS-CDM-Issue-4956-Agenda-Decision-Brief.md)
- [Conformance test specification](TFII-to-FINOS-CDM-Conformance-Test-001.md)
- [Conformance result](tfii-finos-cdm-conformance-test-001.json)
- [Conformance JSON Schema](tfii-finos-cdm-conformance-test-001.schema.json)
- [CDM record-integrity profile specification](TFII-CDM-Record-Integrity-Profile-001.md)
- [CDM record-integrity profile](tfii-cdm-record-integrity-profile-001.json)
- [CDM record-integrity profile JSON Schema](tfii-cdm-record-integrity-profile-001.schema.json)
- [Admission execution test specification](TFII-Collateral-Admission-Control-Execution-Test-001.md)
- [Admission execution vectors](tfii-collateral-admission-control-vectors-001.json)
- [Admission execution-vector JSON Schema](tfii-collateral-admission-control-vectors-001.schema.json)
- [Collateral control specification](TFII-Tokenized-Fund-Collateral-Admission-Control-001.md)
- [Collateral control result](tfii-tokenized-fund-collateral-admission-control-001.json)
- [Collateral control JSON Schema](tfii-tokenized-fund-collateral-admission-control-001.schema.json)
- [Public TFII fixture](fixtures/TFII-Public-Sample-v1.0.json)
- [Transfer-boundary fixture](fixtures/Transfer-Boundary-Classification-v1.0.json)
- [Validator](validate.py)

## Validate

```bash
python3 -m pip install -r requirements.txt
python3 validate.py
```

Expected output:

```text
PASS conformance test: PARTIAL
PASS CDM plus TFII record-integrity profile: PASS
PASS collateral admission execution branches: PASS
PASS collateral admission control: UNKNOWN
```

## Claim Boundary

These artifacts do not provide a legal opinion, collateral approval, risk
score, investment recommendation, automated execution authority or endorsement
by FINOS, GDF, ISDA or any named issuer.

## Controlled Inspection

A named instrument and named collateral workflow can be inspected using
buyer-supplied or buyer-authorized program records. The controlled inspection
is USD 3,000 prepaid and separate from this public contribution. Delivery is
targeted within three business days after payment and complete authorized
inputs. [Open the exact scope and intake instructions](../PRODUCTION_INSPECTION.md).
