import matplotlib.pyplot as plt
import colorama
from colorama import Fore
# Python program to calculate monthly EMI (Equated Monthly Installment)

# EMI Formula = p * r * (1+r)^n/((1+r)^n-1)

# If the interest rate per annum is R% then 
# interest rate per month is calculated using: 

# Monthly Interest Rate (r) = R/(12*100)

# Varaible name details:
# p = Principal or Loan Amount
# r = Interest Rate Per Month
# n = Number of monthly installments

# Reading inputs from user
print(Fore.RED +"............................Welcome you to EMI calculator......................................")
p = float(input(Fore.GREEN +"Enter principal amount:- "))
R = float(input(Fore.RED+"Enter annual interest rate: "))
n = int(input(Fore.CYAN+"Enter number of months: " ))

# Calculating interest rate per month
r = R/(12*100)

# Calculating Equated Monthly Installment (EMI)
emi = p * r * ((1+r)**n)/((1+r)**n - 1)

print(Fore.YELLOW+"Monthly EMI = "+Fore.MAGENTA+" ","{:,}".format(emi))