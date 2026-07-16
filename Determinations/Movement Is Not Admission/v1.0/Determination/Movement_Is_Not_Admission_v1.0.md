# Abstract

The July 2026 Global Digital Finance and ISDA tokenized-money-market-fund sandbox demonstrated that test collateral could move through an orchestrated workflow. It did not establish the admission boundary for a live financial instrument. The published exercise used test assets, created no legal obligations, fixed every token at one United States dollar, applied a standard haircut, and used an eligible list agreed in advance. This determination tests the missing boundary in three stages. First, seventeen financial-record requirements were mapped against the inspected FINOS Common Domain Model revision. Native representation was partial: five requirements passed, three were partial, and nine failed the published native-path test. Second, a TFII record-integrity profile represented all seventeen requirements across five public tokenized-fund records without inferring private facts. Third, a fail-closed admission control executed PASS, FAIL, and UNKNOWN branches. When applied to the five public records, every instrument remained UNKNOWN because receiver-specific ownership, control, reconciliation, valuation, haircut, custody, and default-access evidence was unavailable. The supported conclusion is narrow: successful collateral movement under assumed eligibility is not proof of production admission.

::: {custom-style="FET Principal Finding"}
**PRINCIPAL FINDING.** The sandbox demonstrated movement under assumed eligibility. It did not test whether a live tokenized fund satisfied the production admission boundary.
:::

# 1. Claim

The inspected tokenized-money-market-fund sandbox demonstrated collateral movement and workflow orchestration under a bounded set of simplifying assumptions. It did not prove that any live tokenized fund was legally effective, operationally controllable, financially valued, and accepted under a receiver's production collateral schedule.

The distinction matters because a token can move while the financial object represented by that token remains subject to a different authoritative ownership record, transfer-effective event, correction hierarchy, reconciliation process, valuation boundary, custody arrangement, or receiver-specific eligibility rule.

# 2. Determination

**SUPPORTED.** The public record supports the statement that the sandbox tested movement while assuming the admission decision.

The public record does not support any broader statement that the sandbox approved, rejected, validated, or invalidated a live financial instrument for production collateral use. It also does not support a claim that any participating organization acted improperly.

The external determination for the five real public TFII records is **UNKNOWN**. UNKNOWN is not a euphemism for unsafe and is not a finding of ineligibility. It means the reviewed evidence does not establish the mandatory facts required to make the decision.

# 3. Proof-Layer Result

The determination separates four proof layers that should not be collapsed.

| Proof layer | Test | Result | Meaning |
|---|---:|---:|---|
| Workflow movement | Published sandbox | OBSERVED | Test collateral moved through the demonstrated workflow. |
| Native record representation | 17 FINOS CDM requirements | PARTIAL | Five passed, three were partial, and nine had no native typed path under the published test rule. |
| Extended record representation | CDM plus TFII profile | PASS | All seventeen requirements were representable across five records while preserving Unknowns. |
| Production admission | Five public instruments | UNKNOWN | Receiver-specific program evidence was unavailable, so zero real admission queries ran. |

The native CDM result is not rewritten by the profile. The profile is an extension that carries financial-record integrity fields CDM did not natively preserve under the inspected revision and test rule.

![The production admission boundary](../figures/Movement_Is_Not_Admission_Control_001.svg)

# 4. Material Evidence

## 4.1 The sandbox assumed eligibility

The GDF and ISDA report records six assumptions that remove the production admission question from the demonstrated workflow:

1. all instruments were test assets;
2. no real fund interests were transferred;
3. no legal obligations were created;
4. every instrument was priced at one dollar per token;
5. one standard haircut was applied; and
6. the eligible-asset list was agreed in advance by pledgor and receiver.

Those assumptions are legitimate for a workflow simulation. They are also the reason the simulation cannot be treated as evidence that a live instrument satisfies a production admission boundary.

## 4.2 Native representation was partial

Seventeen requirements were tested against FINOS CDM revision `a6ffe777bc12ef3d289579cb3a86d1cbffea63d2`. CDM represented instrument identity, parties, transfer workflow, collateral criteria, valuation concepts, and lineage. Under the published test rule, it did not natively preserve nine control areas, including authoritative-record identity, token role, ownership-effective event, correction authority, reconciliation, wallet control, evidence state, rights, and coverage.

The result is a conformance observation, not an allegation that CDM is defective. A standard can be intentionally extensible and still require an explicit profile before a particular financial use is safe to represent.

## 4.3 The combined record contract closed representation gaps

