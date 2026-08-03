from swift.engines import EngineRegistry


def test_registry202():

    registry = EngineRegistry()

    engine = registry.get_engine("202")

    assert engine.__name__ == "MT202"
