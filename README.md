# Banking system

class account:
"""represents a single bank account"""
 def __init__(self,account_number:str,owner:str,balanace:float =0.0):
       self.account_number = account_number
       self.owner = owner
       self.balance=float(balance)
       self.transactions:List[dict]=[]
# validation:check if inputs are sensible before storing them
if not account_number:
     raise valueEeeoe("missing account number")
if not owner:
     raise valueError("missing owner name")
if balance <0:
     raise valueError("Initialbalance cannot be negative")
     
def deposit(self,amount:float):
     """deposit money into the account"""
     
