import math

# taxes are based on married filing jointly

# Tax brackets represented as dict(bracket upper limit: bracket tax rate)
brackets_fed_married_jointly = {
        20500: 0.10,   
        83550: 0.12, 
        178150: 0.22,
        340100: 0.24,
        431900: 0.32,
        647850: 0.35,
        math.inf: 0.37
    }

brackets_state = {
    "ca" : {
        17864: 0.01, 
        42350: 0.02,
        66842: 0.04,
        92788: 0.06,
        117268: 0.08,
        599016: 0.093,
        718814: 0.103,
        1198024: 0.113, 
        math.inf: 0.123
    },
    "pa": {
        math.inf: 0.031
    }
}

brackets_city = {
    'marysville': {
        math.inf: 0.015
    }, 
    'pittsburgh': {
        math.inf: 0.03
    }, 
    'lake forest': {
        math.inf: 0
    },
}

brackets_LT_capital_gains = {
    80800: 0, 
    501600: 0.15, 
    math.inf: 0.2
}

standard_deductions = {
    "fed": 25100, 
    "ca": 9202,
    "pa": 0,
}

def tax(income, bracketName):
    if income <= 0:
        return 0
        
    taxes = []
    prevBracket = 0
    for bracket in bracketName:
        if prevBracket < income:
            taxes.append((taxes[-1] if len(taxes) else 0) + 
                bracketName[bracket] * min(income - prevBracket, bracket - prevBracket))
        else:
            break
        prevBracket = bracket

    return taxes[-1]

def LTCapitalGainsTax(income):
    return tax(income, brackets_LT_capital_gains)

def stateTax(income, state):
    income -= standard_deductions[state]
    return tax(income, brackets_state[state])

def federalTax(income):
    income -= standard_deductions["fed"]
    return tax(income, brackets_fed_married_jointly)

def localTax(income, city):
    return tax(income, brackets_city[city])

def ficaTax(income):
    return 0.075 * income

def incomeTax(income, state, city):
    return stateTax(income, state) + federalTax(income) + localTax(income, city) + ficaTax(income)

print(stateTax(100000, "ca"))
print(federalTax(100000))