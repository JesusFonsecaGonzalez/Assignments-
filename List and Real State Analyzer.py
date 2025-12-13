#Jesus Fonseca
#List and Real State Analyzer

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

#Get median

def getMedian(flist):
    if (len(flist) % 2) == 0:
        iIndexEnd = len(flist)//2
        iIndexStart = len(flist)//2-1
        fMedian = (flist[iIndexStart] + flist[iIndexEnd]) / 2


    else:
        iIndex = len(flist)//2
        fMedian = flist[iIndex]

    return fMedian

#Code Main

def main():
    RealEstateList = []
    fCOMMISIONRATE = 0.03

    fRealEstateValue = getFloatInput("Enter Property Sale Value")
    RealEstateList.append(fRealEstateValue)

    while True:
        sInput = input("Enter another value Y or N ")

        if sInput == "Y" or sInput == "y":
            fRealEstateValue = getFloatInput("Enter Property Sales Value")
            RealEstateList.append(fRealEstateValue)
        elif sInput == "N" or sInput == "n":
            break
        else:
            pass

    RealEstateList.sort()
    fMedian = getMedian(RealEstateList)

    for iProperty in range(len(RealEstateList)):
        print("Property", str(iProperty+1), "$", format(RealEstateList[iProperty], '11,.2f'))

    #Print and format output

    print("Min:", format(min(RealEstateList), '12,.2f'))
    print("Max:", format(max(RealEstateList), '12,.2f'))
    print("Total:", format(sum(RealEstateList), '12,.2f'))
    print("Average:", format((sum(RealEstateList)/len(RealEstateList)), '12,.2f'))
    print("Median:", format(fMedian, '12,.2f'))
    print("Commission", format((sum(RealEstateList) * fCOMMISIONRATE), '12,.2f'))


main()

















