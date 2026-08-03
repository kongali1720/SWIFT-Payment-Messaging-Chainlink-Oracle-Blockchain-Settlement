"""
SWIFT Text Block Field Extractor

Extracts fields from Block 4.

Example:

:20:REF123
:23B:CRED
:32A:260803USD1000,
"""

from __future__ import annotations

import re


FIELD_PATTERN = re.compile(
    r":([0-9]{2}[A-Z]?):(.*?)(?=\n:[0-9]{2}[A-Z]?:|\n-$|\Z)",
    re.DOTALL,
)


class SwiftFieldExtractor:

    def extract(self, text_block: str) -> dict[str, str]:
        fields: dict[str, str] = {}

        for tag, value in FIELD_PATTERN.findall(text_block):
            fields[tag] = value.strip()

        return fields
