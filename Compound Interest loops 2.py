#Compound interest loops
#Jesus Fonseca

#Get staring principal

fStartingPrincipal = 0

while fStartingPrincipal <= 0:
    try:
        fStartingPrincipal = float(input("What is the Original deposit value (positive value): "))
        if fStartingPrincipal <= 0:
            print("Input must be a positive numeric value")
    except ValueError:
        print("Input must be a positive numeric value")

#Get the interest rate

fInterestRate = 0

while fInterestRate <= 0:
    try:
        fInterestRate = float(input("What is the Interest Rate (positive value)")) / 100
        if fInterestRate <= 0:
            print("input must be a positive numeric value")
    except ValueError:
        print("Input must be positive numeric value")

fInterestRate = fInterestRate / 12

#Get months

iMonths = 0

while iMonths <= 0:
    try:
        iMonths = float(input("What is the number of months (positive value): "))
        if iMonths <= 0:
            print("You must enter a positive value")
    except ValueError:
        print("Input must be a positive numeric value")

#Get Goal

fGoal = -1

while fGoal < 0:
    try:
       fGoal = float(input("What is the Goal amount (can be 0 but not negative)"))
       if fGoal < 0:
           print("Input must 0 or greater")
    except ValueError:
        print("Input must be 0 or greater")

#Get the interest per month

iTime = 0

while iTime < iMonths:
    iTime +=1
    fCompoundInterest = fStartingPrincipal * ((1 + fInterestRate) ** (iTime))
    print("Month:, ", iTime, "Account Balance: $ " + format(fCompoundInterest, ".2f"))

 ## How many months it takes to reach Goal

iTime = 0
fCompoundInterest = fStartingPrincipal * ((1 + fInterestRate) ** (iTime))

while fCompoundInterest < fGoal:
    iTime += 1
    fCompoundInterest = fStartingPrincipal * ((1 + fInterestRate) ** (iTime))


print("It will take: ", iTime, "months to reach the goal of $" + format(fGoal, ".2f"))









