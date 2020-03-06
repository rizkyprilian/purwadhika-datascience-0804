# Try input function to accept input from user
# Note: \ is escape character

name = input('What\'s your name? ')
age = input('How old are you? ')

# variable that comes from input returns string (str)
print(type(age))

# if we want to make some calculation on age, we need to convert it to int
age = int(age)

# string concatenation must use string variables. if we want to concat an integer, we have to convert it back to str
print('Your name is: ' + name)
# print('Your age is: ' + age + '---- type' + str(type(age)) ) <<< this will return error since age is still an int
print('Your age is: ' + str(age))
print('Your age 5 years later is ' + str(age+5))
print('Your age modulus 2 is ' + str(age%2))

# This will print different variables
print('Your age is', age)


