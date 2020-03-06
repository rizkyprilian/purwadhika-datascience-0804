# Try input function to accept input from user
# Note: \ is escape character

name = input('What\'s your name? ')
age = input('How old are you? ')

# variable that comes from input returns string (str)
# print(type(age))

# if we want to make some calculation on age, we need to convert it to int
age = int(age)

# string concatenation must use string variables. if we want to concat an integer, we have to convert it back to str
print('Your name is: ' + name)
# print('Your age is: ' + age + '---- type' + str(type(age)) ) <<< this will return error since age is still an int
print('Your age is: ' + str(age))

print('Nama saya jika dimunculkan dua kali: '+ name.capitalize()*2)

print('Karakter di nama saya pada posisi modulus 2 umur saya: '+ name[age%2])

print('''Karakter di nama saya pada posisi negatif modulus 2 umur saya lalu
         ditambah 5 hingga sebelum -1 adalah: ''' + name[(-1*(age%2)-5):-1])



