"""
Field 21
Related Reference
"""

class Field21Parser:

    def parse(self, value: str):

        return {
            "related_reference": value.strip()
        }
