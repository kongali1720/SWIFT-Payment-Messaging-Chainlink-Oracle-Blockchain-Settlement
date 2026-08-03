from swift.parser import SwiftParser
from swift.validator import validate_mt103


class MT103:

    def __init__(self, raw_message: str):
        self.raw_message = raw_message

    def process(self):

        parser = SwiftParser(self.raw_message)

        payload = parser.parse()

        validation = validate_mt103(payload)

        return {
            "message_type": "MT103",
            "payload": payload,
            "validation": validation
        }
