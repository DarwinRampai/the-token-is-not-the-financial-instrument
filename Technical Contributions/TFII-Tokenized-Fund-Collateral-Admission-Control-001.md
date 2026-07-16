# TFII Tokenized-Fund Collateral Admission Control 001

**Technical contribution candidate**  
**Author:** Darwin Rampai, Independent Researcher  
**Version:** 1.0  
**Date:** 16 July 2026  
**Public-evidence determination:** UNKNOWN

## 1. Purpose

This control prevents a tokenized fund from entering a collateral eligibility
calculation merely because its token can move, its underlying fund appears on
an eligible list, or its asset and issuer attributes match a collateral
schedule.

It adds a fail-closed record-integrity precheck before FINOS CDM
`CheckEligibilityByDetails`. It does not replace CDM, determine legal effect,
approve collateral, assign a risk score or authorize execution.

## 2. The Production Gap

The 2026 GDF and ISDA U.S. tokenized-money-market-fund report identifies the
right production questions: authoritative ownership records, transfer
effectiveness, settlement finality, wallet controls, reconciliation, accepted
valuation and haircut treatment, product-level acceptance, and default access.

Its sandbox was not an admission test. The report states that:

- all instruments were test assets;
- no real fund interests were transferred;
- no legal obligations were created;
- every instrument was priced at one dollar per token;
- a standard haircut was applied; and
- the eligible-asset list was pre-agreed.

Those assumptions are appropriate for workflow simulation. They remove the
evidence questions that must be answered before production collateral use.

## 3. Control Sequence

```text
exact instrument identity
        |
        v
authoritative record and transfer boundary
        |
        v
correction, reconciliation, wallet and valuation controls
        |
        v
program-specific schedule, acceptance, position and haircut evidence
        |
        v
FINOS CDM collateral eligibility query
        |
        v
independent legal, operational and risk approval
```

Any missing mandatory input returns `HOLD_MISSING_EVIDENCE`. The CDM query is
not run, and the financial determination remains `UNKNOWN`.

## 4. Architecture-Integrity Requirements

The first layer requires:

1. exact financial-object identity;
2. ownership-record architecture;
3. authoritative ledger, register or book;
4. blockchain role;
5. ownership-effective event;
6. governing record keeper;
7. processing calendar;
8. correction hierarchy;
9. reconciliation cadence and direction;
10. wallet and holder controls;
11. valuation boundary and source;
12. source and downstream-use rights; and
13. explicit coverage and Unknowns.

This layer establishes what the instrument is and how its records operate. It
does not establish that a specific collateral receiver has accepted it.

## 5. Program-Specific Admission Requirements

The second layer requires evidence that is specific to the actual collateral
program and decision boundary:

1. governing collateral agreement or eligible schedule;
2. receiver, CCP, custodian or secured-party acceptance;
3. live position, owner, control and encumbrance state;
4. accepted and fresh valuation;
5. applicable haircut or margin percentage;
6. concentration limits;
7. custody, control and any required perfection conditions;
8. default access and liquidation mechanics; and
9. exact-boundary freshness for every input.

These inputs cannot be inferred from a public token label or general fund
prospectus.

## 6. Public Five-Instrument Run

The control was run against the five public TFII records.

| Instrument | Architecture precheck | Program evidence | CDM query | Determination |
|---|---:|---:|---:|---:|
| Franklin OnChain U.S. Government Money Fund | PARTIAL | UNKNOWN | NOT RUN | UNKNOWN |
| JPMorgan OnChain Liquidity-Token Money Market Fund | PARTIAL | UNKNOWN | NOT RUN | UNKNOWN |
| Superstate USTB Money Market Fund | PARTIAL | UNKNOWN | NOT RUN | UNKNOWN |
| Invesco Stablecoin Reserves Onchain Fund | PARTIAL | UNKNOWN | NOT RUN | UNKNOWN |
| HSBC Hybrid Gold ETF | PARTIAL | UNKNOWN | NOT RUN | UNKNOWN |

Aggregate result:

- instruments tested: 5;
- complete architecture prechecks: 0;
- partial architecture prechecks: 5;
- ready for CDM eligibility query: 0;
- held for missing evidence: 5;
- CDM queries run: 0;
- admission decisions made: 0; and
- external determination: `UNKNOWN`.

## 7. Interpretation

The result does **not** mean that all five instruments are ineligible or unsafe.
It means that the public evidence package does not establish enough
instrument-integrity and program-specific evidence to make a collateral
admission determination.

This is the control's intended behavior. `UNKNOWN` prevents a technically
movable token and a criteria match from being silently promoted into a claim
of legally effective, operationally controllable and financially admitted
collateral.

## 8. FINOS CDM Integration Point

The inspected CDM revision can represent an eligible-collateral specification,
asset and issuer query, haircut, concentration limit and boolean criteria
match. The TFII control sits immediately before that query:

```text
if TFII integrity precheck != PASS:
    do not invoke CheckEligibilityByDetails
    return UNKNOWN with missing-evidence schedule
else:
    invoke CheckEligibilityByDetails
    preserve both receipts for independent approval
```

The contribution question is whether this precondition belongs in CDM as a
native structure, a standardized extension, or implementation guidance.

## 9. GDF Relevance

The control operationalizes three issues stated in the GDF/ISDA report:

- tokenization does not bypass existing eligibility, custody, haircut,
  valuation or re-use rules;
- finality differs across digital-native, digital-twin and custodial models;
  and
- production adoption requires product-level acceptance and standardized
  controls beyond a sandbox's pre-agreed inputs.

It supplies a reproducible public precheck that can be applied before a future
live-production simulation.

## 10. Machine Artifacts

- `tfii-tokenized-fund-collateral-admission-control-001.json`
- `tfii-tokenized-fund-collateral-admission-control-001.schema.json`
- `validate.py`

Run:

```bash
python3 validate.py
```

## 11. Claim Boundary

No instrument is declared eligible or ineligible. No legal opinion, risk
score, investment recommendation or execution authority is produced. A later
production run requires authorized program-specific evidence and independent
legal, operational and risk approval.
