def add(num1: int, num2: int):
    return num1 + num2


def subtract(num1: int, num2: int):
    return num1 - num2


def multiply(num1: int, num2: int):
    return num1 * num2


def divide(num1: int, num2: int):
    return num1 / num2


class InsufficientFunds(Exception):
    pass

def test_bank_set_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

class BankAccount():
    def __init__(self, starting_balance = 0):
        self.balance = starting_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            raise InsufficientFunds("Insufficeint balance!")
        self.balance -= amount
    
    def collect_interest(self):
        self.balance *= 1.1