import math

# buat warnain terminal
txtColorWarning = '\033[93m'
txtColorFail = '\033[91m'
txtColorGreen = '\033[92m'
txtColorBlue = '\033[94m'
txtEndColor = '\033[0m'

def generateSequenceListOnList(x):
    number = []
    for i in range(x):
        insideList = []
        for j in range(x):
            insideList.append((j+1) + (i*x))
        number.append(insideList)
    return number

def displayMainMenu(menuList):
    z = '\n --------------------- \nMenu: \n --------------------- \n'
    for i in range(len(menuList)):
        z += '{}. {}'.format(i+1, menuList[i])
        z += '\n'
    z += '--------------------- \n'
    return z

def prettyPrint(matrix):
    z = '\n'
    for insideList in matrix:
        for angka in insideList:
            z += str(angka)
            z += ' '
        z += '\n'
    print(txtColorGreen + z + txtEndColor)


def rotateMatrixKananV2(matrix):
    listKanan = []
    for i in range(len(matrix)):
        listTemp = []
        for j in range((len(matrix)-1),-1,-1):
            listTemp.append(matrix[j][i])
        listKanan.append(listTemp)
    return listKanan

def rotateMatrixKiriV2(matrix):
    listKiri = []
    for i in range((len(matrix)-1),-1,-1):
        listTemp = []
        for j in range(len(matrix)):
            listTemp.append(matrix[j][i])
        listKiri.append(listTemp)
    return listKiri

# hanya bisa kalau matrixSize nya genap
def rotateMatrixKiri(matrixSize,matrix):
    
    # dihitung dari layer kotak paling luar sampai unit kotak paling kecil
    # matrix 6x6 itu ada tiga kali perpindahan
    # matrix 4x4 itu ada dua kali perpindahan 
    # kotak bagian luar dan kotak bagian dalam
    for x in range(0, int(math.floor(matrixSize/2))): 
          
        # ada 3x perpindahan angka dalam matrix 4x4
        for y in range(x, matrixSize-1-x): 
              
            # simpen ujung kiri atas, karena akan di overwrite sama angka lain
            ujungKiriAtas = matrix[x][y] 
  
            # pindahin ujung kanan atas ke ujung kiri atas
            matrix[x][y] = matrix[y][matrixSize-1-x] 
  
            # pindahin ujung kanan bawah ke ujung kanan atas
            matrix[y][matrixSize-1-x] = matrix[matrixSize-1-x][matrixSize-1-y] 
  
            # pindahin ujung kiri bawah ke ujung kanan bawah 
            matrix[matrixSize-1-x][matrixSize-1-y] = matrix[matrixSize-1-y][x] 
  
            # yang tadinya ujung kiri atas jadi ujung kiri bawah 
            matrix[matrixSize-1-y][x] = ujungKiriAtas
    return matrix

# hanya bisa kalau matrixSize nya genap
def rotateMatrixKanan(matrixSize,matrix):
    
    # dihitung dari layer kotak paling luar sampai unit kotak paling kecil
    # matrix 6x6 itu ada tiga kali perpindahan
    # matrix 4x4 itu ada dua kali perpindahan 
    # kotak bagian luar dan kotak bagian dalam
    for x in range(0, int(math.floor(matrixSize/2))): 

        #  x = 0

        # ada 3x perpindahan angka dalam matrix 4x4
        for y in range(x, matrixSize-1-x): 
              
            # simpen ujung kanan atas, karena akan di overwrite sama angka lain. ok
            ujungKananAtas = matrix[y][matrixSize-1-x] 
  
            # pindahin ujung kiri atas ke ujung kanan atas
            matrix[y][matrixSize-1-x] = matrix[x][y]

            # pindahin ujung kiri bawah ke ujung kiri atas
            matrix[x][y] = matrix[matrixSize-1-y][x]

            # pindahin ujung kanan bawah ke ujung kiri bawah
            matrix[matrixSize-1-y][x] = matrix[matrixSize-1-x][matrixSize-1-y]

            # yang tadinya ujung kanan atas jadi ujung kanan bawah. ok
            matrix[matrixSize-1-x][matrixSize-1-y] = ujungKananAtas

    return matrix

# 4x4 matrix
# matrixNum = [ [1,2,3,4],
#               [5,6,7,8],
#               [9,1,2,3],
#               [4,5,6,7] ]

matrixNum = generateSequenceListOnList(4)

menuList = ['Rotate Kanan', 'Rotate Kiri', 'Keluar']

while (True):

    prettyPrint(matrixNum)

    # print menu
    print(displayMainMenu(menuList))

    try:
        inputCommand = int(input(txtColorBlue + 'Pilih Menu: ' + txtEndColor))
        menuList[inputCommand-1]
    except IndexError:
        print()
        print(txtColorFail + 'Menu yang anda pilih tidak tersedia' + txtEndColor)
        print()
        continue
    except ValueError:
        print()
        print(txtColorFail + 'Menu Hanya Boleh Angka' + txtEndColor)
        print()
        continue


    if inputCommand == 1:
        rotateIteration = int(input('Berapa kali rotasi? '))
        for w in range(rotateIteration):
            rotateMatrixKanan(4,matrixNum)
        continue
    elif inputCommand == 2:
        rotateIteration = int(input('Berapa kali rotasi? '))
        for w in range(rotateIteration):
            rotateMatrixKiri(4,matrixNum)
        continue
    elif inputCommand == 3:
        print('Goodbye!')
        break





# prettyPrint(4, matrixNum)
# print()
# prettyPrint(4,rotateMatrixKanan(4, matrixNum))

matrix1 = [1,2,3,4]
matrix2 = [3,4,5,6]
matrix3 = [7,8,9,1]



