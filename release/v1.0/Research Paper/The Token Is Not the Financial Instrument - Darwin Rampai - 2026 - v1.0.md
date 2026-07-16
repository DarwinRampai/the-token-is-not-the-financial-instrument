# Abstract

A token balance does not, by itself, identify the financial instrument, the
record that governs ownership, the event that makes a transfer effective, or
the process that corrects a divergence. This paper tests that proposition
against five United States primary filings covering tokenized money-market-fund
and gold-fund shares. The filings disclose five distinct record architectures:
a transfer-agent blockchain-integrated official record; a blockchain
instruction with an offchain authoritative register; a unified transfer-agent
record with blockchain components; a joint designated-blockchain and offchain
identity register; and an offchain authoritative register with a supplementary
blockchain. The controlled registry contains 44 direct observations, 28 bounded
interpretations, and eight explicit Unknown fields. A separate Franklin
Templeton evidence chain connects the record problem to an active financial
workflow: issuer-reported BENJI peer-to-peer transfers above USD 211 million and
a live institutional collateral program for Benji-issued tokenized
money-market-fund shares. The evidence establishes platform-level financial
consequence, not exact fund exposure or control failure. The contribution is a
reproducible integrity record that keeps token form, financial object,
authoritative record, transfer boundary, reconciliation, correction, valuation,
downstream use, and Unknowns separate.

**Principal finding.** Within the five filings, similar tokenized-share forms
do not establish equivalent ownership, transfer-effectiveness, reconciliation,
or correction architectures. The token is one component of the financial
record. It is not sufficient evidence of the complete financial instrument.

# 1. Research Context

Tokenization compresses a complex financial instrument into a visible digital
object. A wallet shows a token. A block explorer shows a transfer. A contract
shows a balance. Those observations are useful, but they do not answer every
question required for ownership, valuation, collateral, accounting, custody,
or correction.

The missing questions are operational rather than philosophical:

1. Which record is authoritative when a blockchain and an offchain register
   differ?
2. Does a blockchain transaction transfer ownership, submit an instruction, or
   update only a supplementary representation?
3. When does the ownership change become effective?
4. Which actor may reject, reverse, claw back, burn, mint, or correct the
   record?
5. How and when are blockchain and offchain representations reconciled?
6. Which valuation clock controls a downstream financial use?
7. What happens when a correction does not propagate to custody, collateral,
   accounting, or settlement systems?

These questions cannot be answered from token form alone. They require the
instrument's source-native record architecture.

This study does not claim that tokenization is defective. It tests a narrower
problem: whether five instruments that can all be described publicly as
tokenized shares use the same ownership and control system. They do not.

# 2. The Representation Error

The recurring representation error is simple:

> blockchain token observed -> financial instrument understood

The first statement may be true while the second remains unproved. A token can
operate as an official record component, an instruction to a transfer agent, a
joint register component, or a supplementary mirror. The same visible token
form can therefore carry different financial meaning.

The relevant distinction is not onchain versus offchain. It is authoritative
versus non-authoritative, effective versus instructive, reconciled versus
unreconciled, and current versus stale. A financial user needs the complete
record chain, not merely the most visible component.

This matters to more than fund administration. A custodian must know which
record proves the asset held. A collateral controller must know when a transfer
or correction changes eligible collateral. An accountant must know which
position controls the books. A risk engine must know which time boundary and
valuation input apply. A data provider must avoid normalizing different native
meanings into one false category.

# 3. Method

## 3.1 Subject selection

The study uses five primary filings selected for record-architecture diversity,
not statistical representativeness:

1. Franklin OnChain U.S. Government Money Fund;
2. JPMorgan OnChain Liquidity-Token Money Market Fund;
3. Superstate USTB Money Market Fund;
4. Invesco Stablecoin Reserves Onchain Fund; and
5. HSBC Hybrid Gold ETF.

The sample spans registered money-market funds, a tokenized stablecoin-reserve
fund structure, and a proposed hybrid gold ETF. It is bounded to the filing
versions cited in the references.

## 3.2 Canonical record contract

Each instrument is represented through the same 16 evidence-bearing fields:

