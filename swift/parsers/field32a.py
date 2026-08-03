from datetime import datetime


class Field32A:

    DESCRIPTION = "Value Date Currency Amount"

    def parse(self, value: str):

        date = datetime.strptime(value[:6], "%y%m%d").date()

        currency = value[6:9]

        amount = float(value[9:].replace(",", "."))

        return {
            "date": str(date),
            "currency": currency,
            "amount": amount
        }
