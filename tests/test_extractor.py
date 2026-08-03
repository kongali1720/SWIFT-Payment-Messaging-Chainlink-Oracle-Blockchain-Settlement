from swift.extractor import SwiftFieldExtractor


def test_field_extractor():

    text = """
:20:REF123456
:23B:CRED
:32A:260803USD1000,
:50K:/123456789
JOHN DOE
JAKARTA
:59:/987654321
JANE DOE
BANDUNG
:71A:SHA
-
"""

    extractor = SwiftFieldExtractor()

    fields = extractor.extract(text)

    assert fields["20"] == "REF123456"
    assert fields["23B"] == "CRED"
    assert "USD1000" in fields["32A"]
    assert "JOHN DOE" in fields["50K"]
    assert "JANE DOE" in fields["59"]
    assert fields["71A"] == "SHA"
