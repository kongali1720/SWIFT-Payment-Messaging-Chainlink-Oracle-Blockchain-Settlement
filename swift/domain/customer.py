from dataclasses import dataclass


@dataclass
class Customer:
    account: str
    name: str
    address: str
