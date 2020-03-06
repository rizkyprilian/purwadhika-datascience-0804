def jalankanTransaksi(antrian):

    # seumpama kasir punya laci uang, anggap aja sebagai list
    uangDiLaci = []
    kembalianAmanBos = True
    noAntrian = 0

    for uang in antrian:
        noAntrian += 1
        #  print('{} mulai --> {}'.format(noAntrian, uangDiLaci))
        if uang == 25:
            # ga usah ada kembalian. jangan lupa kastamer ditawarin pulsa ya
            uangDiLaci.append(25)
        elif uang == 50:
            # kembalian 25 cuy
            if 25 in uangDiLaci:
                uangDiLaci.remove(25)
            else:
                # ga ada uang pas nya aja paak, yaelaaaah
                kembalianAmanBos = False
                break
            uangDiLaci.append(50)
        elif uang == 100:
            # kembaliannya kan 75. 75 itu bisa 50 + 25, atau 25 + 25 + 25
            if 50 in uangDiLaci and 25 in uangDiLaci:
                uangDiLaci.remove(25)
                uangDiLaci.remove(50)
            elif uangDiLaci.count(25) >= 3:
                # ambil 3 25-an di laci
                # .remove itu cuman ngilangin yg pertama ketemu, jadi harus di-loop 3x
                for i in range(3):
                    uangDiLaci.remove(25)
            else:
                # sebenarnya kastamer cuman mau nuker uang buat parkir
                kembalianAmanBos = False
                break
            # ntaaaps, cuaaan booooos
            uangDiLaci.append(100)
        print('{} selesai --> {}'.format(noAntrian, uangDiLaci))
    
    return kembalianAmanBos, noAntrian

antrian1 = [25,25,50,50,25,50,25,25,50,100]
antrian2 = [25,25,50,100,100,25]
antrian3 = [25,50,25,50,25,25,25,100,25,100]

print(jalankanTransaksi(antrian3))

statusCekAntrian1, noAntrian1 = jalankanTransaksi(antrian1)
statusCekAntrian2, noAntrian2 = jalankanTransaksi(antrian2)
statusCekAntrian3, noAntrian3 = jalankanTransaksi(antrian3)
print('tes antrian 1 --> {}. No antrian terakhir {}'.format(statusCekAntrian1, noAntrian1))
print('tes antrian 2 --> {}. No antrian terakhir {}'.format(statusCekAntrian2, noAntrian2))
print('tes antrian 3 --> {}. No antrian terakhir {}'.format(statusCekAntrian3, noAntrian3))
