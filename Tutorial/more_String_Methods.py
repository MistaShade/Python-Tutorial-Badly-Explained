phone_Num = input("Please input your phone number: ")


first_Check = phone_Num.isdigit()

# .replace one of the most helpful string methods imo. Replaces the character within the string. 
# Basically, what you are saying here is: replace - with 0. Thus, all - will turn into a 0
convert = phone_Num.replace("-", "0")

# .count basically counts how many inserted character are within the string 

second_Check = phone_Num.count("-")
# convert = phone_Num.replace("-", "0")

# If you need a list / guide of different kinds of string methods in Python(There's A LOT OF EM!!!) type this command:
print(help(str))

result = "We have registered your phone number" if first_Check or second_Check == 3 else "your phone number is invalid."

print(result)
print(convert)