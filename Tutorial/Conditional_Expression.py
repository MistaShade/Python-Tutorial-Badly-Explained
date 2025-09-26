# num = 6
# a = 20
# b = 26
# age = 25
# temperature = 33

num = int(input("Enter a number: "))
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
temperature = int(input("Input the temperature: "))
age = int(input("Please enter your age: "))
age_restriction = False


# Is there a way for me for these inputs to be just a singular line? It feels "Unorganized..." I want the program to like have these processing phase to give an illusion that it is "thinking" evil I know! Teehee~ (that was cringe)
input("Processing...")
input("Processing...")
input("Processing...")
input("Got it!!!")

# Positive or Negative
# print(f"the number: {num} is Positive" if num >= 0 else "the number: {num} is Negative")

# Odd or Even
# print(f"the number: {num} is Even" if num % 2 == 0 else "the number: {num} is Odd")

# I prefer this way :3
# Is there a way for me to add the num in the strings? Hmmmm...

# This says print a if a is GREATER than b else just print B bro :3

# Combine max_num and result and the result say whether the output of max_num is Odd or Even
max_num = a if a > b else b
min_num = a if a < b else b

# Why doesn't this work I wonder? Oh I added age-restriction = True it should only be else True!
check = age_restriction if age > 18 else True

# used to put age_restriction on this if statement which is wrong. It should be check since check = to statement
if check:
    print("Hey!!! You're not allowed to use this!!")

else:
    print("Hope this helps you!")

result = "The number is even" if num % 2 == 0 else "The number is odd"
print(result)
print(max_num)