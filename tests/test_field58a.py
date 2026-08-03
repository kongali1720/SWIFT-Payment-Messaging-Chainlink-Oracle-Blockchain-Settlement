from swift.parsers.mt202.field58a import Field58AParser


def test_field58a():

    parser = Field58AParser()

    result = parser.parse("BANKUS33XXX")

    assert result["bic"] == "BANKUS33XXX"
