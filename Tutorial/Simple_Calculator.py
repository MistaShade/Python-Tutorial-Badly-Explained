num1 = float(input("First number: "))
op = input("Sign: ")
num2 = float(input("Second number: "))

if op == "-":
   # Can I add a string here?
   ans = num1 - num2
   print(round(ans, 3))

elif op == "+":
   ans = num1 + num2
   print(round(ans, 3))

elif op == "/":
   ans = num1 / num2
   print(round(ans, 3))
    
elif op == "*":
   ans = num1 * num2
   # How to add an f string here?
   print(round(ans, 3))

else:
   print("That operator does not exists!")

# Multiple ops? (problem)
