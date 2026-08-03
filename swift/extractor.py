"""
SWIFT FIN Text Block Extractor

Parses block {4:}

Returns:

{
    "20": "...",
    "23B": "...",
    ...
}
"""

from __future__ import annotations

import re


FIELD_START = re.compile(r"^:([0-9]{2}[A-Z]?):(.*)$")


class SwiftFieldExtractor:

    def extract(self, text_block: str):

        fields = {}

        current_tag = None

        buffer = []

        for line in text_block.splitlines():

            if line.strip() == "-":
                break

            match = FIELD_START.match(line)

            if match:

                if current_tag:

                    fields[current_tag] = "\n".join(buffer).strip()

                current_tag = match.group(1)

                buffer = [match.group(2)]

            else:

                if current_tag:

                    buffer.append(line)

        if current_tag:

            fields[current_tag] = "\n".join(buffer).strip()

        return fields
