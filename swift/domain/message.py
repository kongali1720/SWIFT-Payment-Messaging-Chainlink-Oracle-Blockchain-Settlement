from dataclasses import dataclass, field


@dataclass
class SwiftMessage:
    blocks: dict = field(default_factory=dict)
    fields: dict = field(default_factory=dict)
