import math

def compoundInterest(principal, interestRate, years):
    # P*(1+rate)^years
    return principal*math.pow((1+interestRate), years)

def burnTime(principal, withdrawalAmount, interestRate, inflationRate):
    counter = 0
    while principal > 0:
        principal *= (1+interestRate) 
        principal -= withdrawalAmount
        withdrawalAmount *= (1+inflationRate)
        counter += 1
    return counter


# Years of note
currentYear = 2022
retireYear = 2025
govtRetireYear = 1992 + 60 # assuming same for collecting Social Security

# Interest rates
inflation = 0.035   # average historical value
stockReturnRate = 0.07  # average historical value

# $$$
currentExpense = 50000
current401k = 100000
annualSocSecIncome = 2000 * 12 * 2
stockAtMiniRetirement = compoundInterest(100000, stockReturnRate, retireYear - currentYear)

# Mini retirement
yearsMiniRetirement = burnTime(stockAtMiniRetirement, currentExpense, stockReturnRate*0.8, inflation)
validMiniRetire = yearsMiniRetirement + retireYear > govtRetireYear
print(f"Total stock @ mini-retirement: {stockAtMiniRetirement}")
print(f"Total years of mini-retirement: {yearsMiniRetirement}")
print("------->" + ("" if validMiniRetire else "IN") + "VALID mini-retirement<-------\n")

# Govt. retirement
futureExpense = compoundInterest(currentExpense, inflation, (govtRetireYear - currentYear))
future401kAmount = compoundInterest(current401k, stockReturnRate, (govtRetireYear - currentYear))
yearsRetirement = burnTime(future401kAmount, (futureExpense - annualSocSecIncome), stockReturnRate * 0.6, inflation)
print(f"401k @ big-retirement: {future401kAmount}")
print(f"Annual expenses @ big-retirement: {futureExpense}")
print(f"Years before you need an \"accident\": {yearsRetirement}")

