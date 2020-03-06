
# Set adalah tipe data mirip list
# tapi semua item di dalamnya unique

# True itu dianggapnya 1
# False itu dianggapnya 0

s = { 1, 3, 1, 2, 2, 3, True, False }
print(s)

# Set ga punya index, kalau mau tarik indexnya, diconvert dulu jadi list
print(list(s)[2])



newList = [ 1, 3, "test1", "test2" , 2, 3, "test1" ]
s = set(newList)
print(s)
print(list(s)[3])