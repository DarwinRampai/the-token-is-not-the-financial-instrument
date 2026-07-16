# FET TFII Correction and Version Policy 001

**Reference family:** Tokenized Financial Instrument Integrity Reference Family 001  
**Policy version:** 1.0  
**Status:** Controlled operating policy  
**Effective date:** 15 July 2026  
**Operator:** Darwin Rampai, independent researcher

## 1. Purpose

This policy governs corrections, restatements, version changes, and downstream
notices for the TFII registry and its derived artifacts. Its purpose is to make
the historical record auditable. No factual field, evidence classification,
source receipt, methodology rule, or published conclusion may be replaced
silently.

The policy applies to the controlled registry, bounded samples,
claim-to-evidence matrices, diagrams, calculation artifacts, public releases,
and licensed deliveries derived from TFII records.

## 2. Governing Rule

**A corrected source record is not the same event as propagation of that
correction to every downstream user.**

FET therefore records two separate states:

1. the canonical record was corrected; and
2. a named downstream artifact or recipient received the correction.

The first state must never be used to infer the second.

## 3. Correction Classes

| Class | Definition | Minimum action |
|---|---|---|
| `CLERICAL` | Typographic or formatting defect that does not change meaning | Correct, increment patch version, preserve receipt |
| `SOURCE_METADATA` | Source identity, date, URL, accession, locator, or hash defect | Replace binding, revalidate every dependent field |
| `FACTUAL_FIELD` | Represented value does not match the admitted source | Correct field, evidence map, sample, and dependent claims |
| `EVIDENCE_STATE` | Observation, interpretation, inference, confidence, or Unknown status changes | Record former and new states with reason |
| `CLASSIFICATION` | Architecture or record-role classification changes | Re-run comparative conclusions and visual |
| `METHODOLOGY` | Rule, taxonomy, inclusion, or calculation logic changes | Increment major or minor version and replay history |
| `RIGHTS_STATE` | Permitted use, delivery, citation, or redistribution basis changes | Re-evaluate every release and delivery boundary |
| `WITHDRAWAL` | Evidence can no longer support a represented claim | Preserve withdrawn record and prohibit further reliance |

## 4. Correction Triggers

A correction review begins when any of the following occurs:

- an official source is amended, replaced, corrected, or withdrawn;
- a source receipt hash, locator, or extraction cannot be reproduced;
- validation detects a schema, evidence, lineage, or rights mismatch;
- the named subject supplies a documented factual correction;
- an independent reviewer supplies material contrary evidence;
- a field previously marked `UNKNOWN` becomes observable;
- a downstream artifact differs from the canonical registry; or
- FET identifies a material ambiguity in its own language.

A disagreement without supporting evidence is recorded but does not by itself
change the canonical record.

## 5. Correction Workflow

Each correction follows this state sequence:

1. `IDENTIFIED`: preserve the incoming notice or validator failure.
2. `TRIAGED`: classify materiality, affected records, rights, and urgency.
3. `EVIDENCE_FROZEN`: retain the pre-correction artifact and hashes.
4. `DECIDED`: accept, reject, defer, or preserve as unresolved conflict.
5. `IMPLEMENTED`: update the canonical registry through a new version.
6. `REVALIDATED`: run schema, source, receipt, claim, rights, and release checks.
7. `PROPAGATED`: update each affected derivative and issue required notices.
8. `CLOSED`: preserve the full before-and-after receipt and unresolved effects.

No step authorizes deletion of the former record.

## 6. Required Correction Receipt

Every accepted or rejected correction must record:

- correction ID;
- date identified and date decided;
- correction class and materiality;
- reporter or detection method;
- affected record, field, claim, and artifact IDs;
- former value, evidence status, confidence, locator, and hash;
- proposed and accepted value;
- admitted source IDs and source receipts;
- decision and reasons;
- effective observation boundary;
- registry version before and after;
- validation results;
- downstream artifacts rebuilt;
- recipients notified and delivery evidence;
- unresolved propagation state; and
- operator identity.

Private reporter details remain controlled unless disclosure is authorized.

## 7. Version Rules

TFII uses semantic versions for the maintained reference family.

- **Patch:** clerical, source-locator, or non-substantive presentation change.
- **Minor:** new record, newly observed field, new source receipt, or bounded
  classification change that preserves the methodology.
- **Major:** methodology, taxonomy, governing interpretation, or claim boundary
  changes in a way that can alter prior conclusions.

Every derivative must bind to the exact canonical registry hash. A derivative
with an older hash remains historical and must not be presented as current.

## 8. Historical Replay

When a correction can affect historical conclusions, FET must:

1. preserve the original source and receipt;
2. determine the source's effective date and observation boundary;
3. replay each affected historical record under the corrected rule;
4. distinguish a corrected historical fact from a later methodology change;
5. regenerate claim matrices, charts, and release manifests; and
6. report which historical outputs changed and which did not.

Current information must not be backfilled into an earlier point-in-time record
unless it is explicitly labeled as a later correction or restatement.

## 9. Propagation Control

Propagation is tracked per artifact and recipient. Possible states are:

- `NOT_REQUIRED`;
- `PENDING`;
- `DELIVERED`;
- `ACKNOWLEDGED`;
- `REJECTED`;
- `FAILED_DELIVERY`;
- `UNKNOWN`.

Silence is not acknowledgement. Public posting is not proof that a private
licensee, model, report, smart contract, or decision process adopted the
correction.

## 10. Material Correction Notices

A material correction notice must state, in plain language:

- what changed;
- why it changed;
- what evidence supports the change;
- which outputs and dates are affected;
- whether any conclusion was withdrawn or narrowed;
- what remains Unknown; and
- where the prior and corrected hashes can be verified.

The notice must not conceal a substantive correction as a routine update.

## 11. Rights And Disclosure Boundary

Correction receipts may identify official sources and publish FET-created
factual structure within the permitted-use boundary. They must not redistribute
private documents, licensed source content, personal data, legal advice, or
confidential counterparty evidence without a valid right.

When the evidence needed to resolve a correction is inaccessible, the record
remains `UNKNOWN`, `DEFERRED`, or `CONFLICTED`. FET does not infer a favorable
answer to close the issue.

## 12. Release Controls

No corrected artifact may be released or delivered until:

- all source and receipt hashes validate;
- all evidence references resolve;
- all dependent claims have been recomputed;
- the prior version remains preserved;
- the rights state permits the intended use;
- the release manifest binds the corrected artifacts; and
- any required factual-review period is complete or explicitly recorded as
  `NO_RESPONSE_BY_DEADLINE`.

`NO_RESPONSE_BY_DEADLINE` is not agreement, endorsement, or confirmation.

## 13. Current State

As of 15 July 2026, the initial TFII registry is a controlled draft. No formal
correction receipt has been opened. Public release and commercial delivery
remain prohibited by the registry. This policy is active before release so the
first publication cannot create an untracked correction debt.
