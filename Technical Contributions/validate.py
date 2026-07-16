#!/usr/bin/env python3
"""Validate the public TFII technical contributions."""

from __future__ import annotations

import json
import hashlib
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parent


def load(name: str) -> dict[str, Any]:
    with (ROOT / name).open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"{name}: top-level JSON value must be an object")
    return value


def schema_errors(schema: dict[str, Any], value: dict[str, Any]) -> list[str]:
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [error.message for error in validator.iter_errors(value)]


def validate_conformance() -> str:
    schema = load("tfii-finos-cdm-conformance-test-001.schema.json")
    result = load("tfii-finos-cdm-conformance-test-001.json")
    sample = load("fixtures/TFII-Public-Sample-v1.0.json")
    calculation = load("fixtures/Transfer-Boundary-Classification-v1.0.json")
    errors = schema_errors(schema, result)

    requirements = result["requirements"]
    ids = [row["requirement_id"] for row in requirements]
    if len(ids) != len(set(ids)):
        errors.append("conformance requirement IDs are not unique")
    counts = Counter(row["status"] for row in requirements)
    expected_counts = {key: counts.get(key, 0) for key in ("PASS", "PARTIAL", "FAIL", "UNKNOWN")}
    if expected_counts != result["summary"]["result_counts"]:
        errors.append("conformance result counts do not recompute")
    if len(requirements) != result["summary"]["requirement_count"]:
        errors.append("conformance requirement count does not recompute")

    sample_rows = {row["record_id"]: row for row in sample["records"]}
    calc_rows = {row["record_id"]: row for row in calculation["rows"]}
    vectors = {row["record_id"]: row for row in result["test_vectors"]}
    if set(vectors) != set(sample_rows) or set(vectors) != set(calc_rows):
        errors.append("conformance vector IDs do not match the fixtures")
    for record_id, vector in vectors.items():
        if vector["architecture_class"] != sample_rows[record_id]["architecture_class"]:
            errors.append(f"{record_id}: architecture class mismatch")
        if vector["transfer_boundary_class"] != calc_rows[record_id]["output_transfer_boundary_class"]:
            errors.append(f"{record_id}: transfer boundary mismatch")
    if result["summary"]["overall_result"] != "PARTIAL":
        errors.append("conformance overall result must be PARTIAL")
    if errors:
        raise ValueError("; ".join(errors))
    return result["summary"]["overall_result"]


def validate_control() -> str:
    schema = load("tfii-tokenized-fund-collateral-admission-control-001.schema.json")
    control = load("tfii-tokenized-fund-collateral-admission-control-001.json")
    sample = load("fixtures/TFII-Public-Sample-v1.0.json")
    errors = schema_errors(schema, control)

    ids = [row["requirement_id"] for row in control["requirement_catalog"]]
    if len(ids) != len(set(ids)):
        errors.append("control requirement IDs are not unique")
    rows = control["instrument_results"]
    if {row["record_id"] for row in rows} != {row["record_id"] for row in sample["records"]}:
        errors.append("control record IDs do not match the public fixture")
    for row in rows:
        missing = [
            item
            for item in row["architecture_results"] + row["program_results"]
            if item["status"] in {"FAIL", "UNKNOWN"}
        ]
        if missing and (
            row["precheck_state"] != "HOLD_MISSING_EVIDENCE"
            or row["cdm_eligibility_query_state"] != "NOT_RUN"
            or row["determination"] != "UNKNOWN"
        ):
            errors.append(f"{row['record_id']}: mandatory Unknown did not fail closed")
    aggregate = control["aggregate"]
    if aggregate["instrument_count"] != len(rows):
        errors.append("control instrument count does not recompute")
    if aggregate["cdm_queries_run"] != 0 or aggregate["admission_decisions_made"] != 0:
        errors.append("control emitted a query or admission decision")
    if control["external_determination"] != "UNKNOWN":
        errors.append("control determination must remain UNKNOWN")
    if any(control["claim_boundary"].values()):
        errors.append("control claim boundary failed")
    if errors:
        raise ValueError("; ".join(errors))
    return control["external_determination"]


