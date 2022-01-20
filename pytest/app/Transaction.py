import datetime
import string

class Transaction:
    def __init__(self, dateStatement, amount, balanceInstance):
        self.dateStatement = dateStatement
        self.amount = amount
        self.balanceInstance = balanceInstance

    dateStatement : datetime
    amount: string
    balanceInstance : int
