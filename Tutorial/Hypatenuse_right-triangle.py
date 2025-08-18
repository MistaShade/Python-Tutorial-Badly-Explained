import math

# a = float(pow(input("Input a: " ), 2))
# a = float(pow(input("Input a ", 2)))
# does this work?

a = float(input("Input a: "))
# Less efficient doing them 1 by 1
# a_pow = pow(a, 2)

b = float(input("Input b: "))
# b_pow = pow(b, 2)

# or do this (more efficient probably :3)

# power = pow(a & b, 2)

solution = math.sqrt(pow(a, 2) + pow(b, 2))


# square_root = math.sqrt(solution)
# just add square_root to the solution variable
# More straightforward and requires less of lines code

c = solution

print(f"This is the answer: {c}")