| Record domain | Required content |
|---|---|
| Identity | source-native instrument and registrant |
| Authority | authoritative record, record keeper, administrator powers |
| Transfer | chain role, transfer-effective event, processing calendar |
| Access | wallet and holder eligibility |
| Integrity | reconciliation and correction hierarchy |
| Valuation | valuation clock and calculation applicability |
| Scope | coverage, reproducibility, downstream use, and rights |

Every field carries a value, evidence status, source identifier, source
locator, confidence, and notes. The accepted evidence statuses are
`OBSERVATION`, `BOUNDED_INTERPRETATION`, `INFERENCE`, and `UNKNOWN`. An Unknown
cannot carry an asserted value.

## 3.3 Source and rights boundary

The core sample uses five SEC EDGAR filings and one admitted Franklin Templeton
regulatory supplement. The SEC states that information on sec.gov is public and
may be copied or further distributed without separate SEC permission, subject
to attribution and restrictions on marks and implied approval (SEC 2026). The
public unit is FET-created structure, classification, and bounded quotation. It
is not a repackaged source archive. The issuer-hosted supplement is cited and
normalized, not redistributed.

Two official Franklin Templeton announcements support the downstream-use
analysis. Those sources are cited and normalized, but not redistributed. No
private transfer-agent workpapers, customer records, custodian positions,
collateral balances, or legal opinions are included.

The Invesco architecture is bound to the 9 July 2026 replacement filing. A
same-day withdrawal filing identifies the earlier amendment as withdrawn and
states that no securities were issued or sold under the withdrawn amendments
(Short-Term Investments Trust 2026a, 2026b). The study therefore treats the
fund as a proposed architecture and does not claim live issuance or use.

## 3.4 Validation

The controlled registry is validated against a formal JSON Schema. The
validator rejects duplicate identifiers, unresolved source IDs, changed source
URLs, missing receipt hashes, asserted values inside Unknown fields, unsupported
observations, collapsed architecture classes, and premature public or
commercial release states.

The current registry contains:

| Evidence state | Fields |
|---|---:|
| Direct observations | 44 |
| Bounded interpretations | 28 |
| Explicit Unknowns | 8 |
| Total evidence-bearing fields | 80 |

# 4. Findings

## 4.1 Five visible token forms, five record architectures

The five filings do not describe one common tokenized-share architecture.

![Figure 1. Five source-native record architectures found in the reviewed primary filings.](../Public%20Evidence/Tokenized%20Financial%20Instrument%20Architecture%20Comparison%20-%20v1.0.svg)

The decisive differences are summarized below.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

| Instrument | Authoritative record | Transfer boundary | Reconciliation state |
|---|---|---|---|
| Franklin OnChain U.S. Government Money Fund | Transfer-agent-maintained blockchain-integrated official record | Relevant blockchain confirmation after transfer-agent processing | Public interval and complete procedure Unknown |
| JPMorgan OnChain Liquidity-Token Money Market Fund | Offchain Investor Register | Transfer-agent processing and Investor Register update | Register controls; subsequent blockchain transactions restore alignment |
| Superstate USTB Money Market Fund | Unified transfer-agent record spanning designated blockchains and book entry | Relevant blockchain confirmation after transfer-agent processing | Unified-record structure observed; frequency and exception procedure Unknown |
| Invesco Stablecoin Reserves Onchain Fund | Designated blockchain records plus offchain identity register jointly form official register | Exact event Unknown | Interval and exception procedure Unknown |
| HSBC Hybrid Gold ETF | Transfer-agent offchain book | Blockchain execution followed by reflection on transfer-agent books | At least daily comparison and corrective entries |

The visible token does not reveal which row applies. That information lives in
the governing record and operating rules.

## 4.2 Blockchain confirmation has different meanings

Franklin and Superstate describe a peer-to-peer transfer as complete upon
confirmation on the relevant approved blockchain after transfer-agent
processing (Franklin Templeton Trust 2025; Superstate Trust 2025). That is not a
universal tokenization rule.

JPMorgan describes token transfer as an instruction. The offchain Investor
Register is determinative, and ownership changes after transfer-agent
processing and register update. A transfer received before 9:00 p.m. Eastern on
a business day may enter that day's update; a later transfer waits for the next
business-day update (JPMorgan Trust IV 2026).

