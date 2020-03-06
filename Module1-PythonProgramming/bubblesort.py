def bubbleSort(inputList, order='asc'): 
    # print('original list: {}'.format(inputList))
    listLength = len(inputList)
    # iterate sebanyak jumlah list
    for i in range(listLength):
        # print('i : {}'.format(i))
        for j in range(0, listLength-i-1):
            # print('j : {}'.format(j))
            # print('inputList[{}]:{} > inputList[{}]:{}. >> {}'.format(j,inputList[j],j+1,inputList[j+1], inputList[j] < inputList[j+1]))
            if order == 'asc':
                # ascending order
                # Tuker kalau angka sebelah kanan nya (j+1) lebih besar dari angka sebelumnya
                if inputList[j] > inputList[j+1] :
                    inputList[j], inputList[j+1] = inputList[j+1], inputList[j]
            else:
                # descending order
                # Tuker kalau angka sebelah kanan nya (j+1) lebih kecil dari angka sebelumnya
                if inputList[j] < inputList[j+1] :
                    inputList[j], inputList[j+1] = inputList[j+1], inputList[j]
        # print('end iteration')
    return inputList

def findMaxMin(inputList):
    maxValue = inputList[0] #assume first
    minValue = inputList[0]
    for i in inputList:
        if i > maxValue:
            maxValue = i
        elif i < minValue:
            minValue = i
    return maxValue, minValue


inputList = [1,676,4,77,23,545]
print(bubbleSort(inputList, 'asc'))

maxValue, minValue = findMaxMin(inputList)
print(maxValue)
print(minValue)
