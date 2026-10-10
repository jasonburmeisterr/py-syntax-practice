#              A beginner project for getting more fluent with py syntax.
#         A calculator that prompts input from the user and does a simple--
#          Multiplication equation to calculate V = L * W * H  as the output or as you may know... I hope.
#                        Volume of a cuboid or rectangular prism whatever you want to call it.

# First we need to set a variable from user prompt inputs
length = float(input("What is your measured length?:"))
width = float(input("What is your measured width?:"))
height =  float(input("What is your measured height?:"))
volume = length * width * height
# Then the output which is simply multiplies all 3 inputs to get "V" or volume.
print(f"The volume of your rectangular prism is {volume}m³")
