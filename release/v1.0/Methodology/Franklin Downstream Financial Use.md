# Franklin / BENJI Downstream Financial Use 001

**Reference family:** Tokenized Financial Instrument Integrity 001  
**Subject:** Franklin OnChain U.S. Government Money Fund / Benji platform family  
**Artifact status:** CONTROLLED DRAFT  
**Evidence boundary:** Public primary sources only  
**As of:** 2026-07-15  
**Public release permitted:** No

## 1. Purpose

This note tests whether the record architecture of a tokenized financial instrument can be connected to an observed downstream financial use without converting undisclosed exposure into fact.

The bounded result is affirmative at the platform level. Franklin Templeton reports more than USD 211 million in cumulative BENJI peer-to-peer transfer volume through 31 March 2026. Franklin Templeton and Binance also report a live institutional off-exchange collateral program in which eligible clients can use Benji-issued tokenized money-market fund shares as collateral while the assets remain in Ceffu-supported custody and their value is mirrored in the Binance trading environment.

The public record does not establish the exact participating fund or share class, pledged balances, clients, haircuts, valuation hierarchy, correction interface, or realized exposure. Those fields remain Unknown.

## 2. Supported Chain

The evidence supports the following bounded chain:

1. The Franklin OnChain U.S. Government Money Fund uses a transfer-agent-maintained blockchain-integrated official ownership record.
2. Its filing states that a peer-to-peer transfer completes upon confirmation on the relevant approved blockchain after transfer-agent processing.
3. Franklin Templeton reports cumulative BENJI peer-to-peer transfer volume above USD 211 million through 31 March 2026.
4. Franklin Templeton and Binance report a live institutional off-exchange collateral program for Benji-issued tokenized money-market fund shares.
5. In that program, eligible assets remain in Ceffu-supported off-exchange custody and their value is mirrored in the Binance trading environment.
6. The public sources do not disclose the complete control interface connecting authoritative ownership, effective transfer, custody state, mirrored collateral value, correction propagation, and default handling.

This is not a claim that the Franklin OnChain U.S. Government Money Fund itself was pledged, or that any control failed. It is evidence that the platform family has moved beyond representational novelty into active transfer and collateral workflows.

## 3. Record Architecture

| Control object | Bounded finding | Proof state | Primary evidence |
|---|---|---|---|
| Financial instrument | Franklin OnChain U.S. Government Money Fund share represented through the Benji blockchain-integrated system | BOUNDED INTERPRETATION | EA-FUND-005 |
| Authoritative ownership record | Transfer agent maintains the official record through a blockchain-integrated system | OBSERVATION | EA-FUND-005, Locator 1 |
| Transfer-effective boundary | Peer-to-peer transfer completes upon relevant blockchain confirmation after transfer-agent processing | OBSERVATION | EA-FUND-005, Locator 3 |
| Correction authority | Transfer agent controls accuracy, error correction, unauthorized-transaction treatment, and transferability limits | OBSERVATION | EA-FUND-005, Locator 2 |

The transfer-effective event is instrument-specific. It must not be generalized to other tokenized funds, even when their tokens look operationally similar.

## 4. Observed Transfer Activity

Franklin Templeton reports cumulative BENJI peer-to-peer transfer volume above USD 211 million through 31 March 2026. This establishes reported use of the transfer mechanism at scale. FET has not independently reconciled the amount against complete transaction-level records, transfer-agent books, or a public coverage manifest.

The number is therefore retained as an issuer-reported observation, not an independently verified benchmark value.

## 5. Live Collateral Workflow

Franklin Templeton and Binance describe a live institutional off-exchange collateral program. The disclosed architecture has three observable components:

- eligible clients use Benji-issued tokenized money-market fund shares as collateral;
- the assets remain in regulated off-exchange custody supported by Ceffu; and
- collateral value is mirrored in the Binance trading environment.

The announcement does not identify the exact fund and share classes admitted, account-level positions, aggregate pledged balance, collateral haircut, update frequency, stale-value rules, default handling, or correction and release mechanics.

## 6. Financial Consequence

**A tokenized fund record is no longer merely a disclosure artifact when the represented shares move at scale and support collateralized trading. Authoritative ownership, transfer effectiveness, custody reconciliation, valuation, and correction propagation become financial controls.**

The consequence does not depend on proving a failure. It follows from the disclosed workflow:

- a custody system must identify the same eligible asset and ownership state recognized by the authoritative record;
- a collateral system must know when a transfer, freeze, correction, or release becomes effective;
- a mirrored collateral value requires a defined valuation source, update boundary, and stale-state policy; and
- a correction to the authoritative record requires a propagation path to any downstream collateral representation.

The public sources establish that these components exist. They do not disclose the complete interfaces among them.

## 7. Missing Control Interfaces

| Unknown | Why it matters | Status |
|---|---|---|
| Exact fund and share-class eligibility | Prevents attribution of platform-level use to a specific fund record | UNKNOWN |
| Pledged balances and client identities | Prevents measurement of exact exposure | UNKNOWN |
| Collateral haircut and valuation hierarchy | Prevents reconstruction of usable collateral value | UNKNOWN |
| Custody-to-transfer-agent reconciliation | Prevents verification that custody and official ownership remain synchronized | UNKNOWN |
| Freeze, correction, clawback, and release propagation | Prevents reconstruction of state-change handling across systems | UNKNOWN |
| Default and liquidation realization path | Prevents reconstruction of enforcement and loss allocation | UNKNOWN |
| Independent transfer-volume reconciliation | Prevents independent confirmation of the issuer-reported cumulative amount | UNKNOWN |

Unknown does not mean absent, defective, or false. It means the reviewed public evidence does not establish the field.

## 8. Claim Boundaries

This note does not claim:

- that the Franklin OnChain U.S. Government Money Fund is an eligible or pledged asset in the collateral program;
- that USD 211 million was independently reconciled by FET;
- that Franklin Templeton, Binance, Ceffu, or any other named party endorsed FET;
- that an operational, legal, accounting, or risk-control failure occurred;
- that the described architecture is unique to Franklin Templeton; or
- that any investment or trading action should be taken.

## 9. Result

The downstream financial-use state is **ESTABLISHED_BOUNDED_PLATFORM_LEVEL**.

The Franklin / BENJI evidence chain establishes an active transfer environment and a live institutional collateral workflow. It therefore proves that record integrity, transfer effectiveness, custody reconciliation, valuation, and correction propagation can carry direct financial consequence. Exact fund collateral exposure and the complete control interface remain Unknown.

The complete machine-readable downstream-use chain, schema, and implementation remain controlled.

## 10. Primary Sources

1. U.S. Securities and Exchange Commission, Franklin Templeton Trust filing, Form 485BPOS, accession 0001741773-25-000031: <https://www.sec.gov/Archives/edgar/data/1786958/000174177325000031/c485bpos.htm>
2. Franklin Templeton, "Franklin Templeton, Stellar Development Foundation Mark Five Years of Benji": <https://www.franklintempleton.com/press-releases/news-room/2026/franklin-templeton-stellar-development-foundation-mark-five-years-of-benji-the-first-u.s.-registered-tokenized-money-market-fund>
3. Franklin Templeton, "Franklin Templeton and Binance Advance Strategic Collaboration with Institutional Off-Exchange Collateral Program": <https://www.franklintempleton.com/press-releases/news-room/2026/franklin-templeton-and-binance-advance-strategic-collaboration-with-institutional-off-exchange-collateral-program>
