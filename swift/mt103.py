"""
MT103 Processing Engine
"""

from swift.blocks import SwiftBlockParser
from swift.extractor import SwiftFieldExtractor
from swift.parsers import FIELD_PARSERS
from swift.validator import validate_mt103


class MT103:

    def __init__(self, raw_message: str):
        self.raw_message = raw_message

    def process(self):

        block_parser = SwiftBlockParser()

        blocks = block_parser.parse(self.raw_message)

        text_block = blocks.get("4", self.raw_message)

        extractor = SwiftFieldExtractor()

        fields = extractor.extract(text_block)

        parsed = {}

        for tag, value in fields.items():

            parser = FIELD_PARSERS.get(tag)

            if parser:
                parsed[tag] = parser.parse(value)
            else:
                parsed[tag] = value

        validation = validate_mt103(fields)

        return {
            "message_type": "MT103",
            "blocks": blocks,
            "fields": parsed,
            "validation": validation,
        }
