# validate user input
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits.

name = input("Please enter your name: ")

# My first mistake: 
# first_Check = name.()
# Instead of using this one, do this:

# First Method:
# first_Check= len(name)
# second_Check = name.count(" ")
# third_Check = name.isalpha()

# result = "Welcome, " if first_Check > 12 and second_Check < 1 and third_Check else ("That name is invalid please try again, ")

# if result:
#     print(f"{result}{name}.")


# I prefer the second method cuz it explains the reason why the user's input's wrong
# Second Method:

if len(name) > 12:
    print("Your username should only have no more than 12 characters.")

elif name.count(" ") > 0:
    print("Your username can't contain spaces.") 

# you can use this instead of .count:
# elif not name.find(" ") == -1 :
#     print("Your username can't contain spaces.")


elif not name.isalpha():
    print("Your username can't contain numbers.")

else:
    print(f"Welcome, {name}")