# format specifiers = {value:flags} format a value based on what flags are inserted

# :.(number)f = round to that many decimal places (fixed point)
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate position value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator

price1 = 3.13159
price2 = -987.65
price3 = 12.34


# This will display 2 decimal places

# print(f"Price 1 is {price1:.2f}")
# print(f"Price 2 is {price2:.2f}")
# print(f"Price 3 is {price3:.2f}")

# This will display 20 spaces

# print(f"Price 1 is {price1:20}")
# print(f"Price 2 is {price2:20}")
# print(f"Price 3 is {price3:20}")

# You can combine that with this! It will add 0s to the spaces

# print(f"Price 1 is {price1:020}")
# print(f"Price 2 is {price2:020}")
# print(f"Price 3 is {price3:020}")

# I guess you can call this one editing the display!(Well I guess this whole thing is all about formatting so...)
# You can command the program to put it on the left justify like this:

# print(f"Price 1 is {price1:<20}")
# print(f"Price 2 is {price2:<20}")
# print(f"Price 3 is {price3:<20}")

# Here's for the right justify
# Since we asked for 20 it will first make spaces for the 20 value to work

# print(f"Price 1 is {price1:>20}")
# print(f"Price 2 is {price2:>20}")
# print(f"Price 3 is {price3:>20}")

# Here's the  center align
# Like what it says it aligns it to the center. Pretty cool stuff

# print(f"Price 1 is {price1:^20}     So Cheap!")
# print(f"Price 2 is {price2:^20}     So Cheap!")
# print(f"Price 3 is {price3:^20}     So Cheap!")

# To know what sign it is (if it's positive or negative in it's current state)
# You can use :+ 


# For example, the original price 2 was a negative value then I used an if else statement to turn it into a positive number. 
# Since it's now a positive number it will display a plus sign (but if it was a negative number it will display a negative sign)
# You can uncomment the if else statement! Try stuff out :3

# if price2:
#     price2 = 987.65
#     print(price2)

# else:
#     print(price2)


# print(f"Price 1 is {price1:+20}")
# print(f"Price 2 is {price2:+20}")
# print(f"Price 3 is {price3:+20}")

# You can use : this format is similar to the previous one but it just removes the plus sign.
# Still figuring out the use of :+ 

# print(f"Price 1 is {price1:20}")
# print(f"Price 2 is {price2:20}")
# print(f"Price 3 is {price3:20}")

# Next, is the :, this basically adds a , to every thousands it sees 
# Here's an example:

# if price1:
#     price1 = 3000.13159
#     price2 = -9087.65
#     price3 = 1200.34

# added an if statement to make the values into thousands
# as you can see (if you executed the program) the thousands have a , symbol pretty cool stuff :3

# print(f"Price 1 is {price1:20,}")
# print(f"Price 2 is {price2:20,}")
# print(f"Price 3 is {price3:20,}")

# Cool thing is, you can mix these format specifiers! For example:

# print(f"Price 1 is {price1:,.20}")
# print(f"Price 2 is {price2:,.20}")
# print(f"Price 3 is {price3:,.20}")

# You can combine them by just adding the sybols after the : 
# So if you want a plus sign with a comma seperator you can say:
# :+,

if price1:
    price1 = 3000.13159
    price2 = -9087.65
    price3 = 1200.34

print(f"Price 1 is {price1:+,}")
print(f"Price 2 is {price2:+,}")
print(f"Price 3 is {price3:+,}")