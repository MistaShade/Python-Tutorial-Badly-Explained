# String
name = 'Cody'

# Notice that num is a String
num = "24"

#Integer
age = 24

#Float
online_Rate = 2.4

#Boolean
is_Online = False
is_Number = False

if is_Online:
    print(f"{name} is online")

else:
    print(f"{name} is not online")

# Conditionals 
if is_Number:
    print(f"This is a number")

else: 
    # Converted that num into a string
    name = bool(name)
    num = int(num)

    print("I will convert it into a number " + " and add it with " + str(age + num))
    print(type(num))
    print(name)