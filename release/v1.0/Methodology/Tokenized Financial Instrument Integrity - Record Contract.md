# Tokenized Financial Instrument Integrity Record Contract 001

**Program:** FET  
**Reference family:** Tokenized Financial Instrument Integrity Reference Family 001  
**Operator:** Darwin Rampai, Independent Researcher  
**Version:** 1.0  
**As of:** 15 July 2026  
**Status:** CONTROLLED TECHNICAL CONTRACT  
**Decision:** D-0059

## 1. Purpose

This contract defines the canonical machine record for the first FET
Reference Integrity family. It tests whether apparently similar tokenized
financial instruments use materially different ownership, transfer,
recordkeeping, reconciliation, correction, timing, and authority
architectures.

The record is designed to prevent a blockchain token balance, transaction, or
label from being treated as complete proof of the financial object it appears
to represent.

## 2. Bounded Proposition

> Similar tokenized-share forms do not establish equivalent ownership,
> transfer-effectiveness, reconciliation, or correction architectures.

The proposition is narrower than a legal classification. It does not claim
that any architecture is invalid, unsafe, misleading, or inferior. It does not
allege wrongdoing and does not recommend an investment or admission decision.

## 3. Integrity Record

One integrity record binds a named financial instrument to:

1. its source-native identity;
2. the registered primary filing;
3. the record described as authoritative;
4. the role played by the blockchain;
5. the event that makes a transfer effective;
6. the entity responsible for recordkeeping;
7. processing and valuation boundaries;
8. wallet eligibility and administrative powers;
9. reconciliation and correction hierarchy;
10. the scope actually covered by the record;
11. calculation applicability;
12. reproducibility state;
13. downstream financial use;
14. rights state;
15. explicit Unknowns; and
16. fixed claim boundaries.

The formal complete-registry schema remains controlled. The bounded public sample preserves the represented field contract.

## 4. Record Fields

| Field | Question answered | Required evidence treatment |
|---|---|---|
| `record_id` | Which stable FET record is this? | Unique controlled identifier |
| `subject` | Which instrument and registrant are under review? | Source-native naming; placeholders remain explicit |
| `source` | Which filing supports the record? | Official URL, accession, form, date, receipt state, retrieval time, content hash, extraction receipt |
| `architecture_class` | Which controlled ownership-record pattern applies? | One enumerated class; not a legal conclusion |
| `financial_object` | What financial object does the filing describe? | Evidence-bearing field |
| `authoritative_record` | Which record controls ownership or entitlement? | Evidence-bearing field |
| `chain_role` | Is blockchain activity authoritative, integrated, instructive, or supplementary? | Evidence-bearing field |
| `transfer_effective_event` | What event makes ownership transfer effective? | Exact clause or `UNKNOWN` |
| `record_keeper` | Which actor maintains the governing record? | Exact entity when available; role-only interpretation otherwise |
| `processing_calendar` | When can the governing record be processed? | Must remain separate from continuous chain operation |
| `wallet_eligibility` | Which wallet or holder controls apply? | Exact eligibility evidence or `UNKNOWN` |
| `administrator_powers` | Who can reject, freeze, reverse, burn, remint, or correct? | Enumerated observed powers only |
| `reconciliation` | How are chain and offchain records compared? | Frequency, direction, exceptions, and Unknowns |
| `correction_hierarchy` | Which record controls after divergence? | Exact hierarchy or bounded interpretation |
| `valuation_clock` | At what boundary is value determined? | Separate from transfer and publication time |
| `coverage_scope` | Which evidence universe is actually covered? | Public filing, private records excluded, and version boundary |
| `calculation_state` | Is a calculation reconstructed in this record? | Explicitly applicable, not applicable, or Unknown |
| `reproducibility_state` | Can another party reproduce the classification? | Receipt, source, private-input, and rights limits |
| `downstream_financial_use` | Which real workflow depends on the record? | Actual use only; possible use is not actual use |
| `rights_state` | What may FET retain, transform, publish, or license? | Rights-aware and use-specific |
| `record_unknowns` | Which required links remain unproved? | Non-empty until complete evidence exists |
| `claim_boundary` | Which conclusions are prohibited? | All four prohibited-claim flags remain false |

## 5. Evidence Object

Every substantive field is a six-part evidence object:

```json
{
  "value": null,
  "evidence_status": "UNKNOWN",
  "source_ids": [],
  "source_locator": "Exact clause not established.",
  "confidence": "Unknown",
  "notes": "The record does not infer the missing value."
}
```

This prevents economic content from being separated from its evidentiary
status.

## 6. Evidence Statuses

| Status | Meaning | Admission rule |
|---|---|---|
| `OBSERVATION` | Directly extracted from a frozen source receipt | Requires a complete immutable retrieval receipt |
| `BOUNDED_INTERPRETATION` | A narrow classification supported by registered evidence | Must identify the source and preserve its limits |
| `INFERENCE` | A reasoned conclusion not directly stated by the source | Must never be presented as observation |
| `UNKNOWN` | Reviewed evidence does not establish the value | Value must be `null`; confidence must be `Unknown` |

No field can be promoted to `OBSERVATION` merely because a document URL is
public. The exact source content must be frozen and locatable.

## 7. Source Receipt States

`PENDING` means the filing is registered, but its exact extraction receipt has
not been frozen. Filing date, retrieval time, content hash, and extraction
receipt remain null.

`COMPLETE` requires:

- filing date;
- UTC retrieval timestamp;
- SHA-256 content hash; and
- a non-empty extraction receipt locating the supporting content.

A pending receipt blocks field-level `OBSERVATION` and blocks public release.

## 8. Architecture Taxonomy

