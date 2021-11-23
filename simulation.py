from taxes import incomeTax

def simulate(bAccount, iAccount, fo1kAccount, incomes, expenses, startYear, endYear, govtRetireYear):
    bankData = []
    investmentData = []
    fo1kData = []
    incomeData = []
    expenseData = []

    # simulates balances by year, updating Data[]
    for year in range(startYear, endYear):
        netIncome = 0

        # Handle incomes
        incomeTotal = 0
        for income in incomes:
            if income.startYear <= year <= income.endYear:
                netIncome += income.amount
                incomeTotal += income.amount
                income.annualUpdate()

        # TODO: check this logic... how is 401K taxed?
        # 401K 
        if year >= govtRetireYear:
            fo1withdraw = 0.04 * fo1kAccount.balance()
            fo1kAccount.sell(fo1withdraw, bAccount)
            incomeTotal += fo1withdraw
            netIncome += fo1withdraw
        
        incomeData.append(incomeTotal)

        # Handle taxes
        netIncome -= incomeTax(netIncome, "ca", 'lake forest')

        # Handle expenses
        expenseTotal = 0
        for expense in expenses:
            if expense.startYear <= year <= expense.endYear:
                netIncome += expense.amount # expenses are negative
                expenseTotal -= expense.amount
                expense.annualUpdate()
        expenseData.append(expenseTotal)

        # Handle end of year income or losses
        if netIncome >= 0:
            bAccount.deposit(netIncome)
        else:
            loss = abs(netIncome)
            # bank account can cover loss
            if loss <= bAccount.balance:
                bAccount.withdraw(loss)
            else:
                deficit = iAccount.sell(loss, bAccount)
                bAccount.withdraw(loss)
        
        # TODO: decide how to handle deficit
        
        # Compound interest in investments
        iAccount.compound()
        fo1kAccount.compound()

        # Buy stocks if too much in bank
        if bAccount.overBalance():
            iAccount.buy(bAccount.overBalance())
            bAccount.withdraw(bAccount.overBalance())

        # Sell stocks if not enough in bank
        # else:
        #     iAccount.sell(bAccount.balanceLimit - bAccount.balance, bAccount)

        # Store this year's end of year data as start of next years datat
        bankData.append(bAccount.balance)
        investmentData.append(iAccount.balance())
        fo1kData.append(fo1kAccount.balance())

    return bankData, investmentData, fo1kData, incomeData, expenseData