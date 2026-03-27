import csv
import os 
import random 
import statistics
import re
from datetime import datetime 
from typing import List 
import requests
from openpxl import workbook


class person:
    def__init__(self,name,age):
       self.name=name
       self.age=age