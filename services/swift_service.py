from swift.mt103 import MT103


def parse_mt103(message: str):
    parser = MT103(message)
    return parser.process()
