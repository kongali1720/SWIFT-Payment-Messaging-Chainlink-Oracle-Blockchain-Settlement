from dataclasses import dataclass, field


@dataclass
class SwiftMessage:
    message_type: str
    blocks: dict = field(default_factory=dict)
    fields: dict = field(default_factory=dict)
