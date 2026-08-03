from pathlib import Path

from swift.detector import MessageDetector


def test_mt202_fixture():

    raw = Path(
        "tests/fixtures/mt202/sample001.fin"
    ).read_text()

    detector = MessageDetector()

    assert detector.detect(raw) == "202"
