unitFrom = input("Enter the unit you are converting from: ")
unitTo = input("Enter the unit you are converting to: ")
temperature = float(input(f"Enter the temperature in {unitFrom}: "))
#Need from Fahrenheit to Celsius, Celsius to Fahrenheit, Fahrenheit to Kelvin, Kelvin to Fahrenheit, Celsius to Kelvin, Kelvin to Celsius
if (unitFrom == "Fahrenheit"):
    intermediateTemperature = (temperature - 32) * 5/9
elif (unitFrom == "Celsius"):
    intermediateTemperature = temperature
else:
    if (unitFrom == "Kelvin"):
        intermediateTemperature = temperature - 273.15

if unitTo == "Fahrenheit":
    finalTemperature = (intermediateTemperature/(5/9)) + 32
elif unitTo == "Celsius":
    finalTemperature = intermediateTemperature
else:
    if unitTo == "Kelvin":
        finalTemperature = intermediateTemperature + 273.15

print(f"That is {finalTemperature:.1f} degrees {unitTo}.")