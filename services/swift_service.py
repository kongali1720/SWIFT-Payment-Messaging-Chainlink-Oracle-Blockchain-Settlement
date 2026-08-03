from swift.mt103 import MT103


def parse_mt103(message: str):
    engine = MT103(message)
    return engine.process()
