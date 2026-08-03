from datetime import datetime


def utc_timestamp():
    return datetime.utcnow().isoformat() + "Z"


def clean_line(value: str) -> str:
    return value.strip()
