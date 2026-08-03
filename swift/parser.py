import re


class SwiftParser:

    def __init__(self, message: str):
        self.message = message

    def parse(self):
        tags = {}

        pattern = r":([0-9A-Z]{2,3}[A-Z]?):(.*?)(?=\n:[0-9A-Z]{2,3}[A-Z]?:|\Z)"

        matches = re.findall(pattern, self.message, re.S)

        for tag, value in matches:
            tags[tag] = value.strip()

        return tags
