#Planet Surface gravity

fMercury = 0.38
fVenus = 0.91
fMoon = 0.165
fMars = 0.38
fJupiter = 2.34
fSaturn = 0.93
fUranus = 0.92
fNeptune = 1.12
fPluto = 0.066

sName = input("What is your name: ")
sWeight = input("What is your weight: ")

fweight = float(sWeight)

fMercuryweight = fMercury * fweight
fVenusweight = fVenus * fweight
fMoonweight = fMoon * fweight
fMarsweight = fMars * fweight
fJupiterweight = fJupiter * fweight
fSaturnweight = fSaturn * fweight
fUranusweight = fUranus * fweight
fNeptuneweight = fNeptune * fweight
fPlutoweight = fPluto * fweight

print(sName, "here are your weights on the Solar System's planets: ")

print(f"Weight on Mercury: {fMercuryweight:10,.2f}")
print(f"Weight on Venus: {fVenusweight:10,.2f}")
print(f"Weight on Moon: {fMoonweight:10,.2f}")
print(f"Weight on Mars: {fMarsweight:10,.2f}")
print(f"Weight on Jupiter: {fJupiterweight:10,.2f}")
print(f"Weight on Saturn: {fSaturnweight:10,.2f}")
print(f"Weight on Uranus: {fUranusweight:10,.2f}")
print(f"Weight on Neptune: {fNeptuneweight:10,.2f}")
print(f"Weight on Pluto: {fPlutoweight:10,.2f}")


