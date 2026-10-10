# shopping car program

item = input("which item would you like to buy?:")
price = float(input("What is the price of the item?:"))
quantity = int(input("How many would you like?:"))
total = price * quantity

#       Without the if else statement u would have to add like (s) instead of the proper
#       English way of saying things plural presenting based on user input.

if total < 1:
    print(f"You purchased {quantity} {item}s ")
else:
    print(f"You purchased {quantity} {item} ")
print(f"Your total is: ${total}")
print("Thank you for shopping with us we look forward to seeing you next time.")