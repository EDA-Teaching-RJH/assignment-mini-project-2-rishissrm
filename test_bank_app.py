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

#Test transfer
def test_transfer():
    bank = Bank()
    c1 = bank.add_customer("Alice", 20, "alice@gmail.com", "07123456789", 1000)
    c2 = bank.add_customer("Bob", 21, "bob@gmail.com", "07987654321", 500)

    bank.transfer(c1.customer_id, c2.customer_id, 300)

    assert c1.balance == 700
    assert c2.balance == 800

#Transactions statistics
def test_transaction_statistics():
    bank = Bank()
    customer = bank.add_customer("Maya", 20, "maya@gmail.com", "07123456789", 1000)

    bank.deposit_to_customer(customer.customer_id, 100)
    bank.deposit_to_customer(customer.customer_id, 200)
    bank.withdraw_from_customer(customer.customer_id, 50)

    stats = bank.transaction_statistics()

    assert stats["count"] == 3
    assert stats["total"] == 350
    assert stats["max"] == 200
    assert stats["min"] == 50