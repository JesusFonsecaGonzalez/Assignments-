#Author: Review Code
#Date: 6/16/25

# Weight = Earth Weight x Surface Gravity Factor

"""
Planet Surface Gravity 
Factor 
Mercury 0.38
Venus 0.91 
Moon 0.165 
Mars 0.38 
Jupiter 2.34 
Saturn 0.93 
Uranus 0.92 
Neptune 1.12 
Pluto 0.066 
# """

# #1.
# fMERCURY = 0.38
# fVENUS   = 0.91
# fMOON    = 0.165
# fMARS    = 0.38
# fJUPITER = 2.34
# fSATURN  = 0.93
# fURANUS  = 0.92
# fNEPTUNE = 1.12
# fPLUTO   = 0.066

# #2.
# sName = input("Enter Name: ")
# sWeight = input("Enter Weight: ")

# #3.
# fWeight = float(sWeight)

# #4.
# fMercuryWeight = fWeight * fMERCURY
# fVenusWeight   = fWeight * fVENUS
# fMoonWeight    = fWeight * fMOON
# fMarsWeight    = fWeight * fMARS
# fJupiterWeight = fWeight * fJUPITER
# fSaturnWeight  = fWeight * fSATURN
# fUranusWeight  = fWeight * fURANUS
# fNeptuneWeight = fWeight * fNEPTUNE
# fPlutoWeight   = fWeight * fPLUTO

# #5.
# print(sName, "here are your weights on our Solar System's planets:")
# print(f"{'Weight on Mercury:':20s}{fMercuryWeight:10,.2f}")
# print(f"{'Weight on Venus:':20s}{fVenusWeight:10,.2f}")
# print(f"{'Weight on Moon:':20s}{fMoonWeight:10,.2f}")
# print(f"{'Weight on Mars:':20s}{fMarsWeight:10,.2f}")
# print(f"{'Weight on Jupiter:':20s}{fJupiterWeight:10,.2f}")
# print(f"{'Weight on Saturn:':20s}{fSaturnWeight:10,.2f}")
# print(f"{'Weight on Uranus:':20s}{fUranusWeight:10,.2f}")
# print(f"{'Weight on Neptune:':20s}{fNeptuneWeight:10,.2f}")
# print(f"{'Weight on Pluto:':20s}{fPlutoWeight:10,.2f}")

"""
Inter Planetary Weights 
You can calculate a persons weight on the different planets within our solar system by 
multiplying their mass by the gravity factor on the surface of the planet. 
Weight = Earth Weight x Surface Gravity Factor
Planet Surface Gravity 
Factor 
Mercury 0.38 
Venus 0.91 
Moon 0.165 
Mars 0.38 
Jupiter 2.34 
Saturn 0.93 
Uranus 0.92 
Neptune 1.12 
Pluto 0.066
For example if you weigh 100 pounds on earth on Mars you would be: 
Mars Weight 38 = 100 x .38 
You Must Code the following: 
1. Declare Named Constants for each of the planet Surface Gravity Factors.  Make sure 
you name them per the suggested rule in the book. 
2. Prompt the user for a Name and their Earth Weight 
3. Convert the entered Weight to the appropriate numeric data type that can store decimal 
points 
4. Multiply the Earth Weight by each of the planets Surface Gravity Factor
5. Refer to the sample output below and make sure you include the following requirements: 
 Output the inputted name and make sure the words Solar Systems includes the 
single quote 
 Make sure all the computed planet weights are lined up exactly in the sample 
output 
 The outputted weight needs to take up 10 positions with 2 decimal points.  
 Test with 70.5 to make sure code works.  Then try your own weight. 
6. Use comments to document your code 
7. Put s prefixes in front of variables that contain string values and n prefix for variables 
that contain numbers.
"""
# #1.
# fMERCURY = 0.38
# fVENUS   = 0.91
# fMOON    = 0.165
# fMARS    = 0.38
# fJUPITER = 2.34
# fSATURN  = 0.93
# fURANUS  = 0.92
# fNEPTUNE = 1.12
# fPLUTO   = 0.066


fMERCURY = 0.38
fVENUS   = 0.91


sName = input("Enter Name: ")
fWeight = float(input("Enter Weight: ")) # "125"

#

# float() 5.5

# int() 5

# sWeight = input("Enter Weight: ")

# fWeight = float(sWeight)



fMercuryWeight = fWeight * fMERCURY #multiply the inputted weight by the gravity factor

fVenusWeight = fWeight * fVENUS


print("your weight on mercury is ", fMercuryWeight)

print("your weight on mercury is ", fVenusWeight)


print(f"{'Weight on Mercury:':20s}{fMercuryWeight:10,.2f}")



















sName = input("Enter Name: ")
fWeight = float(input("Enter Weight: "))

fMercuryWeight = fWeight * fMERCURY
fVenusWeight = fWeight * fVENUS

print("moose here are your weights on the Solar System's planets")

#simple way
#print("Weight on Mercury:", fMercuryWeight)
#print("Weight on Venus:",   fVenusWeight)

#print using an f string or fast string

#print(f"{'Weight on Mercury:':20s}{fMercuryWeight:10,.2f}")

print(f"Weight on Mercury: {fMercuryWeight:,.2f}")
print(f"Weight on Venus: {fVenusWeight:,.2f}")