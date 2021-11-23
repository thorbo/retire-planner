from CashFlow import CashFlow 
from simulation import simulate
from Accounts import *
from constants import * 
import plotly.graph_objects as go

if __name__ == "__main__":

    # account balances -> initialize to currentYear balances 
    bankAccount = BankAccount(10000, 20000)
    investmentAccount = InvestmentAccount(100000, stockReturnRate, .8)
    fo1kAccount = InvestmentAccount(100000, stockReturnRate, .9)

    # cashflows
    incomes = []
    expenses = []

    # Create income sources 
    incomes.append(CashFlow("Ljob", 25000, currentYear, retireYear, 0))
    incomes.append(CashFlow("Jjob", 50000, currentYear, retireYear, 0))
    incomes.append(CashFlow("Ljob", 50000, 2035, 2042, inflation))
    incomes.append(CashFlow("RE_Income", 1100*2*12, 2020, defDeadYear, inflation))
    incomes.append(CashFlow("JSocSec", 25000, govtRetireYear, defDeadYear, inflation))      # https://smartasset.com/retirement/social-security-calculator#vl3RcQqwQG
    incomes.append(CashFlow("LSocSec", 25000, govtRetireYear, defDeadYear, inflation))      # SocSec gets COLA adjustments

    # create expense sources:
    expenses.append(CashFlow("MyMortgage", -2000*12, currentYear, 2021 + 30, 0))
    expenses.append(CashFlow("RE_Mortgage", -1900*12, 2018, 2018 + 30, 0 ))
    expenses.append(CashFlow("Spending", -3000*12, currentYear, defDeadYear, inflation))

    # simulate retirement
    bankData, investmentData, fo1kData, incomeData, expenseData = simulate(bankAccount, investmentAccount, fo1kAccount, incomes, expenses, currentYear, defDeadYear, govtRetireYear)

    years = [i for i in range(currentYear, 2070)]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=years, y=bankData, mode='lines+markers', name="Bank"))
    fig.add_trace(go.Scatter(x=years, y=investmentData, mode='lines+markers', name="Investment"))
    fig.add_trace(go.Scatter(x=years, y=incomeData, mode='lines+markers', name="Income"))
    fig.add_trace(go.Scatter(x=years, y=expenseData, mode='lines+markers', name="Expenses"))
    fig.add_trace(go.Scatter(x=years, y=fo1kData, mode='lines+markers', name="401K"))
    fig.update_yaxes(range=[0, 3000000])
    fig.show()    
