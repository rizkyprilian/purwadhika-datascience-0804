# Tuples tipe data 

t = (1, [0, "test"], { "a1" : True })

print(t[2]["a1"])
print(t[1][1])
t[1][1] = "akan"
print(t[1][1])
t[1] = "mark"
print(t[1])