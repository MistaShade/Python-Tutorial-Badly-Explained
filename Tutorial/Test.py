#Strings
last_Name = 'Quixote'
food = "HemoBar"
email = "ESQUIIIRREEEEE@gmail.com"

#Integers
age = 42

#Float
percentage = 99.9

#Boolean
is_Bloodfiend = True
for_Sale = True

print(last_Name + " is " + str(age))

# str will convert the integer to a string
# This is a simple print statement that combines a string and an integer

print("")

print(f"Hello,  {last_Name} You are {age}")
print("")

print(f"and your favorite food is {food}")
print("")

print(f"Your email is {email}")
print("")

print(f"You're {percentage}  percent dreaming")
print("")

print(f"Is Quixote a bloodfiend?: {is_Bloodfiend}")
print("")

if is_Bloodfiend:
    print("Is a Bloodfiend")

else: 
    print("Not a Bloodfiend")

print("")

if for_Sale:
    print("Hemobar is for sale")

else:
    print("Hemobar is not for sale")

print("")