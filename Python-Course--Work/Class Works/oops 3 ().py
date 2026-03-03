# Abstraction means hiding internal implementation details and showing only the essential features to the user.
# Simple Real-World Example
# When you use an ATM:
# You see: withdraw, deposit, balance
# You don’t see: bank server logic

from abc import ABC,abstractmethod
class BankAccount:
    @abstractmethod
    def withdraw(self):
        pass
    def deposit(self):
        pass
    def check_balance(self):
        print("you can view your balance account")
    def view_statements(self):
        print("you can check out your history")
    def set_pin(self):
        print("you can change the pin")
class savingsAccount(BankAccount):
    def withdraw(self):
        print("[withdraw]:you can with as many times until your money is over")
    def deposit(self):
        print("[deposit]:you deposit 50k")
class CurrentAccount:
    def withdraw(self):
        print("[withdraw]:you can with as many times until your money is over")
    def deposit(self):
        print("[deposit]:you deposit 51")
class JointAccount:
    def withdraw(self):
        print("[withdraw]:40k from both parties")
    def deposit(self):
        print("[deposit]:101 can be deposited")
class salaryAccount():
    def withdraw(self):
        print("[withdraw]:max 1l")
    def deposit(self):
        print("[deposit]:once in a month and 21")
class FixedDepositeAccount(BankAccount):
    def withdraw(self):
        print("[withdraw]:you can withdraw once")
    def deposit(self):
        print("[deposit]:you can depositeb  50k")