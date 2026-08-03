from dataclasses import dataclass
from datetime import date


@dataclass
class Amount:
    value_date: date
    currency: str
    amount: float
