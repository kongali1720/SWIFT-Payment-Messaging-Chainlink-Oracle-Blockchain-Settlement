from swift.parsers.mt202.field21 import Field21Parser


def test_field21():

    parser = Field21Parser()

    result = parser.parse("RELREF001")

    assert result["related_reference"] == "RELREF001"
