


x = 'Halo Dunia Dunia'

# get length of the string
print(len(x))

# get the first index of the search text
print(x.index('Dunia'))

# split a string into array by a delimiter
print(x.split(' '))

# change case to lowercase
print(x.lower())

# change case to uppercase
print(x.upper())

# change the first letter of the sentence to uppercase
print(x.capitalize())

print(x.replace('Dunia', 'Lalalala', 1))

print(str.index(x,'a'))

# use three quote to write a long string into multiple line
y = '''looooooong text \t
is loooooooooooooooong'''


# substring

text = "I'm Baron, nice to meet you"

# get text index at n
print(text[1])

print(text[:4])

# start from index 2 (included) until index (4)
print(text[2:5])

print(text[:])

# negative index will count from the right side
print(text[-3:])

# reverse >>>>> esrever
print(text[::-1])