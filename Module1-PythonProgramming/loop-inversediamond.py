numOfRow = int(input('num of row: '))

# there are going to be two iteration:
# 1. upper part iteration
# 2. below part iteration

# first we are going to get how many iteration needed for each part
numOfIterationForEachPart = numOfRow // 2
# for odd number, we need to add one extra iteration on the upper part
extra = 0
if (numOfRow%2 != 0):
    extra = 1

t9 = ''

print ('num iteration each part {}'.format(numOfIterationForEachPart))

# 1. upper part iteration
for row in range(0, numOfIterationForEachPart+extra):
    numOfStars = (row*-1)+numOfIterationForEachPart+extra
    numOfInverseSpace = (row*2)+1

    print(row,numOfStars, numOfInverseSpace)
    
    for row1 in range(0, numOfStars):
        t9 += '* '

    for row1 in range(0, numOfInverseSpace):
        t9 += '  '

    for row1 in range(0, numOfStars):
        t9 += '* '
    t9 += '\n'

print('------')
# 2. below part iteration
for row in range(numOfIterationForEachPart-1,-1,-1): 
    numOfStars = (row*-1)+numOfIterationForEachPart+extra # -2x + c + n
    numOfInverseSpace = (row*2)+1 # 2x + 1

    print(row,numOfStars, numOfInverseSpace)

    for row1 in range(0, numOfStars):
        t9 += '* '

    for row1 in range(0, numOfInverseSpace):
        t9 += '  '

    for row1 in range(0, numOfStars):
        t9 += '* '
    
    t9 += '\n'


print(t9)