The HSBC filing describes blockchain execution followed by reflection on the
transfer agent's books, while calling the offchain book definitive evidence of
ownership (HSBC Physical Gold Trust 2026). Invesco describes a joint official
register but does not identify whether blockchain confirmation, transfer-agent
acceptance, joint-register update, or another event is the exact
transfer-effective boundary (Short-Term Investments Trust 2026a).

One block explorer status can therefore correspond to at least four different
record meanings in this sample: completion, instruction, first step in a
two-step process, or an unresolved boundary.

## 4.3 Correction authority is part of the instrument

Record correction is not an implementation footnote. It determines which state
survives an error, dispute, unauthorized transaction, or divergence.

The JPMorgan filing states that the Investor Register controls when token
balances diverge, with later blockchain transactions used to restore alignment.
The Superstate filing describes subsequent-block correction without deleting
prior blockchain activity. The HSBC filing describes at-least-daily
reconciliation and corrective mint, burn, reallocation, or appended entries.
The Invesco filing permits transfer rejection or suspension and describes a
general transaction-correction process, but the propagation path between the
blockchain and offchain register components is not stated in the reviewed text.

A data system that records only token transfers can preserve transaction
history while losing the current authoritative result. Event history is not a
substitute for the governing corrected state.

## 4.4 Valuation and transfer do not share one clock

The sample also rejects the assumption that continuous token movement implies
continuous authoritative valuation.

Effective on or about 18 May 2026, Franklin normally calculates NAV hourly from
8:00 a.m. Eastern time until its normal 5:00 p.m. Eastern close on days when
both the NYSE and the Federal Reserve Bank of New York are open, subject to
omitted intraday calculations and early-close conditions. This superseded the
older single daily valuation boundary captured in the initial TFII record.
JPMorgan calculates Token Class NAV at stated cut-off times on days the fund
accepts orders. Superstate calculates NAV when a properly formed purchase or
redemption request is received, including outside ordinary business hours.
Invesco prices accepted purchase and redemption orders at the next determined
NAV and calculates amortized-cost deviation daily. HSBC uses the earlier of the
day's LBMA Gold Price PM or 12:00 p.m. New York time, subject to a fallback.

Transfer time, ownership-effective time, valuation time, and publication time
are separate boundaries. Collapsing them can create a precise but false
point-in-time record.

# 5. The Financial Consequence

The record distinction becomes financially consequential when represented
shares support another workflow.

Franklin Templeton reports more than USD 211 million of cumulative BENJI
peer-to-peer transfer volume through 31 March 2026. A separate Franklin
Templeton and Binance announcement describes a live institutional program in
which eligible clients may use Benji-issued tokenized money-market-fund shares
as off-exchange collateral while the assets remain in Ceffu-supported custody
and their value is mirrored in the Binance trading environment (Franklin
Templeton 2026a, 2026b).

![Figure 2. Bounded Franklin and BENJI record-to-custody-to-collateral control chain. Solid lines show observed or bounded links; dashed lines show undisclosed interfaces and Unknowns.](../Public%20Evidence/Franklin%20BENJI%20Financial%20Control%20Chain%20-%20v1.0.svg)

The announcement does not disclose the exact participating fund, share class,
balance, client, haircut, valuation hierarchy, stale-value rule, default path,
or correction interface. The evidence therefore supports platform-level use,
not exact fund exposure.

That boundary is the result, not an inconvenience. The public record proves
that tokenized fund shares participate in transfer and collateral workflows.
It does not prove how an ownership correction, freeze, custody discrepancy, or
valuation change propagates through the complete collateral system.

Once a represented share supports trading collateral, five integrity controls
become financially material:

1. asset identity must match the eligible fund and share class;
2. custody state must reconcile with the authoritative ownership record;
3. transfer and correction events must propagate to the collateral controller;
4. mirrored value must use a defined input, time boundary, haircut, and stale
   policy; and
5. default and release processes must identify which record controls.

No failure is required for those controls to matter. The dependency itself
creates the control requirement.

# 6. A Financial Instrument Integrity Record

