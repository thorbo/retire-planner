class BankAccount():
    balanceLimit = 0
    name = ""
    balance = 0
    def __init__(self, balance, balanceLimit):
        self.balance = balance
        self.balanceLimit = balanceLimit

    def withdraw(self, amount):
        self.balance -= amount
    
    def deposit(self, amount):
        self.balance += amount

    def overBalance(self):
        return self.balance - self.balanceLimit if self.balance > self.balanceLimit else 0

class InvestmentAccount(): 
    returnRate = 0
    stockAllocation = 1
    
    def __init__(self, balance, returnRate, stockAllocation):
        self.stocks = []
        self.stocks.append([balance, 0])
        self.returnRate = returnRate
        self.stockAllocation = stockAllocation
        

    def compound(self, years=1):
        for i, stock in enumerate(self.stocks):
            self.stocks[i][1] = sum(stock) * (1 + self.returnRate * self.stockAllocation) * years - self.stocks[i][0]

    def sell(self, amount, bAccount):
        # return: amount not sold
        # TODO: LTCapitalGainsTax(amount)
        
        while self.stocks:
            # always operate on the earliest stock (first in list)
            stockAmount = sum(self.stocks[0])
            if amount <= stockAmount:
                percentToSell = amount / stockAmount
                self.stocks[0][0] -=  self.stocks[0][0] * percentToSell
                self.stocks[0][1] -=  self.stocks[0][1] * percentToSell
                bAccount and bAccount.deposit(amount)
                return 0
            else:
                bAccount and bAccount.deposit(stockAmount)
                amount -= stockAmount
                self.stocks.pop(0)

        # any amount remaining is amount not sold in this transaction
        return amount

    def buy(self, amount):
        self.stocks.append([amount, 0])

    def balance(self):
        total = 0
        for stock in self.stocks:
            total += sum(stock)
        return total