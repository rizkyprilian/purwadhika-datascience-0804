import math

# All below functions returns float

# Life of Pi !!! The answer of life
print(math.pi)

# get absolute value from a float number
# fabs....float absolute. get it? FABULUOS!
print(math.fabs(-233.55))

# returns x**y (float)
print(math.pow(2,3))

# return square root of x
print(math.sqrt(256))

# ------------------
# round, ceil, floor
# ------------------

# round float to nearest integer +0.5 returns ceil, -0.5 returns floor
print(round(4.7))
print(round(4.4))

# if the integer is even, it will be same as math.floor 
print(round(4.5)) # return 4

# if the integer is odd, it will be same as math.ceil
print(round(5.5)) # return 6

# take second parameter as number of precision digit
print(round(5.7757727272, 2))


# force floor
print(math.floor(4.7))

# force ceil
print(math.ceil(4.4))

