"""
SWIFT FIN Block Parser

Parses:
{1:}
{2:}
{3:}
{4:}
{5:}
"""

from __future__ import annotations

import re


class SwiftBlockParser:
    """
    Parse SWIFT FIN blocks.

    Example
    -------
    {1:F01BANK...}
    {2:I103BANK...}
    {3:{108:ABC123}}
    {4:
    :20:ABC
    -}
    {5:{CHK:ABC}}
    """

    def parse(self, message: str) -> dict[str, str]:
        blocks: dict[str, str] = {}

        length = len(message)
        i = 0

        while i < length:
            if message[i] != "{":
                i += 1
                continue

            j = message.find(":", i)
            if j == -1:
                break

            block_id = message[i + 1 : j]

            depth = 1
            k = j + 1

            while k < length and depth > 0:
                if message[k] == "{":
                    depth += 1
                elif message[k] == "}":
                    depth -= 1
                k += 1

            blocks[block_id] = message[j + 1 : k - 1].strip()

            i = k

        return blocks
