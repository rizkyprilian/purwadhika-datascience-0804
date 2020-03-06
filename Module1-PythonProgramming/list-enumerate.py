buah = ['Jeruk','Mangga','Pisang']

# APAPUN YANG BISA DIAMBIL INDEX NYA BERARTI ITERABLE a.k.a BISA DI LOOPING
# string juga bisa di-looping

# kalau mau looping dan kita pengen tahu index dan valuenya secara bersamaan
for index, value in enumerate(buah):
    # print(index)
    # print(value)
    print('{}. {}'.format(index+1, value))


# ZIP untuk looping dua iterable secara bersamaan, dan hasilnya jadi tuple
# kalau jumlah item dalam list berbeda, dia akan berhenti di index list yang lebih kecil

cars = ['BMW','Honda', 'Isuzu', 'Ford', 'Chevrolet']
motorcycles = ['Suzuki', 'Honda', 'BMW', 'Yamaha']

for car,motorcycle in zip(cars, motorcycles):
    print(car + ' ' +motorcycle)
