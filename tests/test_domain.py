from swift.domain.customer import Customer


def test_customer():

    customer = Customer(
        account="123456789",
        name="JOHN DOE",
        address="JAKARTA"
    )

    assert customer.name == "JOHN DOE"
