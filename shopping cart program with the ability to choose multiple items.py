# shopping cart program
#      My main struggle here was the loop logic itself
#       Also remembering that float still needs to be followed by float(input)

variety = int(input("How many different items would you like?:"))
total = 0           # start it at 0, before my loop 


for i in range(variety):
    item = input("Which item would you like?: ")
    price = float(input("what is the price of the item?: ")) 
    quantity = float(input(f"how many {item}s would you like?:"))
    total = total + price * quantity
print(f"Your total is: ${total}") 
print("Thank you for shopping with us, we look forward to seeing you next time")
    #print you purchased blah blah blah and i successfully wrote a loop with a running total. 
