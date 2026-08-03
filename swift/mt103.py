from swift.factory import MessageFactory
from swift.validator import validate_mt103


class MT103:

    def __init__(self, raw_message: str):
        self.raw_message = raw_message

    def process(self):

        message = MessageFactory().build(
            self.raw_message
        )

        validation = validate_mt103(
            message.fields
        )

        return {
            "message_type": "MT103",
            "blocks": message.blocks,
            "fields": message.fields,
            "validation": validation,
        }
