numOfRow = int(input('num of row: '))

# -----------------------
print('\n')
# -----------------------
# this question doesn't involves row num
# t1 = ''

# for row in range(numOfRow):
#     t1 += ' * '

# print(t1)

# -----------------------
print('soal no 2: \n')
# -----------------------

t2 = ''

for item in range(0,numOfRow):
    t2 += ' * \n'

print(t2)

# -----------------------
print('soal no 3: \n')
# -----------------------

t3=''

for row in range(numOfRow):
    for row1 in range(numOfRow):
        t3 += ' * '
    t3 += '\n'

print(t3)

# -----------------------
print('soal no 4: \n')
# -----------------------

t4=''

for row in range(numOfRow):
    for row1 in range(0, row+1):
        t4 += '* '
    t4 += '\n'

print(t4)

# -----------------------
print('soal no 5: \n')
# -----------------------

t5=''

for row in range(numOfRow):
    for row1 in range(0, (row*-1)+numOfRow):
        t5 += '* '
    t5 += '\n'

print(t5)

# -----------------------
print('soal no 6:\n')
# -----------------------


t6 = ''

# there are going to be two iteration:
# 1. upper part iteration
# 2. below part iteration

# first we are going to get how many iteration needed for each part
numOfIterationForEachPart = numOfRow // 2
# for odd number, we need to add one extra iteration on the upper part
extra = 0
if (numOfRow%2 != 0):
    extra = 1

# 1. upper part iteration
for row in range(0, numOfIterationForEachPart+extra):
    for row1 in range(0, (row*-1)+numOfIterationForEachPart+extra):
        t6 += '* '
    t6 += '\n'

# 2. below part iteration

### below code is working :)
# for row in range(0,numOfIterationForEachPart):
#     for row1 in range(0, row+2):
#         t6 += '* '
#     t6 += '\n'

### but, inversing the range also works :).
for row in range(numOfIterationForEachPart-1, -1, -1):
    for row1 in range(0, (row*-1)+numOfIterationForEachPart+extra):
        t6 += '* '
    t6 += '\n'

print(t6)

# -----------------------
print('soal no 7: \n')
# -----------------------

t6 = ''

# for row in range(numOfRow):

#     for space in range(0, (row*-1)+(numOfRow-1)):
#         t6 += '  '

#     # calculate number of stars
#     for star in range(0, (2*row)+1):
#         t6 += '* '
#     t6 += '\n'


for i in range(0, numOfRow, 1):
    for j in range (0, (numOfRow*2)+1):
        
        if j <= numOfRow - i and j >= numOfRow + 1:
            t6 += ' * '
        else:
            t6 += '   '
    t6 += '\n'

print(t6)




# -----------------------
print('soal no 8: \n')
# -----------------------

t7 = ''
k = (2*numOfRow) - 1

for row in range(numOfRow):
    # calculate number of spaces
    for space in range(0, row):
        t7 += '  '

    # calculate number of stars
    for numOfStars in range(0, (row*-2)+k):
        t7 += '* '

    t7 += '\n'

print(t7)

# -----------------------
print('soal no 9 (diamond): \n')
# -----------------------

t8 = ''
# there are going to be two iteration (same as qs no 6)
# i am going to re-use those variables

# 1. upper part iteration
for row in range(numOfIterationForEachPart+extra):

    for space in range(0, (row*-1)+((numOfIterationForEachPart+extra)-1)):
        t8 += '  '

    # calculate number of stars
    for star in range(0, (2*row)+1):
        t8 += '* '
    t8 += '\n'

# 2. below part iteration

### below code is working :)
# k = (2*numOfIterationForEachPart) - 1

# for row in range(numOfIterationForEachPart):
#     # calculate number of spaces
#     for space in range(0, row+extra):
#         t8 += '  '

#     # calculate number of stars
#     for numOfStars in range(0, (row*-2)+k):
#         t8 += '* '

#     t8 += '\n'

### but, inversing the range also works :).
for row in range(numOfIterationForEachPart-1,-1,-1):

    for space in range(0, (row*-1)+((numOfIterationForEachPart+extra)-1)):
        t8 += '  '

    # calculate number of stars
    for star in range(0, (2*row)+1):
        t8 += '* '
    t8 += '\n'

print(t8)