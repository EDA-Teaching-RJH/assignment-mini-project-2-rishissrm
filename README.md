# Banking system

class account:
"""represents a single bank account"""
 def __init__(self,account_number:str,owner:str,balanace:float =0.0):
       self.account_number = account_number
       self.owner = owner
       self.balance=float(balance)
       self.transactions:List[dict]=[]

       