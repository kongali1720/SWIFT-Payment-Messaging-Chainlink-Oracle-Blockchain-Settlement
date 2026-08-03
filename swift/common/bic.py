"""
Generic BIC parser.
"""

class BICParser:

    def parse(self, value: str):

        value = value.strip()

        return {
            "bic": value,
            "country": value[4:6] if len(value) >= 6 else "",
            "location": value[6:8] if len(value) >= 8 else "",
            "branch": value[8:] if len(value) > 8 else "PRIMARY",
        }
