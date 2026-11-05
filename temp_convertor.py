# This is a temp convertor

unit = input("Please enter your temp unit (C or F):")

if unit == "C":
     value = float(input("Please enter your value for temp "))
     converted_value = value * 1.8 + 32
     print(f"the converted unit is: {converted_value} degress farenheit")
elif unit == "F":
    value = float(input("Please enter your value for temp "))
    converted_value = value / 1.8 + 32
    print(f"the converted unit is: {converted_value} degress Celsius")
else:
     print("Please enter a valid unit")

