from swift.detector import MessageDetector


def test_detector_mt103():

    message = """{1:F01BANKBEBBAXXX0000000000}
{2:I103BANKDEFFXXXXN}
{4:
:20:ABC123
-}
"""

    detector = MessageDetector()

    assert detector.detect(message) == "103"
