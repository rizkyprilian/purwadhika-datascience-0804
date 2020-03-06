# Rizky Prilian 
# JC-DS-08-04
# 2020/02/19

import math

# 1 ----------------------
# if x = 4
# y = 3
# z = 2
# calculate --> 
# ----------------------

# x = 4
# y = 3
# z = 2

# w = math.pow(((y*z)+x) / (x*y),z)
# print ('value of w is: '+ str(w))

# 2 ------------------
# 1. input any number to a variable (inputNum)
# 2. return inputNum**2
# ------------------

# inputNum = int(input('Please input any number: '))
# print('your number ^ 2 is '+ str(math.pow(inputNum,2)))

# 3 ---------------
# from 485 days, 
# return x years, y month, z days
# assume: 1 year = 360 days, 1 month = 30 days
# ---------------

# days = 485

# year = days // 360 # get how many years
# month = (days % 360) // 30
# week = ((days % 360) % 30) // 7
# daysLeft = ((days % 360) % 30) % 7

# print( str(year) + ' year(s) ' + str(month) + ' month(s) ' + str(week) + ' week(s) ' + str(daysLeft) + ' day(s) ')

# There has to be much more efficient way to do this. But if it works, it's not stupid :))

# 4 --------------
# usiaAndi + usiaBudi = 49
# usiaAndi / usiaBudi = 0.4
# print usiaAndi 2 more years
# print usiaBudi 2 more years
# --------------
# I know the math, but i still don't know how to code it
# x + y = 49
# x = 0.4y
# 0.4y + y = 49
# 1.4y = 49
# y = 49/1.4

# totalAge = 49 # usiaAndi + usiaBudi = 49

# ---> umurBudi = (total * 10) / (10 / (ratioUsia * 10))

# ratioUsia = 0.4 # usiaAndi / usiaBudi = 0.4 . if Andi is 4, Budi is 10. in this case Budi is 1 (or 100%)
# usiaBudi = totalAge / (1 + ratioUsia)
# usiaAndi = totalAge - usiaBudi
# print('Usia Andi 2 tahun lagi: ' + str(usiaAndi+2))
# print('Usia Budi 2 tahun lagi: ' + str(usiaBudi+2))


# 5 ----------------------------
# there is string 'Halo Dunia'
# count how many a
# -----------------------

# kalimat = 'Halo Dunia'
# print(kalimat.count('a'))

# ---> len(kalimat.split('a') - 1)  # -1 karena ada empty string di belakang hasil split


# 6 ---------------------
# There are two vehicles moving onto each other
# A -->            <-- B
# Distance from A to B = 120
# A is moving at 60km/h
# B is moving at 40km/h
# when is A and B are going to collide?
# ----------------------

# collide means A and B meet at each other in between the distance
# assume they will hit at x time
# distance = speed x time
# 60x+40x = 120
# 100x = 120
# x = 1.2 
# they will hit each other at 1 hour 12 minutes

# distanceToEachOther = 120
# speedA = 60
# speedB = 40
# startHour = 9
# collisionTime = ( distanceToEachOther / ( speedA + speedB ) ) + startHour # 9:00 is the time they are departing - at same time

## print('A and B collided at '+ str(collisionTime) + 'hour')

## pretty print

# collisionHour = math.floor(collisionTime)
# collisionMinute = collisionTime - collisionHour
## 1 hour = 60 minutes
# collisionMinute *= 60
# print('A and B will be collided at '+ str(collisionHour) + ':' + str(int(collisionMinute)))


# questions @ github

# 1 -------------------
# get a four digit number
# perform cyclic rotation per two digit
# ----------------------

# inputNumCyclicRotation = int(input('Please input a number: '))
# inputNumCyclicRotation /= 100 # 1234 --> 12.34
# firstTwoDigit = math.floor(inputNumCyclicRotation) # so get the first two integer in the front (before the decimal)
# nextTwoDigit = round((inputNumCyclicRotation - firstTwoDigit), 2) * 100 # now we could get the next two number (after the decimal)
# print('results: '+ str(int((nextTwoDigit*100) + firstTwoDigit)))


# 2 ---------------------
# given a radius of circle (from input)
# calculate the area of the circle
# -----------------------

# pi*(r**2)

# radius = int(input('Please enter the circle radius: '))
# print('Area of the circle is: '+ str(math.pi * math.pow(radius, 2)))

# 3 -------------------
# input 1: 34
# input 2: 98
# output 3948
# ---------------------

# firstNum = int(input('Please enter first num: '))
# secondNum = int(input('Please enter second num: '))

# ## process first num
# ## i want to change 34 ----> 3.04

# firstNum /= 10
# firstIntFromFirstNum = int(math.floor(firstNum))
# secondDecimalFromFirstNum = round((firstNum - firstIntFromFirstNum)/10, 2)
# firstNum = firstIntFromFirstNum + secondDecimalFromFirstNum

# print(firstNum)

# ## process second num
# ## i want to get 0.908 from 98
# secondNum /= 10
# firstIntFromSecondNum = int(math.floor(secondNum))
# secondDecimalFromSecondNum = round((secondNum - firstIntFromSecondNum)/10, 2)
# secondNum = round((firstIntFromSecondNum + secondDecimalFromSecondNum)/10, 3)

# print(secondNum)

# print('results --> '+ str(int((firstNum + secondNum)*1000)))


# ---> more simple answer
# tensA = firstNum // 10
# unitA = firstNum % 10

# tensB = secondNum // 10
# unitB = secondNum % 10

# print (tensA * 1000 + tensB * 100 + unitA * 10 + unitB)


# 4 --------------------
# receive text as an input
# receive a character to be removed
# show results
# ----------------------

# text = input('Please input a text: ')
# charToRemove = input('Please enter a character to be removed from above text: ')
# print('results: ' + text.replace(charToRemove,''))

# 5 -------------------
# input two words text
# swap first word and second word
# ---------------------

# swapTextInput = input('Please input a text: ')
# splittedText = swapTextInput.split(' ')
# print('Swapped words: '+ splittedText[1] + ' ' + splittedText[0])
