from swift.detector import MessageDetector


def test_mt202():

    raw = """{1:F01BANKBEBBAXXX0000000000}
{2:I202BANKDEFFXXXXN}
{4:
:20:ABC123
:21:REFERENCE
-}
"""

    detector = MessageDetector()

    assert detector.detect(raw) == "202"
