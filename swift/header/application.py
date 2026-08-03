"""
SWIFT FIN Block 2 Parser

Example

I103BANKDEFFXXXXN
"""

class ApplicationHeaderParser:

    def parse(self, value: str):

        return {
            "direction": value[0],
            "message_type": value[1:4],
            "receiver": value[4:16],
            "priority": value[16:] if len(value) > 16 else "",
        }
