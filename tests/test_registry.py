from swift.engines import EngineRegistry


def test_registry():

    registry = EngineRegistry()

    engine = registry.get_engine("103")

    assert engine.__name__ == "MT103"
