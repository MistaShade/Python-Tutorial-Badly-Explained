import math

radius = float(input("radius: "))

area = math.pi * pow(radius, 2)

# if you'd like to round it up to 2 decimal places do round(area, 2)
print(f"The area of the circle is: {round(area, 2)}")
