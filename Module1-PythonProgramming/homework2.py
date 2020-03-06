# 1 ----------------
# Accept a number, determine whether the inputted number is even or odd
# ------------------

# testNum = int(input('Please input a number: '))

# if (testNum%2 == 0):
#     print('GENAP !!!')
# else:
#     print('GANJIL !!!')

# 2 ------------------
#---------------------

import math
from termcolor import colored

bodyWeight = float(input('\nWhat\'s your weight? (kg) '))
bodyHeight = int(input('What\'s your height? (cm) '))

bodyHeight /= 100 # convert to meter

print('Weight : {} kg. Height: {}m'.format(bodyWeight, bodyHeight))

imt = bodyWeight / math.pow(bodyHeight, 2)

print('IMT: {}\n'.format(imt))

if (imt>39.9):
    print(colored('--> OBESE!','red'))
elif(imt>30 and imt<39.9):
    print(colored('--> OVERWEIGHT', 'yellow'))
elif(imt>25 and imt<30):
    print(colored('--> SLIGHTLY OVERWEIGHT', 'yellow'))
elif(imt>18.5 and imt<25):
    print(colored('--> IDEAL!! YAY!', 'green'))
else:
    print(colored('--> TOO THIN!','red'))

print('\n')