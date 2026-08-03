from swift.mt103 import MT103


class EngineRegistry:

    def __init__(self):

        self._engines = {
            "103": MT103,
        }

    def get_engine(self, message_type):

        if message_type not in self._engines:
            raise ValueError(
                f"Unsupported message type: {message_type}"
            )

        return self._engines[message_type]
