REQUIRED_FIELDS = [
    "20",
    "23B",
    "32A",
    "50K",
    "59"
]


def validate_mt103(data: dict):

    missing = []

    for field in REQUIRED_FIELDS:
        if field not in data:
            missing.append(field)

    return {
        "valid": len(missing) == 0,
        "missing": missing
    }
