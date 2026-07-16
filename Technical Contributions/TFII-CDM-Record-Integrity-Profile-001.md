# TFII CDM Record Integrity Profile 001

## 1. Purpose

This profile closes the representational boundary identified by the
TFII-to-FINOS CDM Conformance Test without changing the bounded finding about
native CDM.

- Native FINOS CDM conformance: `PARTIAL`.
- CDM plus the TFII record-integrity profile: `PASS` for representability.
- Actual tokenized-fund collateral admission: `UNKNOWN` until program evidence
  is supplied.

These are three different determinations.

## 2. Profile Function

CDM retains the financial-product, transfer, status, valuation and collateral
mechanics it already represents. TFII adds the evidence-bearing fields needed
to preserve:

- authoritative ownership record;
- record keeper and record role;
- token or ledger role;
- ownership-effective event;
- valuation authority;
- correction authority and lineage;
- reconciliation state;
- wallet and holder controls;
- field-level evidence and Unknowns;
- commercial-use rights;
- point-in-time coverage and freshness; and
- a fail-closed precondition before a CDM eligibility query can run.

No new economic instrument is created. The profile describes the integrity of
the existing financial object and the evidence required to use it.

## 3. Test Result

All seventeen conformance requirements map to either a native CDM path or a
typed TFII profile field. The combined representability result is `PASS`.

All five frozen TFII records validate against the profile. Unknown fields are
accepted only when they are explicit, evidence-bearing and carried into the
collateral gate. The profile therefore does not convert missing evidence into
a favorable determination.

## 4. Admission Boundary

Every public specimen remains blocked before eligibility evaluation because
the following program records are not public:

- governing collateral schedule;
- receiver acceptance;
- live ownership, control and encumbrance state;
- accepted valuation source and exact boundary;
- haircut and concentration limits;
- custody and settlement configuration;
- wallet and holder controls; and
- default access and liquidation procedure.

Consequently, zero CDM eligibility queries are authorized and zero admission
decisions are made. The admission result remains `UNKNOWN`.

## 5. Validation

The validator checks:

1. JSON Schema validity;
2. deterministic replay from the frozen public sample;
3. the exact source-sample hash;
4. seventeen unique requirement mappings;
5. all combined profile requirements passing;
6. evidence assertions on every record;
7. preservation of Unknowns; and
8. fail-closed collateral gates.

Run:

```bash
.venv/bin/python scripts/build_tfii_cdm_record_integrity_profile_001.py
.venv/bin/python scripts/validate_tfii_cdm_record_integrity_profile_001.py
```

## 6. Result

The technical control is complete at the data-contract layer. It can represent
the missing financial-record evidence without weakening CDM or inventing
private facts. Completion of a named collateral determination now requires
the accountable workflow owner to supply or authorize the actual program
records.

