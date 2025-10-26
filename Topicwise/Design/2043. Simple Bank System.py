# https://leetcode.com/problems/simple-bank-system/?envType=daily-question&envId=2025-10-26

from typing import List


class Bank:

    def __init__(self, balance: List[int]):
        self.balance = balance
        self.accounts = len(balance)

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if (
            account1 <= self.accounts
            and account2 <= self.accounts
            and self.balance[account1 - 1] >= money
        ):
            self.balance[account1 - 1] -= money
            self.balance[account2 - 1] += money
            return True
        return False

    def deposit(self, account: int, money: int) -> bool:
        if account <= self.accounts:
            self.balance[account - 1] += money
            return True
        return False

    def withdraw(self, account: int, money: int) -> bool:
        if account <= self.accounts and self.balance[account - 1] >= money:
            self.balance[account - 1] -= money
            return True
        return False
