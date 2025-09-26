# for C (C * 9 / 5) + 32 = F

user_Input = input("Fahrenheit or Celsius (F | C): ")
temp = float(input("Temperature: "))

if user_Input == "F":
    # formula here
    # Wrong formula
    # temp = temp * 9 / 5 + 32
    temp = round((temp - 32) * 5 / 9, 1)
    print(f"Your temperature is {temp}")

elif user_Input == "C":
    # formula here
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"Your temperature is {temp}")

else: 
    print(f"{user_Input} is not valid.")

