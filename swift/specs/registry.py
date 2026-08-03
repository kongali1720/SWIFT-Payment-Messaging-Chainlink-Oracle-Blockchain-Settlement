from .mt103 import MT103Specification


SPECIFICATIONS = {
    "103": MT103Specification(),
}


def get_specification(message_type: str):
    return SPECIFICATIONS[message_type]
