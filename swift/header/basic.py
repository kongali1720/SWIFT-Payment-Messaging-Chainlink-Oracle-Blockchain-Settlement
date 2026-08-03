"""
SWIFT FIN Block 1 Parser

Example:

F01BANKBEBBAXXX0000000000
"""

class BasicHeaderParser:

    def parse(self, value: str):

        return {
            "application_id": value[0:1],
            "service_id": value[1:3],
            "logical_terminal": value[3:15],
            "session_number": value[15:19],
            "sequence_number": value[19:25],
        }
