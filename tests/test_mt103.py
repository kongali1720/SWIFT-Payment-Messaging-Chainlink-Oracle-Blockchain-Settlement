from swift.mt103 import MT103


def test_mt103_basic():

    message = """
:20:ABC123
:23B:CRED
:32A:260803USD1000,
:50K:JOHN DOE
:59:JANE DOE
"""

    parser = MT103(message)

    result = parser.process()

    assert result["message_type"] == "MT103"

    assert result["validation"]["valid"] is True

    assert result["payload"]["20"] == "ABC123"
