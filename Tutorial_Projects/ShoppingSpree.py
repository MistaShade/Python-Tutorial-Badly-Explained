# Input name
# Pick a power up (Types of powerups? Will think about it)
# Introduction
# Random Events

# Put the item's stats here perhaps?


player_Money = 100
player_Lives = 200
player_Attacks = 10

employees_Lives = 100
employees_Attacks = 20
employees = 5

# Items :3

# Good Items
# Put them in an array perhaps?
# And call them once they are needed (like call each of them inside an array)
mountain_Dew = player_Attacks * 2


# Bad Items



print("Welcome, to ShoppingSpree.")
player_Name = input("To continue, please eneter your name: ")
input("You will face many crazy employees that will force you to buy their items.")
input("Some items can help you survive")
input("And of course, some items can put you in a disadvantage.")
input("Shop Well.")

print(f"There are {employees}. What are you going to do?")

while player_Lives > 0:
    print(f"There are {employees}. What are you going to do?")
    option = input("What are you going to do?: (A = search the area) (B = talk to an employee)")

    if option == "A":
        input("You decided to search the area")
        # Get a random item



