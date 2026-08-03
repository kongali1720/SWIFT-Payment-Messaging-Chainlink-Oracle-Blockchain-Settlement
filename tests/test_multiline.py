from swift.extractor import SwiftFieldExtractor


def test_multiline_customer():

    text = """
:50K:/123456789
JOHN DOE
JL MERDEKA NO 1
JAKARTA
:59:/999999999
JANE DOE
BANDUNG
:71A:SHA
-
"""

    extractor = SwiftFieldExtractor()

    fields = extractor.extract(text)

    assert fields["50K"].startswith("/123456789")

    assert "JL MERDEKA" in fields["50K"]

    assert fields["71A"] == "SHA"
