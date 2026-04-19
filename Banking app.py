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
            print(f"{txn['date']} | {txn['type']} | {txn['amount']} Taka | Balance:{txn['balance']} Taka")

    def _add_transaction(self, txn_type, amount):
        txn = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "type": txn_type,
            "amount": amount,
            "balance": self.balance
        }
        self.transactions.append(txn)

    def to_record(self):
        txn_data = ";".join(
            [f"{t['date']}, {t['type']}, {t['amount']}, {t['balance']}" for t in self.transactions]
        )
        return f"{self.account_number}|{self.holder_neme}|{self.balance}|{txn_data}\n"
    
    @staticmethod
    def from_record(line):
        parts = line.strip().split("|")
        if len(parts) < 4:
            return None
        account_number = parts[0]
        holder_name = parts[1]
        balance = float(parts[2])
        account = Account(account_number, holder_name, balance)
        txn_data = parts[3]