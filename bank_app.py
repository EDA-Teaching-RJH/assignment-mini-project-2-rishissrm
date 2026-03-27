import csv
import os 
import random 
import statistics
import re
from datetime import datetime 
from typing import List 
import requests
from openpyxl import workbook

#banking system

class person:
    def __init__(self,name,age):
       self.name=name
       self.age=age

#customer input for the data collection
#these belong to this specific student object

class customer(person):
    def __init__(self,customer_id,name,age,email,phone,balance=0.0):
        super().__init__(name,age)
        self.customer_id=customer_id
        self.phone=phone
        self.balance=balance
        self.email=email


    def deposit(self,amount):
        if amount<=0:
            raise ValueError("deposit amount must be greater than 0.")
        self.balnce+= amount

        #withdrw money from the customers account
        def withdraw(self,amount):
            if amount <=0:
                raise ValueError("withdrawal amount must be greater than 0.")
            if amount > self.balance:
                raise ValueError("Insuffient funds.")
            self.balance -=amount

    #coverting customer data into list to be saved in cvs
    def to_list(self):
        return[
             self.customer_id,
             self.name,
             self.age,
             self.email,
             self.phone,
             round(self.balance,2)
        ]


        #transaction class stores one transaction record.
        class transaction:
            def __init__(self,transaction_id,customer_id,transaction_type,amount,date):
               self.transaction_id=transaction_id
               self.customer_id=customer_id
               self.transaction_type=transaction_type
               self.amount=amount
               self.date=date
#Convert transaction data into a list for CSV or excel
        def to_list(self):
            return [
                self.transaction_id,
                self.customer_id,
                self.transaction_type,
                round(self.amount,2),
                self.date
            ]

#Bank class is the main part of the program
#It stores all the customers and their transations and performs all operations
class Bank:
    def __init__(self):
        self.customers: List[Customer] = []
        self.transations: List[Transactions] = []

    #Check whether the name contrains only letters and spaces.
    def is_valid_name(self,name):
        pattern = r"^[A-Za-z ]{2,30}$"
        return bool(re.match(pattern,name))
    
    #Check whether the email is in a valid format
    def is_valid_email(self,email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[A-Za-z]{2,}$"
        return bool(re.match(pattern,email))

    #Check whether the phone number has 10 or 11 digits.
    def is_valid_phone(self,phone):
        pattern = r"^[0-9]{10,11}$"
        return bool(re.match(pattern,phone))

    #Add a new customer after validating the input.
    def add_customer(self,name,age,email,phone,opening_balance=0.0):
        if not self.is_valid_name(name):
            raise ValueError("Invalid name, Use Letters and spaces only.")
        
        if not self.is_valid_email(email):
            raise ValueError("Invalid email format.")
        
        if not self.is_valid_phone(phone):
            raise ValueError("Invalid phone number. Use 10 or 11 digits.")

        customer_id = len(self.customer) +1
        customer = Customer(customer_id,name, age,email,phone,opening_balance)
        self.customers.append(customer)
        return Customer

    #Find a customer by their customer ID.
    def find_customer(self,customer_id):
        for customer in sef.customers:
            if customer.customer_id == customer_id:
                return customer
        raise ValueError("Customer not found.")

    #Save one transation into the transaction list.
    def record_transaction(self,customer_id,transaction_type,amount):
        transaction_id =len(self.transations) +1
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaction = transaction(transaction_id,customer_id,transaction_type,amount,date)
        self.transations.append(transaction)

