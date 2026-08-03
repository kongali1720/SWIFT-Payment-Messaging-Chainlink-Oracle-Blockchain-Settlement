from swift.factory import MessageFactory


def test_factory():

    raw = """{1:F01BANKBEBBAXXX0000000000}
{2:I103BANKDEFFXXXXN}
{4:
:20:ABC123
:23B:CRED
-}
"""

    message = MessageFactory().build(raw)

    assert message.blocks["basic_header"]["application_id"] == "F"

    assert message.blocks["application_header"]["message_type"] == "103"

    assert message.fields["20"] == "ABC123"
