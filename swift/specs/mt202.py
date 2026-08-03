"""
SWIFT MT202 Specification
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class MT202Specification:

    message_type = "202"

    required_fields = (
        "20",
        "21",
        "32A",
        "58A",
    )

    optional_fields = (
        "52A",
        "53A",
        "54A",
        "56A",
        "57A",
        "72",
    )
