from swift.detector import MessageDetector
from swift.engines import EngineRegistry


def parse(message: str):

    detector = MessageDetector()

    message_type = detector.detect(message)

    registry = EngineRegistry()

    engine = registry.get_engine(message_type)

    return engine(message).process()
