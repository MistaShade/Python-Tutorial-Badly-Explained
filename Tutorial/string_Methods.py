name = input("Please enter your name: ")

# name.capitalize will capitalize the FIRST letter of your string. Even if you add another part of your name it will only focus on the very first letter.
name = name.upper()

# name.lower will lowercase all of the letters within the string
name = name.lower()

# len basically counts the letters within a string! (REMEMBER! SPACES ARE COUNTED!!)
# result = len(name)

# .find "finds" what yyou have inputted within the string of the variable then it stops when it "finds" what you have inputted. For example, if you put a space within .find it will find a space in the variable's string!

# I do wonder tho! If there's no space, why is it -1? It's probably from the left side and it's saying that it's non-existent. Daz pretty cool!
# Since it starts with 0, if it finds nothing it will go next to 0 which are the non-real numbers (negative)
first_Result = name.find(" ")

# rfind means reverse find
# It will find the LAST occurence of a letter within a string
# If you have multiple letters, for example o then it will mainly focus on the last o
second_Result = name.rfind("o")

# name.digit will only return true or false so, it's a boolean! It will detect if the string contains only digits.
# Reminder: Do not convert your string into a digit. It will still return false. It will only detect strings~
third_Result = name.isdigit()

# name.isalpha() also returns true or false. It will detect if the string only has ALPHABETICAL letters :3
# Reminder: A SPACE is not an alphabetical letter so that means if there's a space within the string then it will return false.
fourth_Result = name.isalpha()

print(f"Your name is {name} and the result is:")
print(first_Result)
print(second_Result)
print(third_Result)
print(fourth_Result)