name = input("Type your name to proceed: ")
age = int(input("Age: "))
temperature = float(input("Temperature: "))

if name:
    print(f"You may proceed, {name}")
else: 
    print("Please input your name")

if age: 
    print(f"Successfully stored data!, you are {age}")
else:
    print("Data not complete")

if temperature:
    print(f"Your temperature is {temperature}")
else:
    print("Data not complete")