# def times2(num) :
#     return num * 2

# listNum = [ 1, 2, 3, 4, 5]
# listNum = list(map(times2, listNum)) #diconvert jadi list dari map object

# print(listNum)


# listNum = [ 1, 2, 3, 4, 5]
# listNum = list(map(lambda z: z * 2 if z <3 else z/2, listNum)) #lambda comprehension baby yeaaah!

# print(listNum)


# def genap(num) :
#     return num % 2 == 0

# listNum = [ 1, 2, 3, 4, 5]
# listNum = list(filter(genap, listNum))

# print(listNum)


# listNum = [ 1, 2, 3, 4, 5]
# listNum = list(filter(lambda num: num % 2 == 0, listNum))

# print(listNum)


# listKata = ['Merdeka','Hello','Hellos','Sohib','Kari ayam']
# print(listKata)

# while(True):
    
#     searchText = input('Text Search: ')
#     # for kataTest in listKata:
#     #     print('{} --> {}'.format(kataTest.lower(), kataTest.lower().index(searchText.lower())))
#     print(list(filter(lambda kata: searchText.lower() in kata.lower(),listKata)))

# listNum = [1,2,3,4,5]

# def filterList(function, listContainer):
#     # filteredList = []
#     # for item in listContainer:
#     #     if function(item):
#     #         filteredList.append(item)
#     # return filteredList
#     return [item for item in listContainer if function(item)]

# print(filterList(lambda num: num%2 == 0, listNum))

# def mapList(function,listContainer):
#     # mappedList = []
#     # for item in listContainer:
#     #     mappedList.append(function(item))
#     # return mappedList
#     return [function(item) for item in listContainer]

# print(mapList(lambda num: num*2, listNum))

# text = 'pok ame ame belalang kupu kupu siang makan nasi kalau malam minum susu'
# splittedText = text.split()
# print(list())


# sum_triangular_numbers(5)

# [1]
# 2 [3]
# 4 5 [6]
# 7 8 9 [10]
# 11 12 13 [14]

# sum of each last part of the triangle is 35

def generateNumbersList(numOfRow):
    zeList = []
    for x in range(numOfRow):
        for y in range(x+1):
            zeList.append()
    return zeList

print(generateNumbersList(5))

# 1,2,4,7,11

# 1+0 = 1
# 1+1 = 2
# 2+2 = 4
# 4+3 = 7