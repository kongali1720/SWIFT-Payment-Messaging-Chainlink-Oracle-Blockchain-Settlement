class Field59:

    DESCRIPTION = "Beneficiary Customer"

    def parse(self, value: str):

        lines = [line.strip() for line in value.splitlines() if line.strip()]

        account = ""

        if lines and lines[0].startswith("/"):
            account = lines.pop(0)[1:]

        return {
            "account": account,
            "name": lines[0] if len(lines) > 0 else "",
            "address": " ".join(lines[1:])
        }
