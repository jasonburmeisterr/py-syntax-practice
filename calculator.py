# Python calculator

import sys

def main():
    print("Welcome to the calculator")

operator = input("Enter an operator (+)'Add' (-)'Subtract' (*)'Multiply' (/)'Divide' (%)'Remainder' :")

if operator == "+":
    value1 = float(input("Enter a number: "))
    value2 = float(input("Enter another number: "))
    total = value1 + value2
    print(f" The sum is: {total}")
elif operator == "-":
    value1 = float(input("Enter a number: "))
    value2 = float(input("Enter another number: "))
    total = value1 - value2
    print(f" The difference is: {total}")
elif operator == "*":
    value1 = float(input("Enter a number:"))
    value2 = float(input("Enter another number:"))
    total = value1 * value2
    print(f" The product is: {total}")
elif operator == "/":
    value1 = float(input("Enter a number:"))
    value2 = float(input("Enter another number:"))
    total = value1 / value2
    print(f" The quotient is: {total}")
elif operator == "%":
    value1 = float(input("Enter a number:"))
    value2 = float(input("Enter another number:"))
    total = value1 % value2
    print(f" The remainder is: {total}")





