from pathlib import Path

from swift.mt103 import MT103


def test_fixture():

    data = Path(
        "tests/fixtures/mt103/sample001.fin"
    ).read_text()

    result = MT103(data).process()

    assert result["message_type"] == "MT103"

    assert result["validation"]["valid"]
