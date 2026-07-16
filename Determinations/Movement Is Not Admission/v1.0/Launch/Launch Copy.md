# Public Release Copy

## Primary Notice

Movement is not admission.

The July 2026 GDF and ISDA tokenized-money-market-fund sandbox moved test
collateral through an orchestrated workflow. It also assumed the production
admission decision: test assets, no legal obligations, fixed USD 1 values, one
standard haircut, and a pre-agreed eligible list.

I tested the missing boundary.

Native FINOS CDM: 5 PASS / 3 PARTIAL / 9 FAIL.  
CDM plus the TFII Record Integrity Profile: 17 / 17 PASS.  
Admission control: PASS, FAIL, and UNKNOWN branches executed.  
Five public tokenized-fund records: 5 UNKNOWN / 0 admission decisions
manufactured.

The supported conclusion is exact: the sandbox moved collateral; it did not
test whether a real tokenized fund should be admitted.

This is not an allegation that the sandbox was improper or that any named
instrument is unsafe. It is a reproducible determination of what the public
exercise proved, assumed, and left untested.

Technical determination and evidence:
https://github.com/DarwinRampai/the-token-is-not-the-financial-instrument/releases/tag/movement-is-not-admission-v1.0.0

Corrections and production inspection: rampaidarwin@gmail.com

## Technical Follow-Up

The control is fail-closed. Complete matching evidence returns PASS. Complete
non-matching evidence returns FAIL. Missing mandatory evidence returns UNKNOWN
before the eligibility query runs.

The next valid test is one real proposed instrument, one actual receiver
schedule, and authorized ownership, control, valuation, custody,
reconciliation, and default-access records.

Production inspection is USD 3,000 prepaid. The resulting receipt remains
bounded to the supplied workflow and evidence boundary.
