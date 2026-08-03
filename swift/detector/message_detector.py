"""
SWIFT FIN Message Detector
"""

from swift.blocks import SwiftBlockParser


class MessageDetector:

    def detect(self, raw_message: str) -> str:

        blocks = SwiftBlockParser().parse(raw_message)

        block2 = blocks.get("2", "")

        if len(block2) < 4:
            raise ValueError("Invalid Block 2")

        direction = block2[0]

        if direction not in ("I", "O"):
            raise ValueError("Unknown SWIFT direction")

        return block2[1:4]
