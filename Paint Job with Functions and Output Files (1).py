#Jesus Fonseca
#Paint Job with Functions and Output files

import math

# getFloatInput
# Asks user for a positive numeric input.

def getFloatInput(sPrompt):
    while True:
        try:
            fValue = float(input(sPrompt + ": "))
            if fValue <= 0:
                print("Error: value must be positive and non-zero.")
            else:
                return fValue
        except ValueError:
            print("Error: please enter a numeric value.")

# getGallonsOfPaint

def getGallonsOfPaint(fSquareFeet, fFeetPerGallon):
    return math.ceil(fSquareFeet / fFeetPerGallon)

# getLaborHours

def getLaborHours(fLaborHoursPerGallon, iGallons):
    return fLaborHoursPerGallon * iGallons

# getLaborCost

def getLaborCost(fLaborHours, fLaborChargePerHour):
    return fLaborHours * fLaborChargePerHour

# getPaintCost

def getPaintCost(iGallons, fPaintPrice):
    return iGallons * fPaintPrice

# getSalesTax

def getSalesTax(sState):
    sState = sState.upper()

    if sState == "CT":
        return 0.06
    elif sState == "MA":
        return 0.0625
    elif sState == "ME":
        return 0.085
    elif sState == "NH":
        return 0.0
    elif sState == "RI":
        return 0.07
    elif sState == "VT":
        return 0.06
    else:
        return 0.0

# showCostEstimate
def showCostEstimate(
    sLastName, sState, iGallons, fLaborHours,
    fLaborCost, fPaintCost, fTaxAmount, fTotalCost
):

    print(f"Gallons of paint: {iGallons}")
    print(f"Hours of labor: {round(fLaborHours, 2)}")
    print(f"Paint charges: ${fPaintCost:,.2f}")
    print(f"Labor charges: ${fLaborCost:,.2f}")
    print(f"Tax: ${fTaxAmount:,.2f}")
    print(f"Total Cost: ${fTotalCost:,.2f}")

    sFileName = sLastName + "_PaintJobOutput.txt"

    with open(sFileName, "w") as f:
        f.write(f"Gallons of paint: {iGallons}\n")
        f.write(f"Hours of labor: {round(fLaborHours, 2)}\n")
        f.write(f"Paint charges: ${fPaintCost:,.2f}\n")
        f.write(f"Labor charges: ${fLaborCost:,.2f}\n")
        f.write(f"Tax: ${fTaxAmount:,.2f}\n")
        f.write(f"Total Cost: ${fTotalCost:,.2f}\n")

    print(f"File: {sFileName} was created")

# main

def main():

    fSquareFeet = getFloatInput("Enter wall space in square feet")
    fPaintPrice = getFloatInput("Enter paint price per gallon")
    fFeetPerGallon = getFloatInput("Enter feet per gallon")
    fLaborHoursPerGallon = getFloatInput("How many Labor hours per gallon")
    fLaborChargePerHour = getFloatInput("Labor charge per hour")

    sState = input("State job is in: ")
    sLastName = input("Customer Last Name: ")

    iGallons = getGallonsOfPaint(fSquareFeet, fFeetPerGallon)
    fLaborHours = getLaborHours(fLaborHoursPerGallon, iGallons)
    fLaborCost = getLaborCost(fLaborHours, fLaborChargePerHour)
    fPaintCost = getPaintCost(iGallons, fPaintPrice)
    fTaxRate = getSalesTax(sState)


    fTaxAmount = (fLaborCost + fPaintCost) * fTaxRate
    fTotalCost = fLaborCost + fPaintCost + fTaxAmount


    showCostEstimate(
        sLastName, sState, iGallons, fLaborHours,
        fLaborCost, fPaintCost, fTaxAmount, fTotalCost
    )

# Run program

if __name__ == "__main__":
    main()
