inputNums = input('Masukkan angka: ')

def renderLine(text):
    return text.replace('0', ' ').replace('1', '|').replace('2', '__')

def printSevenSegment(num):
    rowAtas = ''
    rowTengah = ''
    rowBawah = ''

    if num == 0:
        rowAtas = '020'
        rowTengah = '1001'
        rowBawah = '121'
    elif num == 1:
        rowAtas = '0000'
        rowTengah = '0001'
        rowBawah = '0001'
    elif num == 2:
        rowAtas = '020'
        rowTengah = '021'
        rowBawah = '120'
    elif num == 3:
        rowAtas = '020'
        rowTengah = '021'
        rowBawah = '021'
    elif num == 4:
        rowAtas = '0000'
        rowTengah = '121'
        rowBawah = '0001'
    elif num == 5:
        rowAtas = '020'
        rowTengah = '120'
        rowBawah = '021'
    elif num == 6:
        rowAtas = '020'
        rowTengah = '120'
        rowBawah = '121'
    elif num == 7:
        rowAtas = '020'
        rowTengah = '0001'
        rowBawah = '0001'
    elif num == 8:
        rowAtas = '020'
        rowTengah = '121'
        rowBawah = '121'
    elif num == 9:
        rowAtas = '020'
        rowTengah = '121'
        rowBawah = '021'
    return rowAtas, rowTengah, rowBawah

listNums = [int(i) for i in inputNums.split(' ')]

listRowAtas = [printSevenSegment(i)[0] for i in listNums]
listRowTengah = [printSevenSegment(i)[1] for i in listNums]
listRowBawah = [printSevenSegment(i)[2] for i in listNums]

print(renderLine(' '.join(listRowAtas)))
print(renderLine(' '.join(listRowTengah)))
print(renderLine(' '.join(listRowBawah)))

# print(' '.join(listRowAtas))
# print(' '.join(listRowTengah))
# print(' '.join(listRowBawah))


# txtRowAtas = ''
# txtRowTengah = ''
# txtRowBawah = ''

# for angkaInput in listNums:
#     rowAtas, rowTengah, rowBawah = printSevenSegment(angkaInput)
#     txtRowAtas += rowAtas + ' '
#     txtRowTengah += rowTengah + ' '
#     txtRowBawah += rowBawah + ' '

# print(renderLine(txtRowAtas))
# print(renderLine(txtRowTengah))
# print(renderLine(txtRowBawah))