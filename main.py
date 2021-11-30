from CashFlow import CashFlow 
from simulation import simulate
from Accounts import *
from constants import * 
import plotly.graph_objects as go

if __name__ == "__main__":

# account balances -> initialize to currentYear balances 
    bankAccount = BankAccount(50000, 50000)
    investmentAccount = InvestmentAccount(100000, stockReturnRate, .8)
    fo1kAccount = InvestmentAccount(100000, stockReturnRate, .9)

    # cashflows
    incomes = []
    expenses = []

    # Create income sources 
    incomes.append(CashFlow("job", 125000, currentYear, retireYear, 0))
    incomes.append(CashFlow("SocSec", 25000, govtRetireYear, defDeadYear, inflation))  # SocSec gets COLA adjustments https://smartasset.com/retirement/social-security-calculator#vl3RcQqwQG

    # create expense sources:
    expenses.append(CashFlow("MyMortgage", -2000*12, currentYear, 2021 + 30, 0))
    expenses.append(CashFlow("Spending", -3000*12, currentYear, defDeadYear, inflation))
    expenses.append(CashFlow("kid1", -1000*12, 2023, 2043, inflation))
    expenses.append(CashFlow("kid2", -1000*12, 2025, 2045, inflation))

    # simulate retirement
    bankData, investmentData, fo1kData, incomeData, expenseData = simulate(bankAccount, investmentAccount, fo1kAccount, incomes, expenses, currentYear, defDeadYear, govtRetireYear)

    years = [i for i in range(currentYear, defDeadYear)]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=bankData, mode='lines+markers', name="Bank"))
    fig.add_trace(go.Scatter(x=years, y=investmentData, mode='lines+markers', name="Investment"))
    fig.add_trace(go.Scatter(x=years, y=incomeData, mode='lines+markers', name="Income"))
    fig.add_trace(go.Scatter(x=years, y=expenseData, mode='lines+markers', name="Expenses"))
    fig.add_trace(go.Scatter(x=years, y=fo1kData, mode='lines+markers', name="401K"))
    fig.update_yaxes(type="log", range=[4, 7])  # 10^4 - 10^7
    fig.show()    
