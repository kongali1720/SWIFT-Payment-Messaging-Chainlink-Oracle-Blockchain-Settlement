from swift.blocks import SwiftBlockParser
from swift.extractor import SwiftFieldExtractor
from swift.header import (
    BasicHeaderParser,
    ApplicationHeaderParser,
)
from swift.parsers import FIELD_PARSERS
from swift.domain.message import SwiftMessage


class MessageFactory:

    def build(self, raw_message: str):

        block_parser = SwiftBlockParser()

        blocks = block_parser.parse(raw_message)

        basic = {}

        application = {}

        if "1" in blocks:
            basic = BasicHeaderParser().parse(blocks["1"])

        if "2" in blocks:
            application = ApplicationHeaderParser().parse(blocks["2"])

        text = blocks.get("4", raw_message)

        extractor = SwiftFieldExtractor()

        fields = extractor.extract(text)

        parsed = {}

        for tag, value in fields.items():

            parser = FIELD_PARSERS.get(tag)

            parsed[tag] = parser.parse(value) if parser else value

        message = SwiftMessage()

        message.blocks = blocks

        message.fields = parsed

        message.blocks["basic_header"] = basic

        message.blocks["application_header"] = application

        return message
