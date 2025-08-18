# Calculate the circumference of the circle

import math

radius = float(input("Radius: "))

circumference = 2 * math.pi * radius

# radius = bool

if radius:
    print(math.floor(circumference))

else: 
    print("Failed to calculate pls try again")

    