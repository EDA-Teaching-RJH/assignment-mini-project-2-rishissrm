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