The practical response is not another dashboard label. It is a maintained
integrity record that binds each financial object to its native authority and
time boundaries.

The minimum record contains:

1. source-native instrument identity;
2. authoritative ownership or entitlement record;
3. blockchain role;
4. transfer-effective event;
5. responsible record keeper and administrator powers;
6. processing and valuation clocks;
7. reconciliation direction and frequency;
8. correction hierarchy;
9. downstream financial use;
10. source and calculation provenance;
11. rights and permitted-use state;
12. explicit Unknowns; and
13. correction and version history.

This record does not replace the transfer agent, custodian, administrator,
legal adviser, auditor, or risk owner. It makes their distinct claims and
interfaces visible without treating one source as proof of another.

The machine contract matters because narrative diligence decays. A filing can
change. A product can add a network. A transfer rule can be amended. A public
Unknown can become known. A downstream user can depend on a stale
classification. The integrity record must therefore be versioned, monitored,
and corrected rather than published once and abandoned.

# 7. Implications

## 7.1 Issuers and transfer agents

An issuer can use the record to show exactly what its token does and does not
prove. Transfer agents can expose authoritative-state, processing, and
correction boundaries without representing every private workpaper publicly.

## 7.2 Custodians, collateral systems, and exchanges

These users need more than token possession. They need instrument identity,
eligibility, ownership authority, reconciliation, valuation, correction, and
release interfaces. A wallet balance can be necessary evidence while remaining
insufficient control evidence.

## 7.3 Data and benchmark providers

Normalization should preserve native financial meaning. A field called
`tokenized_share_balance` is unsafe if one source represents an authoritative
record, another an instruction, and another a supplementary mirror. The data
contract must carry architecture and evidence metadata with the quantity.

## 7.4 Funds, auditors, and risk functions

Point-in-time holdings, valuation, and collateral reviews require the governing
record at the relevant boundary. Event-derived reconstruction can support
history, but it cannot silently replace corrected authoritative state.

## 7.5 Programmable finance

Smart contracts cannot infer the legal and operational meaning of an input
from its token interface. If a financial workflow depends on tokenized
instruments, the dependency needs an explicit integrity record or an equivalent
control supplied by the responsible institutions.

# 8. Limitations

The study has five principal limitations.

1. The sample is purposive and contains only five United States filings. It
   does not estimate the prevalence of any architecture across tokenized
   finance.
2. Filing language is evidence of the disclosed architecture, not an
   independent legal opinion about ownership in every jurisdiction or dispute.
3. Private transfer-agent workpapers, reconciliation logs, administrator
   records, customer positions, collateral balances, and contractual control
   procedures were not available.
4. The USD 211 million transfer amount is issuer-reported and was not
   independently reconciled by FET.
5. The collateral evidence establishes a Benji platform-level program. It does
   not establish that the Franklin OnChain U.S. Government Money Fund or any
   specific share class was pledged.

Eight registry fields remain Unknown. The most material are Invesco's exact
transfer-effective event and peer-transfer processing calendar, selected
reconciliation procedures, and downstream financial uses that are not
independently verified for four subjects.

# 9. What This Note Does Not Claim

This note does not claim that:

- any reviewed instrument is invalid, unsafe, misleading, or legally defective;
- any named organization failed an operational, regulatory, fiduciary, or
  contractual duty;
- a blockchain record is inferior to an offchain record;
- every tokenized fund uses one of the five observed architectures;
- the named parties endorse this research;
- the controlled registry is a regulated benchmark, valuation source, audit,
  or legal opinion; or
- any investment, trading, listing, collateral, or settlement action should be
  taken.

# 10. Conclusion

The token is not the complete financial instrument. It is a representation
whose meaning depends on the authoritative record, transfer rules, operating
authority, valuation boundary, reconciliation process, correction hierarchy,
and downstream use that surround it.

Across five primary filings, five different record architectures sit behind
similar tokenized-share forms. Blockchain confirmation completes a transfer in
some architectures, submits an instruction in another, precedes authoritative
book reflection in another, and remains an unresolved boundary in one filing.
Those differences are not cosmetic. They determine what can be proven from a
token balance or transaction.

