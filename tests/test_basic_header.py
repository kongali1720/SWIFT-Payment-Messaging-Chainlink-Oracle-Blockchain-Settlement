from swift.header.basic import BasicHeaderParser


def test_basic_header():

    parser = BasicHeaderParser()

    result = parser.parse(
        "F01BANKBEBBAXXX0000000000"
    )

    assert result["application_id"] == "F"

    assert result["service_id"] == "01"

    assert result["logical_terminal"] == "BANKBEBBAXXX"

    assert result["session_number"] == "0000"

    assert result["sequence_number"] == "000000"
