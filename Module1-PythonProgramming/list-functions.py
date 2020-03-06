# List comprehension
# Looping di dalam list

# # put loop inside list , result > [0,1,2,3,4]
# x = [i for i in range(5)]
# print(x)

# # we can do function or arithmetic operation
# x = [str(i) for i in range(5)]
# print(x)

# # Loop inside loop
# # for i in range(5):
# #   for j in range(2):
# #       return i*j 
# x = [i*j for i in range(5) for j in range(2)]
# print(x)

# # we can even put conditionals. but no elif
# # for i in range(5):
# #   for j in range(2):
# #       if i < 3:
# #           return i*j
# #       else:
# #           return i+j
# x = [i*j if i < 3 or i==4 else i+j for i in range(5) for j in range(2)]
# print(x)

# ---------------
# contoh
# ---------------

buah = ['Jeruk','Nanas','Apel','Mangga','Pir','Kiwi','Semangka']

# for b in buah:
#   if len(b)>4:
#       return b[:2]
#   else:
#       return 'buah lain'

print([b[:2] if len(b)>4 else 'buah lain' for b in buah])

deretAngka = [i for i in range(1, 40)]
deretAngkaGenap = [1 if angka%2 == 0 else 0 for angka in deretAngka]

print(deretAngkaGenap)