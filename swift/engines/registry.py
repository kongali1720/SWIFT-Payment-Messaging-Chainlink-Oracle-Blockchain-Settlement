from swift.mt103 import MT103
from swift.mt202 import MT202


class EngineRegistry:

    def __init__(self):
        self._engines = {
            "103": MT103,
            "202": MT202,
        }

    def get_engine(self, message_type: str):

        try:
            return self._engines[message_type]
        except KeyError:
            supported = ", ".join(sorted(self._engines.keys()))
            raise ValueError(
                f"Unsupported message type: {message_type}. "
                f"Supported: {supported}"
            )

    def supported_message_types(self):
        return tuple(sorted(self._engines.keys()))
