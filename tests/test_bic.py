from swift.common.bic import BICParser


def test_bic():

    parser = BICParser()

    result = parser.parse("BANKUS33XXX")

    assert result["country"] == "US"

    assert result["location"] == "33"

    assert result["branch"] == "XXX"
