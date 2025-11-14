PV = float(input("Enter the starting principle: ")) # 1000.00

r = float(input("Enter the annual interest rate: ")) /100 # 2.5

t = int(input("How many times per year is the interest compounded: ")) # 12

m = int(input("For how many years will the account earn interest: ")) # 2



FV = PV * (1 + r / t) ** (m * t)  #Formula


print(f"At the end of {m} years, you will have ${FV:,.2f}")  #Result