The Franklin and BENJI evidence chain shows why the distinction carries money.
When represented fund shares move at scale and support collateralized trading,
identity, ownership, custody, valuation, correction, and propagation become
financial controls. The public record proves the workflow but not every
interface or exposure.

The required infrastructure is a maintained financial instrument integrity
record: canonical, point-in-time, provenance-preserving, rights-aware, and
explicit about Unknowns. Without that record, programmable finance can automate
the movement of a representation faster than it can prove the financial object
being moved.

# References

Franklin Templeton. 2026a. "Franklin Templeton, Stellar Development Foundation
Mark Five Years of BENJI." April 30, 2026.
<https://www.franklintempleton.com/press-releases/news-room/2026/franklin-templeton-stellar-development-foundation-mark-five-years-of-benji-the-first-u.s.-registered-tokenized-money-market-fund>.

Franklin Templeton. 2026b. "Franklin Templeton and Binance Advance Strategic
Collaboration with Institutional Off-Exchange Collateral Program." February 11,
2026.
<https://www.franklintempleton.com/press-releases/news-room/2026/franklin-templeton-and-binance-advance-strategic-collaboration-with-institutional-off-exchange-collateral-program>.

Franklin Templeton Trust. 2025. *Franklin OnChain U.S. Government Money Fund*.
Form 485BPOS, accession 0001741773-25-000031. January 3, 2025.
<https://www.sec.gov/Archives/edgar/data/1786958/000174177325000031/c485bpos.htm>.

Franklin Templeton Trust. 2026. *Supplement to the Franklin OnChain U.S.
Government Money Fund Prospectus and Statement of Additional Information*.
Forms 497 and 497K, accessions 0001655589-26-000576 and
0001655589-26-000578. April 24, 2026.
<https://www.franklintempleton.com/forms-literature/download-preview/9001-P>.

HSBC Physical Gold Trust. 2026. *HSBC Hybrid Gold ETF*. Form S-1, accession
0001104659-26-009255. February 2, 2026.
<https://www.sec.gov/Archives/edgar/data/2065655/000110465926009255/tm2512337d6_s1.htm>.

JPMorgan Trust IV. 2026. *JPMorgan OnChain Liquidity-Token Money Market Fund*.
Form 485BPOS, accession 0001193125-26-217424. May 12, 2026.
<https://www.sec.gov/Archives/edgar/data/1659326/000119312526217424/d44657d485bpos.htm>.

Short-Term Investments Trust. 2026a. *Invesco Stablecoin Reserves Onchain
Fund*. Form 485APOS, accession 0002071844-26-000768. July 9, 2026.
<https://www.sec.gov/Archives/edgar/data/205007/000207184426000768/final485.htm>.

Short-Term Investments Trust. 2026b. *Request for Withdrawal of Registration
Statement Amendments*. Form AW, accession 0002071844-26-000774. July 9, 2026.
<https://www.sec.gov/Archives/edgar/data/205007/000207184426000774/invescostit-stablecoinonchai.htm>.

Superstate Trust. 2025. *Superstate USTB Money Market Fund*. Form N-1A/A,
accession 0001104659-25-042142. April 30, 2025.
<https://www.sec.gov/Archives/edgar/data/1982577/000110465925042142/tm2513524d1_n1a.htm>.

U.S. Securities and Exchange Commission. 2026. "Privacy Information: Website
Dissemination." Accessed July 15, 2026.
<https://www.sec.gov/about/privacy-information>.

# Data And Artifact Availability

The public evidence package includes a bounded five-record machine sample, a
claim-to-evidence matrix, a deterministic classification example, the record
contract, rights determination, correction policy, architecture figures,
Franklin downstream-use analysis, and a hash-bound release manifest. The
complete maintained registry, normalized source receipts, implementation,
calculation receipts, correction feed, and future private evidence remain
controlled.

Corrections supported by authoritative evidence may be submitted to
`rampaidarwin@gmail.com` with the subject `TFII 001 correction`. Accepted
corrections are recorded without silently overwriting the released version.

# Conflicts And Funding

The author conducted this work independently. No named subject funded,
classified, reviewed, or endorsed it. No settled revenue, licence, adoption,
endorsement, or commercial validation is claimed.
