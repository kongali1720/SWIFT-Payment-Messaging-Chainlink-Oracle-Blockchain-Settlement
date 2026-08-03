from swift.parsers.field32a import Field32A


def test_field32a():

    parser = Field32A()

    result = parser.parse("260803USD1000,")

    assert result["currency"] == "USD"
    assert result["amount"] == 1000.0
