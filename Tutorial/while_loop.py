name = input("Enter your name: ")


while name == "":
    print("You did not enter your name. Please try again.")
    name = input("Enter your name: ")


print(f"Hello, {name}")
# Mistakenly used else here (I thought else was needed here.)

# else:
#     print(f"Welcome, {name}")

