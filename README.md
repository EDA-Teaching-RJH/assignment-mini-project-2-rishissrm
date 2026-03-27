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


    def deposit(self,amount):
        if amount<=0:
            raise valueError("deposit amount must be greater than 0.")
        self.balnce+= amount