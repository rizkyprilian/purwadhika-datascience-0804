
def generateSequenceListOnList1(x):
    number = []
    for i in range(x):
        insideList = []
        for j in range(x):
            insideList.append((j+1) + (i*x))
        number.append(insideList)
    return number

print(generateSequenceListOnList1(4))


