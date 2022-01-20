from Transaction import Transaction

class Account:
    def __init__(self, balance, statement):
        self.balance = balance
        self.statement = statement

    balance: int
    statement: Transaction