The TFII Record Integrity Profile added typed, evidence-bearing fields for the missing and partial control areas. All seventeen requirements were represented across the five public records. Five of five records validated against the profile. Private facts were not guessed. Missing evidence remained explicitly UNKNOWN.

This PASS establishes representability only. A complete schema does not manufacture complete evidence and does not authorize collateral use.

## 4.4 The control executed all decision branches

Three fixed synthetic vectors executed the admission control:

- complete evidence with matching criteria returned PASS;
- complete evidence with non-matching criteria returned FAIL; and
- missing mandatory custody and control evidence returned UNKNOWN before query execution.

Two bounded eligibility-reference queries ran. The incomplete vector was blocked before query. The evaluator is a bounded Python parity replay of FINOS CDM criteria logic, not generated CDM runtime and not a live-instrument decision.

## 4.5 Five real records stopped at the boundary

The control then assessed the public TFII records for Franklin Templeton, JPMorgan, Superstate, Invesco, and HSBC. Every architecture precheck was partial. None contained the receiver-specific program evidence required to proceed. Zero CDM eligibility queries ran, and zero admission decisions were manufactured.

# 5. Material Unknowns

The following evidence remains Unknown for each proposed real production workflow unless supplied by an authorized party:

- the governing collateral agreement or eligible schedule;
- receiver, secured-party, custodian, or CCP acceptance;
- exact position, owner, control, and encumbrance state;
- accepted valuation source and freshness rule;
- applicable haircut and concentration limits;
- custody, control, and any perfection conditions;
- reconciliation between token, fund entitlement, and collateral records;
- default access and liquidation mechanics; and
- the exact observation boundary for each input.

These facts cannot be inferred from a token label, prospectus, public wallet balance, or generic eligible-asset category.

# 6. Financial Consequence

The control addresses a specific operational risk: a technically movable token or an asset-category match can be promoted into an admission claim without proving the records and rights that make the collateral usable by a particular receiver.

No realized loss or observed production admission failure is claimed in this determination. The consequence established here is a decision-control boundary. Without the precheck, incomplete evidence can reach criteria matching. With the precheck, missing mandatory facts return UNKNOWN and the query does not run.

# 7. Scope Boundary

This determination is not a legal opinion, audit, collateral approval, risk score, investment recommendation, trading signal, or allegation of wrongdoing. It does not claim endorsement by FINOS, GDF, ISDA, Ownera, any issuer, or any collateral receiver.

The test is bounded to the cited GDF and ISDA report, the inspected FINOS CDM revision, five public TFII records, the published profile, and three synthetic execution vectors. Private production records were excluded because they were not available through an authorized route.

# 8. Production Inspection

A production inspection requires one named instrument, one pledgor and receiver workflow, the actual admission schedule, and authorized operating records. The output is a machine-readable integrity receipt, eligibility determination or evidence hold, Unknown register, and calculation hashes.

The public materials establish the method and the fail-closed behavior. Complete maintained records, implementation, private inputs, and buyer-specific outputs remain controlled. Production inspection is prepaid and governed by written terms.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# 9. Conclusion

Movement is observable. Admission is a separate financial determination.

The sandbox proved that test collateral could move through an orchestrated process under agreed assumptions. The combined CDM and TFII profile proved that the required record distinctions can be represented. The execution vectors proved that the control can return PASS, FAIL, and UNKNOWN. The five public live-instrument records proved that the control stops when production evidence is absent.

The supported public conclusion is therefore exact: **the sandbox moved collateral; it did not test whether a real tokenized fund should be admitted.**

# References

Global Digital Finance and International Swaps and Derivatives Association. 2026. *Unlocking Capital with U.S. Tokenized Money Market Funds for Collateral Mobility*. https://www.gdf.io/wp-content/uploads/2026/07/6.07.26_Unlocking-Capital-with-U.S-Tokenized-Money-Market-Funds-for-Collateral-Mobility.pdf.

FINOS. 2026. *Common Domain Model*. Revision `a6ffe777bc12ef3d289579cb3a86d1cbffea63d2`. https://github.com/finos/common-domain-model.

Rampai, Darwin. 2026. *The Token Is Not the Financial Instrument: Five Tokenized Funds, Five Record Architectures, and the Control Boundary Between Blockchain Transfer and Financial Ownership*. Version 1.0. https://doi.org/10.5281/zenodo.21399416.

Rampai, Darwin. 2026. "Tokenized-Fund Record Integrity and Collateral Admission." Public technical contribution. https://github.com/DarwinRampai/the-token-is-not-the-financial-instrument/tree/main/Technical%20Contributions.
