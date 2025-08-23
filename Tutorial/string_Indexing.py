# indexing = accessing elements of a sequence using [] (indexing operator)
#                   [start : end : step]

credit_CardNum = "1987-8943-4562"

# print(credit_CardNum[0])
# print(credit_CardNum[0:4])
print(credit_CardNum[5:])

# you can also use - numbers that's pretty cool
# My only explanation from this is since the starting index is always 0 right? Then that means it will go to the right side since there are no more existing numbers to the left side 
# So it went to the right :3 
print(credit_CardNum[-1])

# This should print 2


# We'll now be doing the step!!! :3
# So step basically tells the program how many digits we're going to step on (wait...)
# and it will print each number after it steps on the amount of digits (ahma just visualize it :3)


print(credit_CardNum[::3])
# Since we said the program to step on 3 digits it will print the 3RD DIGIT and 3RD digit
# credit_CardNum = "1987-8943-4562"
# In this case, 1, 7, 9, -, and 6 will be printed!
# note: it will always start with the first digit ever digit (since we start with 0 it'll include it)