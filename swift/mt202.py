from swift.factory import MessageFactory


class MT202:

    def __init__(self, raw_message):

        self.raw_message = raw_message

    def process(self):

        message = MessageFactory().build(
            self.raw_message
        )

        return {
            "message_type": "MT202",
            "blocks": message.blocks,
            "fields": message.fields,
        }
