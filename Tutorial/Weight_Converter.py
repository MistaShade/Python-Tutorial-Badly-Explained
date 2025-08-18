# 2.205
# K = Kilograms (multiply)
# L = Pounds (divide)
# Lbs (pounds)
# Klg (Kilograms)

user_Input = float(input("Weight: "))
unit = input("Kilograms or Pounds? (K | L): ")


if unit == "K":
    user_Input = user_Input * 2.205
    unit = "kgs."

    if user_Input >= 9000:
     print("You're FAATTT")
     print(f"Your weight is {round(user_Input, 1)} {unit}")

elif unit == "L": 
    user_Input = user_Input / 2.205
    unit = "lbs."

    if user_Input >= 9000:
     print("You're FAATTT")
     print(f"Your weight is {round(user_Input, 1)} {unit}")

# This always activates
else:
    print(f"{unit} is not valid")

# This always activates (always better to put this inside an else if statement in this scenario :3)
print(f"Your weight is {round(user_Input, 1)} {unit}")