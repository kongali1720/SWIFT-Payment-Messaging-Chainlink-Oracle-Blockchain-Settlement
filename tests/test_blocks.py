from swift.blocks import SwiftBlockParser


def test_block_parser():

    message = """{1:F01BANKBEBBAXXX0000000000}
{2:I103BANKDEFFXXXXN}
{3:{108:ABC123}}
{4:
:20:REF123
:23B:CRED
-}
{5:{CHK:ABCDEF}}"""

    parser = SwiftBlockParser()

    blocks = parser.parse(message)

    assert blocks["1"].startswith("F01")
    assert blocks["2"].startswith("I103")
    assert "108" in blocks["3"]
    assert ":20:" in blocks["4"]
    assert "CHK" in blocks["5"]
