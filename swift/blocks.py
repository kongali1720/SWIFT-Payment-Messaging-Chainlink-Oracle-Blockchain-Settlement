"""
SWIFT FIN Block Parser

Supported Blocks:
{1:} Basic Header
{2:} Application Header
{3:} User Header
{4:} Text Block
{5:} Trailer
"""

import re


class SwiftBlockParser:

    BLOCK_PATTERN = re.compile(r"\{(\d):(.*?)\}", re.DOTALL)

    def parse(self, message: str) -> dict:
        blocks = {}

        for block_id, content in self.BLOCK_PATTERN.findall(message):
            blocks[block_id] = content.strip()

        return blocks
