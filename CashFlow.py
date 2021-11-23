class CashFlow:
    name = ""
    startAmount = 0
    amount = 0
    startYear, endYear = 0, 0, 
    annualIncreaseRate = 0

    def __init__(self, name, amount, startYear, endYear, annualIncreaseRate) -> None:
        self.name = name
        self.amount = self.startAmount = amount
        self.startYear = startYear
        self.endYear = endYear
        self.annualIncreaseRate = annualIncreaseRate
    
    def annualUpdate(self):
        self.amount *= 1 + self.annualIncreaseRate

    def __str__(self) -> str:
        return self.name + ": " + str(self.amount)