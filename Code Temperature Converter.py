#Code Temperature Converter
## Jesus Fonseca
# Welcome message
print("Welcome to My Temperature Converter")

#Get input

fTemp = float(input("Enter a temperature: "))
sScale = input("Enter C for Celcius or F Farenheit: ")

#Conditional Statements to calculate Conversion

if sScale == "F" or sScale == "f":
    if fTemp > 212:
        print("Temp can't be greater than 212")
        raise SystemExit
    else:
        fCelsius = ((5.0/9) * (fTemp - 32))
        print("The Celcius value is: ", format(fCelsius, '.1f'))

elif sScale == "C" or sScale == "c":
    if fTemp > 100:
        print("Temp can't be greater than 100")
        raise SystemExit
    else:
        fFarenheit = ((9.0/5.0) * fTemp) + 32
        print("The Farenheit value is: ", format(fFarenheit, '.1f'))

else:
    print("Enter F or C")
    raise SystemExit