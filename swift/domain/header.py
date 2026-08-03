from dataclasses import dataclass


@dataclass
class BasicHeader:
    application_id: str
    service_id: str
    logical_terminal: str
    session_number: str
    sequence_number: str


@dataclass
class ApplicationHeader:
    direction: str
    message_type: str
    receiver: str
    priority: str
