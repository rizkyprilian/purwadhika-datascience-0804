# # function is a block of reusable code

# # def funcname(param)
# def contoh(teks):
#     print(str(teks.split()))

# contoh('baa baa black sheep have you any wool?')

# # -------------

# def addNum(x,y):
#     print(x+y)

# addNum(10,5)

# # -------------

# def printNum(num1,num2):
#     print(num1, num2)

# printNum(num2 = 8, num1=1)

# -------------

# def printNama(umur, nama):
#     print(nama + ' Handoko. umur '+str(umur))

# a = ['Budi', 'Caca', 'Dedi', '']

# for nama in a:
#     printNama(umur=len(nama), nama=nama)

# --------------

# def total(x,y):
#     return x+y

# print(total(10,9))

# --------------

# def tambah(x,y):
#     return x+y

# def kali(x,y):
#     return x*y

# def bagi(x,y):
#     if (not(y == 0)):
#         return x/y
#     else:
#         return 'ga boleh dibagi 0 laaaaah'

# def latihan(x,y,operasi):
#     if operasi == 'tambah':
#         return tambah(x,y)
#     elif operasi == 'kali':
#         return kali(x,y)
#     elif operasi == 'bagi':
#         return bagi(x,y)
#     else:
#         return 'karepmu!'

# print(latihan(5,6,'tambah'))
# print(latihan(5,6,'kali'))
# print(latihan(y=5,x=6,operasi='bagi'))
# print(latihan(y=0,x=6,operasi='bagi'))
# print(latihan(5,6,'bzbzbzbzbzbz'))

# list

mobil = ['Apanja','Xenia','Kolbak', 12, 'Kawasaki']
motor = ['SupraFit','Kawasaki','Vespa']

print(mobil[0:2])
print(mobil[1][0])
print(mobil[2])

print(mobil[::-1]) # reverse the list

print(mobil+motor)

mobil.append('Carry')

mobil.append(motor)


print(mobil)

mainMenu = ['1','2']

mainMenu[5]