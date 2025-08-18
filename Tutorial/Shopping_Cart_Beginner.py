# item = input("What would you like to buy?: ")
# price = float(input("The price of the item?: "))
# quantity = int(input("How many items?: "))

# print(f"You bought {quantity} {item} that will {quantity * price} pesos")

item = input("What would you like to buy?: ")
price = float(input("What is the price of the item?: "))
quantity = int(input("How many would you like to buy?: "))

# Always add another variable where it calculates the other variables. It is a good practice for code efficiency
total = price * quantity

print(f"You bought {quantity} {item}. The total is: {total}")