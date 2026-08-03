from swift.mt103 import MT103


def test_mt103_fin():

    message = """{1:F01BANKBEBBAXXX0000000000}
{2:I103BANKDEFFXXXXN}
{3:{108:ABC123}}
{4:
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
-}
{5:{CHK:123456789ABC}}"""

    result = MT103(message).process()

    assert result["message_type"] == "MT103"

    assert result["fields"]["20"] == "REF123456"

    assert result["fields"]["23B"] == "CRED"

    assert result["fields"]["32A"]["currency"] == "USD"

    assert result["fields"]["50K"]["name"] == "JOHN DOE"

    assert result["fields"]["59"]["name"] == "JANE DOE"

    assert result["fields"]["71A"] == "SHA"

    assert result["validation"]["valid"] is True
