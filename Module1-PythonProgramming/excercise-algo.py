
def prependList(item, _list):
    newList = []
    newList.append(item)
    newList += _list
    return newList

def moveZeros(_list):
    allTheZeros = []
    newList = []
    for angka in _list:
        if str(angka) == '0':
            allTheZeros.append(angka)
        else:
            newList.append(angka)

    return newList + allTheZeros




testLists = [
    [False,1,0,1,2,0,1,3,"a"],
    [0,0,0,"Test",0,3,"a",True],
    [True,True,False,"a","b",1,1,1]
]

for testList in testLists:
    print('original list --> {}'.format(testList))
    print('modified list --> {}'.format(moveZeros(testList)))
    print('--------\n')
