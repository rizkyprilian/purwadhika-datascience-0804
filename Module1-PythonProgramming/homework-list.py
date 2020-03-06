# Nama: Rizky Prilian
# Kelas: JCDS0804
# Modul 1 Python
# Tanggal 2020/02/23

# -------
# Assignment: Buat list menu seperti dibawah
# -------
# 1. isi list
# 2. lihat list
# 3. Sort list ascending (def)
# 4. sort list descending (def)
# 5. Dapatkan nilai tertinggi dan terendah (def)
# 6. jumlah ganjil dan genap (def)
# 7. keluar

# buat warnain terminal
txtColorWarning = '\033[93m'
txtColorFail = '\033[91m'
txtColorGreen = '\033[92m'
txtColorBlue = '\033[94m'
txtEndColor = '\033[0m' 

def displayMainMenu(menuList):
    z = '\n --------------------- \nMenu: \n --------------------- \n'
    for menuIndex in range(len(menuList)):
        z += '{}. {}'.format(menuIndex+1, menuList[menuIndex])
        z += '\n'
    z += '--------------------- \n'
    return z

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

def countEvenOdd(inputList):
    evenCount = 0
    oddCount = 0

    for i in inputList:
        if (i%2 == 0):
            evenCount += 1
        else:
            oddCount += 1
    
    return evenCount, oddCount

# initial vars
mainMenu = ['Isi List', 'Lihat List', 'Sort List Asc', 'Sort List Desc', 'Dapatkan Nilai Tertinggi dan Terendah', 'Jumlah Ganjil dan Genap', 'Keluar']
inputList = []

# main routine
while(True):
    
    # display Menu
    print(displayMainMenu(mainMenu))

    inputCommand = input(txtColorBlue + 'Pilih Menu: ' + txtEndColor)

    try:
        inputCommand = int(inputCommand)
    except:
        print()
        print(txtColorFail + 'Menu yang anda pilih tidak tersedia (hanya dalam angka)' + txtEndColor)
        print()
        continue

    try:
        mainMenu[inputCommand-1]
    except IndexError:
        print()
        print(txtColorFail + 'Menu yang anda pilih tidak tersedia' + txtEndColor)
        print()
        continue

    # menu selection

    # Isi List
    if inputCommand == 1:

        while(True):
            print()
            newItem = input('Masukkan angka ke dalam list (# untuk mengakhiri input): ')

            # exit input loop
            if newItem == '#':
                break

            try:
                newItem = int(newItem)
            except:
                print()
                print(txtColorFail + 'Invalid Input!' + txtEndColor)
                continue
            
            # append new item into list
            inputList.append(newItem)

        continue #continue main loop

    # Lihat List
    elif inputCommand == 2:
        print('\n >>>> {} \n'.format(inputList))
        continue

    # sort asc
    elif inputCommand == 3:
        if len(inputList) < 1:
            print(txtColorWarning + 'List is empty!' + txtEndColor)
            continue

        inputList = bubbleSort(inputList, 'asc')
        print('\n >>>> {} \n'.format(inputList))
        continue

    # sort desc
    elif inputCommand == 4:
        if len(inputList) < 1:
            print(txtColorWarning + 'List is empty!' + txtEndColor)
            continue
        
        inputList = bubbleSort(inputList, 'desc')
        print('\n >>>> {} \n'.format(inputList))
        continue

    # find max and min in the list
    elif inputCommand == 5:
        if len(inputList) < 1:
            print(txtColorWarning + 'List is empty!' + txtEndColor)
            continue
        
        maxValue, minValue = findMaxMin(inputList)
        print('\n >>> max: {}, min: {}'.format(maxValue, minValue))
        continue

    # count even and odd number
    elif inputCommand == 6:
        if len(inputList) < 1:
            print(txtColorWarning + 'List is empty!' + txtEndColor)
            continue
        
        evenCount, oddCount = countEvenOdd(inputList)
        print('\n >>> jumlah angka genap: {}, jumlah angka ganjil: {}'.format(evenCount, oddCount))
        continue

    elif inputCommand == 7:
        break
        

