import os
from datetime import datetime

class Account:
    def __init__(self,account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than zero")
            return
        self.balance += amount
        self._add_transaction("Deposit", amount)
        print(f"Deposited {amount} Taka successfully. Current balance: {self.balance} Taka")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be grater than zero.")
            return
        if amount > self.balance:
            print("\nInsufficient funds.")
            return
        self.balance -= amount
        self._add_Transactions("Withdrawal", -amount)
        print(f"Withdrawn {amount} Taka successfully. Current balance: {self.balance} Taka")

    def check_balance(self):
        print(f"Account balance for {self. holder_name}: {self.balance}Taka")

    def view_transactions(self):
        print(f"\nTransaction History for {self.holder_name}:")
        if not self.transactions:
            print("No transactions available.")
            return
        for txn in self.transactions:
            print(f"{}")