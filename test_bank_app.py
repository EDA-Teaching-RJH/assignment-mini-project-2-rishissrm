import pytest
from bank_app import Bank

#Testing add_customer funtion
def test_add_customer():
    bank = Bank()
    customer = bank.add_customer("Rowan", 20, "Rowan@gmail.com", "07123456789", 1000)

    assert customer.name == "Rowan"
    assert customer.age == 20
    assert customer.balance == 1000
    assert len(bank.customers) == 1

#Testing deposit funtion
def test_deposit():
    bank = Bank()
    customer = bank.add_customer("Sam", 21, "sam@gmail.com", "07123456789", 500)

    bank.deposit_to_customer(customer.customer_id, 200)

    assert customer.balance == 700

#Testing withdrawal function
def test_withdraw():
    bank = Bank()
    customer = bank.add_customer("Riya", 22, "riya@gmail.com", "07123456789", 500)

    bank.withdraw_from_customer(customer.customer_id, 100)

    assert customer.balance == 400

#Insuffient funds message
def test_withdraw_insufficient_funds():
    bank = Bank()
    customer = bank.add_customer("Tom", 19, "tom@gmail.com", "07123456789", 100)

    with pytest.raises(ValueError, match="Insufficient funds."):
        bank.withdraw_from_customer(customer.customer_id, 500)
