# TFII Collateral Admission Control Execution Test 001

## Purpose

This test proves that the admission control executes all three determination
branches. It separates control completeness from evidence completeness.

## Method

Three fixed synthetic vectors carry all twenty-two admission requirements:

1. complete evidence and matching criteria;
2. complete evidence and non-matching criteria; and
3. one mandatory Unknown before the eligibility query.

The criteria evaluator is a bounded Python parity replay of the FINOS CDM
`CheckEligibilityByDetails` and recursive `CheckCriteria` structure at revision
`a6ffe777bc12ef3d289579cb3a86d1cbffea63d2`. It is not generated CDM runtime
and is labelled accordingly.

## Result

- vectors executed: 3;
- completed prechecks: 2;
- held prechecks: 1;
- eligibility reference queries run: 2;
- admission determinations made: 2;
- PASS: 1;
- FAIL: 1;
- UNKNOWN: 1; and
- all execution branches: PASS.

The control is therefore technically executable. The five named public TFII
records still remain `UNKNOWN` because they do not contain receiver-specific
program evidence. Synthetic execution does not change a real instrument's
status.

## Run

```bash
.venv/bin/python scripts/run_tfii_collateral_admission_control_vectors_001.py
.venv/bin/python scripts/validate_tfii_collateral_admission_control_vectors_001.py
```

