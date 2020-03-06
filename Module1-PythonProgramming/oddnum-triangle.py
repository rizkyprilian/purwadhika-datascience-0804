

# Given the triangle of consecutive odd numbers:
# Calculate the row sums of this triangle from the row index (starting at index 1)
# Print the triangle as well

# listContainer = []
# for idx, angkaAwal in enumerate(listAngkaAwal):
#     listTemp = []
#     for y in range(idx+1):
#         listTemp.append((y*2) + angkaAwal)
#     listContainer.append(listTemp)
# -- above code in list comprehension version
# -- it's hard to read though :))
generateOddSequence = lambda n :  [ [y*2 + a for y in range(i+1)] for i,a in enumerate([x*(x-1)+1 for x in range(1,n+1)])]

def printTriangleFromSequence(sequence):
    z = ''
    for idx,row in enumerate(sequence):
        numOfSpace = (-1*idx)+len(sequence)
        # just to tweak the spacing because row no 3 and above has two digits number
        if idx < 3:
            numOfSpace += 2
        z += numOfSpace*' '
        for num in row:
            z += str(num).ljust(4,' ')
            # ljust itu cara kerjanya sama kaya gini:
            # z += ' '*(4- len(str(num))) 
        z += '\n'
    return z

def reduceSum(nums):
    total = 0
    for item in nums:
        total += item
    return total

# todo: validate the rowNumber (check for IndexError)
def getSumOfRow(rowNumber,sequence):
    return sum(sequence[rowNumber-1])

# sum itu sama kaya reduceSum

# print(generateOddSequence(5))
oddSequence1 = generateOddSequence(10)
print(oddSequence1)
print(printTriangleFromSequence(oddSequence1))
print('Sum of row 2 is {}'.format(getSumOfRow(2,oddSequence1)))
print('Sum of row 3 is {}'.format(getSumOfRow(3,oddSequence1)))
print('Sum of row 4 is {}'.format(getSumOfRow(4,oddSequence1)))
