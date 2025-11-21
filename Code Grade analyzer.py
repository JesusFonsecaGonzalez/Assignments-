#Code Grade Analyzer

##Grade Analyzer

sName = input("Name of person we are calculating a grade for: ")
iTestScore1 = int(input("Test 1: "))
iTestScore2 = int(input("Test 2: "))
iTestScore3 = int(input("Test 3: "))
iTestScore4 = int(input("Test 4: "))

sTestDrop = input("Do you wish to drop the lowest grade [Y] or [N] ? ")

#if Statements to check if the value is less than 0

if iTestScore1 < 0 or iTestScore2 < 0 or iTestScore3 < 0 or iTestScore4 < 0:
    exit(print("Test scores must be better than 0"))

#Check to see if Y or N

if sTestDrop == "Y" or sTestDrop == "y":
    iTest = 3
    if iTestScore1 < iTestScore2 and  iTestScore1 < iTestScore3 and iTestScore1 < iTestScore4:
        ilow = iTestScore1
    elif iTestScore2 < iTestScore3 and iTestScore2 < iTestScore4:
        ilow = iTestScore2
    elif iTestScore3 < iTestScore4:
        ilow = iTestScore3
    else:
        ilow = iTestScore4

elif sTestDrop == "N" or sTestDrop == "n":
    iTest = 4
    ilow = 0

else:
    exit(print("Enter Y or N to drop the lowest grade"))

#Calculate Average

iAverage = (iTestScore1 + iTestScore2 + iTestScore3 + iTestScore4 - ilow)/ iTest

#Determine letter grade

if iAverage >= 97:
    sGrade = "A+"
elif iAverage >= 94:
    sGrade = "A"
elif iAverage >= 90:
    sGrade = "A-"
elif iAverage >= 87:
    sGrade = "B+"
elif iAverage >= 84:
    sGrade = "B"
elif iAverage >= 80:
    sGrade = "B-"
elif iAverage >= 77:
    sGrade = "C+"
elif iAverage >= 74:
    sGrade = "C"
elif iAverage >= 70:
    sGrade = "C-"
elif iAverage >= 67:
    sGrade = "D+"
elif iAverage >= 64:
    sGrade = "D"
elif iAverage >= 60:
    sGrade = "D-"
else:
    sGrade = "F"

print(sName, "test average is: ", format(iAverage, '.1f'))
print("Letter grade for the test is:", sGrade)
