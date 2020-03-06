# ---------------------------
print('\n####################\n')
# ---------------------------


x = 5
y = '5'

print(x == y) # false
print(x > int(y)) # false
print(x >= int(y)) # true
print(x < int(y)) # false
print(x <= int(y)) # true

# ---------------------------
print('\n####################\n')
# ---------------------------


x = 5
y = '5'
z = 6

print(x==int(y) and int(y)<z)
print(x==int(y) or int(y)<z)
print(not(x==int(y) or int(y)<z))