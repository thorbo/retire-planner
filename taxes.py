import math
# TODO: deductions

# Tax brackets represented as dict:
# key: bracket upper limit, value: bracket tax rate
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
        8932: 0.01, 
        21175: 0.02,
        33421: 0.04,
        46394: 0.06,
        58634: 0.08,
        299508: 0.093,
        359407: 0.103,
        599012: 0.113, 
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

def incomeTax(income, state, city):

    def stateTax(income, state):
        return tax(income, brackets_state[state])

    def federalTax(income):
        return tax(income, brackets_fed_married_jointly)

    def localTax(income, city):
        return tax(income, brackets_city[city])

    def ficaTax(income):
        return 0.075 * income

    # print(income, stateTax(income, state) + federalTax(income) + localTax(income))
    return stateTax(income, state) + federalTax(income) + localTax(income, city) + ficaTax(income)