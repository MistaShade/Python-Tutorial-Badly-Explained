money = 0
money = money + 1

# or you could do this 
money += 1
money -= 1
money *= 1
money /= 1
# This is known as augmented assignment operator

money = money ** 2

# ** is called an exponentiation! (you know what it does! It is basically saying amount of money powered by 2!)

money **= 2
# augmented assignment operator version

remainder = money % 2

# % is called a modulus it will give the remainder of any division
# super useful for identifying what is odd or even

# ** means to the power of
friend = "None"
friend = input("Name of your friend: ")
print(friend)
print(f"You have {remainder}")