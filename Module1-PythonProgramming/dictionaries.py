# nama index di dictionary adalah key nya (kalau di list itu index)
# urutan pengisian dictionary adalah key:value

d = { 
    "key1" : "item1", 
    "key2" : None,
    "kucing" : [3, "jerapah"] 
    }

d['kuda'] = 'hiiiiii'
d['ikan'] = 'blub blub'
d['ikan'] = 'Blubub'

# buat hapus key
del d['ikan']

print(d["key1"])
print(d["key2"])
print(d["kucing"])
print(d["kucing"][1])

print()

# mau lihat semua indexnya, kita bisa loop
for key in d:
    print(key)

# atau pake dictionary.keys
print(d.keys())

print()
# kalau kita mau ngecek ada ga suatu key dalam dictionary
print('kucing' in list(d.keys()))
print('anjing' in list(d.keys()))

print()
# kalau kita pengen dapet list dari values nya
print(list(d.values()))

print()
# bisa juga bikin list tuple dari setiap item di dictionaries
for key,val in d.items():
    print(key)
    print(val)

# dictionary comprehension
# fruits = ['Mangga', 'Pisang', 'Jambu']
# vegetables = ['Wortel','Kol','PakChoy']

# fruveg = {key:value for }