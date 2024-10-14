from account import BankAccount
from real import RealEstate
from security import Security
class Asset(BankAccount, RealEstate, Security):
    ...