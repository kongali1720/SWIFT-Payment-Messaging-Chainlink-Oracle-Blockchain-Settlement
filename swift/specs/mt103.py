"""
SWIFT MT103 Specification
"""

from dataclasses import dataclass, field


@dataclass(frozen=True)
class MT103Specification:

    message_type: str = "103"

    required_fields: tuple = (
        "20",
        "23B",
        "32A",
        "50K",
        "59",
        "71A",
    )

    optional_fields: tuple = (
        "13C",
        "26T",
        "33B",
        "36",
        "52A",
        "53A",
        "54A",
        "56A",
        "57A",
        "70",
        "72",
        "77B",
    )

    field_descriptions: dict = field(
        default_factory=lambda: {
            "20": "Transaction Reference Number",
            "23B": "Bank Operation Code",
            "32A": "Value Date Currency Amount",
            "50K": "Ordering Customer",
            "59": "Beneficiary Customer",
            "71A": "Details of Charges",
        }
    )
