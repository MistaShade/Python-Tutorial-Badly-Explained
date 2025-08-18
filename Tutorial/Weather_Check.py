temp = float(input("Input the temperature: "))
weather = input("Is it raining? (Y | N): ")
a = True
is_raining = False

if temp >= 40 or is_raining or temp < 0 or weather == "Y":
    if temp > 40 or temp < -20:
        print("Dangerous temperature!")

    elif weather == "Y":
        print("It is raining")

    print("Do not go to the event")

else:
    print("Perfect day to go to an event!")

print(a)