def validate_profile() -> str:
    schema = load("tfii-cdm-record-integrity-profile-001.schema.json")
    profile = load("tfii-cdm-record-integrity-profile-001.json")
    sample_path = ROOT / "fixtures" / "TFII-Public-Sample-v1.0.json"
    errors = schema_errors(schema, profile)

    source_hash = hashlib.sha256(sample_path.read_bytes()).hexdigest()
    if profile["source_sample_sha256"] != source_hash:
        errors.append("profile source-sample hash mismatch")
    requirements = profile["requirements"]
    ids = [row["requirement_id"] for row in requirements]
    if len(ids) != 17 or len(ids) != len(set(ids)):
        errors.append("profile must contain 17 unique requirements")
    if any(row["combined_status"] != "PASS" for row in requirements):
        errors.append("combined profile requirements must all PASS")
    records = profile["records"]
    for row in records:
        if not row["coverage"]["unknowns"]:
            errors.append(f"{row['record_id']}: Unknowns were not preserved")
        gate = row["collateral_gate"]
        if gate["cdm_eligibility_query_permitted"] or gate["determination"] != "UNKNOWN":
            errors.append(f"{row['record_id']}: profile did not fail closed")
    if profile["summary"]["combined_profile_result"] != "PASS":
        errors.append("combined profile result must be PASS")
    if errors:
        raise ValueError("; ".join(errors))
    return profile["summary"]["combined_profile_result"]


def criteria_match(criteria: dict[str, Any], query: dict[str, Any]) -> bool:
    if "all" in criteria:
        return all(criteria_match(item, query) for item in criteria["all"])
    if "any" in criteria:
        return any(criteria_match(item, query) for item in criteria["any"])
    if "not" in criteria:
        return not criteria_match(criteria["not"], query)
    actual = query[criteria["field"]]
    expected = criteria["value"]
    operation = criteria["operation"]
    if operation == "EQUALS":
        return actual == expected
    if operation == "LTE":
        return actual <= expected
    if operation == "GTE":
        return actual >= expected
    raise ValueError(f"unsupported vector operation: {operation}")


def validate_execution_vectors() -> str:
    schema = load("tfii-collateral-admission-control-vectors-001.schema.json")
    artifact = load("tfii-collateral-admission-control-vectors-001.json")
    errors = schema_errors(schema, artifact)
    outputs = []
    for row in artifact["vectors"]:
        states = row["requirement_states"]
        if "UNKNOWN" in states.values():
            expected = {
                "precheck_state": "HOLD_MISSING_EVIDENCE",
                "cdm_query_state": "NOT_RUN",
                "is_eligible": None,
                "determination": "UNKNOWN",
            }
        else:
            matched = [
                index
                for index, criterion in enumerate(row["specification"]["criteria"])
                if criteria_match(criterion, row["query"])
            ]
            eligible = bool(matched) and all(value == "PASS" for value in states.values())
            expected = {
                "precheck_state": "COMPLETE",
                "cdm_query_state": "RUN_REFERENCE_PARITY_REPLAY",
                "is_eligible": eligible,
                "matching_criteria_indexes": matched,
                "determination": "PASS" if eligible else "FAIL",
            }
        if row["output"] != expected:
            errors.append(f"{row['vector_id']}: deterministic replay mismatch")
        outputs.append(row["output"]["determination"])
    if outputs != ["PASS", "FAIL", "UNKNOWN"]:
        errors.append("execution branches must be PASS, FAIL and UNKNOWN")
    if errors:
        raise ValueError("; ".join(errors))
    return "PASS"


def main() -> int:
    try:
        conformance = validate_conformance()
        profile = validate_profile()
        execution = validate_execution_vectors()
        control = validate_control()
    except Exception as exc:
        print(f"FAIL {exc}", file=sys.stderr)
        return 1
    print(f"PASS conformance test: {conformance}")
    print(f"PASS CDM plus TFII record-integrity profile: {profile}")
    print(f"PASS collateral admission execution branches: {execution}")
    print(f"PASS collateral admission control: {control}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
