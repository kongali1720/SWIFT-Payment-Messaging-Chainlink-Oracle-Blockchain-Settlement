"""
Field 58A
Beneficiary Institution
"""

class Field58AParser:

    def parse(self, value: str):

        lines = value.strip().splitlines()

        bic = lines[0] if lines else ""

        return {
            "bic": bic
        }
