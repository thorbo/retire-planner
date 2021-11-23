from CashFlow import CashFlow
from Accounts import (BankAccount, InvestmentAccount)

revenue = CashFlow("revenue", 100, 2020, 2025, 0.05)
revenue.annualUpdate()
assert(revenue.amount == 100*1.05)
revenue.annualUpdate()
assert(revenue.amount == 100*1.05*1.05)

bAccount = BankAccount(100, 1000)
bAccount.deposit(50)
assert(bAccount.balance == 150)
bAccount.withdraw(50)
assert(bAccount.balance == 100)
assert(bAccount.overBalance() == 0)
bAccount.deposit(1000)
assert(bAccount.overBalance() == 100)

bAccount = BankAccount(100, 1000)
iAccount = InvestmentAccount(100, 0.1, 1)
iAccount.buy(900)
assert(iAccount.balance() == 1000)
iAccount.compound()
assert(round(iAccount.balance()) == 1100)
iAccount.sell(500, bAccount)
assert(round(iAccount.balance()) == 600)
assert(bAccount.balance == 600)


iAccount.sell(700, bAccount)

