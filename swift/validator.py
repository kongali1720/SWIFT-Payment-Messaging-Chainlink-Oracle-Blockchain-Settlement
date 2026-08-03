from swift.specs.registry import get_specification


def validate_mt103(fields):

    spec = get_specification("103")

    missing = []

    for field in spec.required_fields:

        if field not in fields:
            missing.append(field)

    return {
        "valid": len(missing) == 0,
        "missing": missing,
    }
