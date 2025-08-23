print("Here is the menu: 1. Chicken | 2. Steak | 3. Soup | 4. Noodles |5. Dessert | Input the number of the product")

chicken = 10.6 
steak = 11.4
soup = 8.60
noodles = 7.50
dessert = 867,000

name = input("Pls enter your name: ")
string_Order = input("Would you like to eat something?: ")
order = int(input('What would you like to order?: '))

if name == "":
    print("You have no name!")
    exit()
    # Why does it not exit?

elif string_Order  == "Yes":
    print(f"{name}, have some food")

elif string_Order == "yes":
    print(f"{name}, have some food")


else:
    print("no food for you :3")


if order == 1:
    print(f"Cost: {chicken}")
    new_order = int(input("Would you like another order?: "))
    # planned to do a new_order which asks the user if they want another product which will lead to elif statements that I am not happy of (need to learn more about this)

elif order == 2:
    print(f"Cost: {steak}")

elif order == 3:
    print(f"Cost: {soup}")                    

elif order == 4:
    print(f"Cost: {noodles}")

elif order == 5:
    print(f"Cost: {dessert}")

else:
    print("No order")

