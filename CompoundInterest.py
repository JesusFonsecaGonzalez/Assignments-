

PV = float(input("Enter Principle: "))  # 1000.00


R = float(input("Enter Interest Rate: ")) / 100  # 2.5 


t = int(input("How many times per year is the interest compounded?: "))  # 12


m = int(input("For how many years?: "))  # 2


FV = PV * (1 + R / t) ** (m * t)


print(f"At the end of {m} years, you will have ${FV:,.2f}")









"""
CIT-115/115L Python          Professor Brian Candido                            STCC 1 
 
Compound Interest 
 
You will be coding Chapter 2 Programming Exercise 14 Compound Interest.  Refer to the 
book and review the requirements.  In this assignment you will be asking for input of Principal, 
Interest Rate, Compounding Times of Year and the Term Number of Years.    
Using the formula provided you will compute what the money will be worth at the end of the 
term.   A sample output solution is given below.   
Note:  
 Make sure when prompting for input you leave space between the : and the inputted 
value. 
 make sure your output matches it exactly including the formatting of the final answer to 
include a $. 
 
 
Principal Investment (PV): is the present value or principal amount to be invested. 
 
Interest Rate (R): is the annual nominal interest rate or "stated rate" in percent. r = 
R/100, the interest rate in decimal.   
 
For example if the user inputs 2.5, your program must take this value, convert it to a float 
and then divide it by 100 to get the interest percentage into a decimal format such as .025 
 
Number of Periods (t): commonly this will be number of years but periods can be any 
time unit. Enter whole numbers or use decimals for partial periods such as months for 
example, 7.5 years is 7 yr 6 mo. 
 
Compounding (m): is the number of times compounding occurs per period. If a period is 
a year then annually=1, quarterly=4, monthly=12, daily = 365, etc.  
 
Future Value (FV): the calculated future value of our investment 
 
Using the values below would return a FV of $1,051.22 
PV = 1000 
R = 2.5 
t = 2 
m = 12 
 
  
                C       CIT-115/115L Python          Professor Brian Candido 
"""


