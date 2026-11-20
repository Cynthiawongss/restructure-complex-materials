#!/usr/bin/env python3
"""Check lexical preservation in the two committed fictional handover trials.

This checks source-field labels and verbatim source values, not the correctness
of classification, merge decisions, meaning, or model behavior in future runs.
Python 3 standard library only.
"""
from pathlib import Path
import re

root = Path(__file__).resolve().parent
for language, output in [("en", "english"), ("zh-CN", "chinese")]:
    packet = (root / "inputs" / f"handover.{language}.md").read_text()
    answer = (root / "runs" / f"{output}.md").read_text()
    source = None
    facts = []
    for line in packet.splitlines():
        heading = re.match(r"## ([A-F])\s*[—–-]", line)
        if heading:
            source = heading[1]
            continue
        if source and re.search(r"[:：]", line):
            field, value = re.split(r"[:：]", line, maxsplit=1)
            facts.append((source, field.strip(), value.strip()))
    assert len(facts) == 39, (language, "unexpected fixture field count", len(facts))
    missing_values = [(sid, field) for sid, field, value in facts if value not in answer]
    missing_fields = [(sid, field) for sid, field, value in facts if f"{sid}.{field}" not in answer]
    assert not missing_values, (language, "missing source values", missing_values)
    assert not missing_fields, (language, "missing source field labels", missing_fields)
    print(f"{language}: 39/39 source values and field labels present")
