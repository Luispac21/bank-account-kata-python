from Transaction import Transaction
from Account import Account
import datetime
from math import nan
import os

myAccount = Account(0,[])

def getAmount():
    print("Amount: ")
    amount = input()
    return abs(int(amount))

def deposit(amountDeposit):
    myAccount.balance += amountDeposit
    transaction = Transaction ( datetime.date.today(),'+' + str(amountDeposit), myAccount.balance)
    myAccount.statement.append(transaction)
    return transaction
    

def withdraw(amountWithdraw):
    if(myAccount.balance < amountWithdraw):
        print("Don't have balance to cover the withdraw")
        input()
        subMenu()

    myAccount.balance -= amountWithdraw
    transaction = Transaction ( datetime.date.today(),'-' + str(amountWithdraw), myAccount.balance)
    myAccount.statement.append(transaction)
    return transaction
    

def printSmallStatement(transaction):
    print("Do you want print small statement? Y/N")
    ans = input()

    if(ans == "Y" or ans == "y"):
        cls()
        print("Date             Amount       Balance")
        print(transaction.dateStatement , "     ", transaction.amount , "         ", transaction.balanceInstance)
        input()

def printGlobalStatement():
    if(len(myAccount.statement) > 0):
        print("Date             Amount       Balance")
        for row in myAccount.statement:
            print(row.dateStatement , "     ", row.amount , "         ", row.balanceInstance)
        

    else:
        input("You have to make any transaction first!")
        menu()

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def subMenu():
    ans = input("1 - Eject card  2 - To do other operation")
    if(ans == "1"):
        input("Eject card")
        welcome()
    else:
        menu()

def menu():
    cls()
    print("What the operation?")
    print("1 - Deposit")
    print("2 - Withdraw")
    print("3 - Print Statement")
    print("4 - Exit")
    op = input()
    if(op != nan):
        if(op == "1"):
            amount = getAmount()
            transaction = deposit(amount)
            printSmallStatement(transaction)
            subMenu()

        if(op == "2"):
            amount = getAmount()
            transaction = withdraw(amount)
            printSmallStatement(transaction)
            subMenu()

        if(op == "3"):
            printGlobalStatement()
            
        if(op == "4"):
            exit()

def welcome():
    cls()
    print("Welcome, please insert card and put PIN")
    input("(Press enter to simulate the task)")
    menu()
    

welcome()


    