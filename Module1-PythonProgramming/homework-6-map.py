# sum_triangular_numbers(5)

# [1]
# 2 [3]
# 4 5 [6]
# 7 8 9 [10]
# 11 12 13 14 [15]

# the beginning of each row has a pattern
#          1,2,4,7,11 
# selisih   1 2 3 4
# selisih    1 1 1
# ---> quadratic pattern!
# rumus dapetin angka ke-n : 1/2n**2 + 1/2n + 1
# @youtube watch?v=vYFz8Qf7h6A
# (n**2-n)/2+1
# ((n*(n-1))/2)+1

def generateNumbersList(numOfRow):
    listContainer = []
    for x in range(1,numOfRow+1):
        list_temp = []
        for i in range(x):
            list_temp.append(int((x*(x-1)/2) + 1)+i)
        listContainer.append(list_temp)
    return listContainer

def printTriangle(numList):
    z = ''
    for row in numList:
        for idx, number in enumerate(row):
            if idx == len(row) - 1:
                z += f'[{number}]'
            else:
                z += f'{number} '
        z += '\n'
    return z

def reduceSum(nums):
    total = 0
    for item in nums:
        total += item
    return total

def sum_triangular_numbers(numOfRow):
    numList = generateNumbersList(numOfRow)
    print(numList)
    print(printTriangle(numList))
    print()
    print('sum of each last part of the triangle is {}'.format(reduceSum(list(map(lambda x: x[-1], numList)))))

sum_triangular_numbers(5)

# .copy() untuk duplikat list dan tidak berhubungan