from swift.header.application import ApplicationHeaderParser


def test_application_header():

    parser = ApplicationHeaderParser()

    result = parser.parse(
        "I103BANKDEFFXXXXN"
    )

    assert result["direction"] == "I"

    assert result["message_type"] == "103"

    assert result["receiver"] == "BANKDEFFXXXX"

    assert result["priority"] == "N"