| Class | Controlled meaning |
|---|---|
| `TRANSFER_AGENT_BLOCKCHAIN_INTEGRATED_OFFICIAL_RECORD` | Approved blockchain records operate inside a transfer-agent-controlled official record architecture |
| `BLOCKCHAIN_INSTRUCTION_OFFCHAIN_AUTHORITATIVE_REGISTER` | A blockchain transfer operates as an instruction; the offchain investor register controls the ownership change |
| `UNIFIED_TRANSFER_AGENT_RECORD_WITH_BLOCKCHAIN_COMPONENTS` | Book-entry and blockchain components form one transfer-agent-controlled record |
| `DESIGNATED_BLOCKCHAIN_AND_OFFCHAIN_IDENTITY_REGISTER_JOINT_OFFICIAL_RECORD` | Designated blockchain records and an offchain identity register jointly constitute the official shareholder register, subject to stated controls and exceptions |
| `OFFCHAIN_AUTHORITATIVE_REGISTER_SUPPLEMENTARY_BLOCKCHAIN` | The offchain transfer-agent book is definitive and the blockchain representation is supplementary or correctable |

The taxonomy classifies record architecture. It does not decide the legal
effect of a holder's claim in a jurisdiction.

## 9. Initial Five-Subject Comparison

The five architecture classes remain bounded interpretations supported by
complete normalized filing receipts. They are not legal classifications.

| Record | Subject | Architecture class | Current decisive distinction |
|---|---|---|---|
| FET-TFII-001 | Franklin OnChain U.S. Government Money Fund | Transfer-agent blockchain-integrated official record | Blockchain is described as integrated into transfer-agent recordkeeping |
| FET-TFII-002 | JPMorgan OnChain Liquidity-Token Money Market Fund | Blockchain instruction, offchain authoritative register | Token transfer is treated as an instruction; register update governs the ownership change |
| FET-TFII-003 | Superstate USTB Money Market Fund | Unified transfer-agent record with blockchain components | Book-entry and designated blockchain records operate within one controlled record architecture |
| FET-TFII-004 | Invesco Stablecoin Reserves Onchain Fund | Designated blockchain plus offchain identity register form the joint official record | Blockchain record operation remains subject to stated procedures, allowlisting, and administrative control |
| FET-TFII-005 | HSBC Hybrid Gold ETF | Offchain authoritative register, supplementary blockchain | Offchain transfer-agent book is treated as definitive when records diverge |

This comparison supports the first fracture: identical or similar token form
does not prove identical record authority or transfer effectiveness.

## 10. Coverage And Unknowns

The initial registry covers public filing architecture only. It does not cover:

- transfer-agent or administrator workpapers;
- custodian internal positions;
- unpublished reconciliation exceptions;
- jurisdiction-specific legal opinions;
- private downstream integrations;
- customer contracts; or
- issuer endorsement, trademark rights, and private or non-EDGAR downstream-data rights.

These exclusions are not defects to be silently filled. They are machine-
readable limits on what the record proves.

## 11. Rights Boundary

The SEC's Website Dissemination policy states that sec.gov information may be
copied or further distributed without separate SEC permission. For the five
registered EDGAR filings, this establishes a bounded basis to cite, retain,
transform, display, distribute, and license FET-created factual structure with
attribution.

This basis does not establish SEC or issuer endorsement, trademark permission,
private-record access, or rights to unrelated third-party data. Complete source
filings remain linked to the official SEC archive rather than bundled as the
FET product. The complete determination is recorded in
`docs/reference_data/FET_TFII_SEC_EDGAR_Rights_Basis_001.md`.

## 12. Validation Gates

The validator must fail when:

- the JSON Schema fails;
- record, source, instrument, or Unknown identifiers are duplicated;
- a source ID does not resolve to the official source register;
- a source URL differs from the registered official URL;
- an `UNKNOWN` field carries an asserted value;
- non-Unknown evidence has no source;
- an `OBSERVATION` lacks a complete immutable receipt;
- the five-subject taxonomy collapses into fewer than five classes;
- release is enabled while receipts remain pending;
- commercial delivery is enabled while rights remain unresolved; or
- the embedded validation block disagrees with recomputed state.

Run:

The bounded public calculation can be reproduced with the packaged classification example and the steps in `README.md`. The complete registry validator remains controlled.

## 13. Correction And Version Policy

Corrections must not overwrite history silently.

1. Preserve the original record and receipt.
2. Record the correction source and effective boundary.
3. Identify which fields changed and why.
4. Increment the registry version.
5. Re-run schema, source, rights, and claim-boundary validation.
6. Publish or deliver a correction only within the permitted-use boundary.
7. Record downstream propagation separately from source correction.

A corrected source does not prove that every downstream user adopted the
correction.

## 14. Current Validation Result

As of 15 July 2026:

- records: 5;
- distinct architecture classes: 5;
- evidence-bearing fields: 80;
- direct observations: 44;
- bounded interpretations: 28;
- Unknowns: 8;
- complete normalized filing receipts: 5 of 5;
- public release permitted: no; and
- commercial delivery permitted: no.

The machine contract is valid. The factual records are controlled drafts, not
release-ready assertions.

## 15. Immediate Work Order

1. Transmit the five hash-bound factual-review records only after principal approval.
2. Assign response deadlines only after documented delivery.
3. Adjudicate corrections and disputes against authoritative sources.
4. Record non-response as `NO_RESPONSE_BY_DEADLINE`, never confirmation.
5. Preserve the validated pre-review DOCX, PDF, HTML, machine-readable package,
   and visual-QA record as controlled artifacts.
6. Rebuild the registry and every dependent artifact after accepted corrections.
7. Repeat final factual and visual inspection and freeze the post-review hashes.

No publication or sale is authorized by this technical contract alone.
