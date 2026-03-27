import csv
import os 
import random 
import statistics
import re
from datetime import datetime 
from typing import List 
import requests
from openpxl import workbook

#banking system

class person:
    def__init__(self,name,age):
       self.name=name
       self.age=age

#customer input for the data collection
#these belong to this specific student object

class customer(person):
    def__init__(self,customer_id,name,age,email,phone,balance=0.0):
    super().__init__(name,age)
    self.customer_id=customer_id
    self.phone=phone
    self.balance=balance
    self.email=email


    def deposit(self,amount):
        if amount<=0:
            raise valueError("deposit amount must be greater than 0.")
        self.balnce+= amount

        #withdrw money from the customers account
        def withdraw(self,amount):
            if amount <=0:
                raise value Error("withdrawal amount must be greater than 0.")
            if amount > self.balance:
                raise valueError("Insuffient funds.")
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
            def__init__(self,transaction_id,customer_id,transaction_type,amount,date):
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

