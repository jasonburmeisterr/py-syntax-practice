# python weight converter project
# practical elif if else
# @jasonburmeisterr 10/28/26

print("Welcome to a weight convertor in python where you can convert weight metrics like Milligrams (mg), Grams (g), Kilograms (kg), and Metric Tons (t) ")

print("")

answer = input("Which weight metric you want to convert? '(mg) (g) (kg) (t)':   ")

if answer == "mg":
    answer2 = input("which metric would you like to convert to? '(g) (kg) (t)':   ")
elif answer == "g":
    answer2 = input("which metric would you like to convert to? '(mg) (kg) (t)':   ")
elif answer == "kg":
    answer2 = input("which metric would you like to convert to? '(mg) (g) (t)':   ")
elif answer == "t":
    answer2 = input("which metic would you like to convert to? '(mg (kg) (g)':   ")
else:
    print(f" The metric '{answer}' is not recognized. Please try again.")

number1 = float(input(f"Enter a number for {answer}:  "))

if answer == "mg" and answer2 == "g":
    answer2 = number1 / 1000
    print(f"{answer2}g")
elif answer == "g" and answer2 == "mg":
    answer2 = number1 * 1000
    print(f"{answer2}mg")
elif answer == "mg" and answer2 == "kg":
    answer2 = number1 / int(1e6)
    print(f"{answer2}kg")
elif answer == "kg" and answer2 == "mg":
    answer2 = number1 * int(1e6)
    print(f"{answer2}mg")
elif answer == "mg" and answer2 == "t":
    answer2 = number1 / int(1e+9)
    print(f"{answer2}t")
elif answer == "t" and answer2 == "mg":
    answer2 = number1 * int(1e+9)
    print(f"{answer2}mg")
elif answer == "g" and answer2 == "kg":
    answer2 = number1 * 1000
    print(f"{answer2}kg")
elif answer == "kg" and answer2 == "g":
    answer2 = number1 * 1000
    print(f"{answer2}kg")
elif answer == "g" and answer2 == "t":
    answer2 = number1 / int(1e+6)
    print(f"{answer2}t")
elif answer == "kg" and answer2 == "t":
    answer2 = number1 / int(1000)
    print(f"{answer2}t")
elif answer == "t" and answer2 == "kg":
    answer2 = number1 * int(1000)
    print(f"{answer2}kg")





    

    


