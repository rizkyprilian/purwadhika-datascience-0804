# class adalah blue print yang bisa diinisiasi menjadi object baru

# gimana cara bikin default parameter?
# kenapa sama aja child init sama super??
# mau manggil fungsi yang sama dalam satu kelas harus pake self juga?

class hewan:
    def __init__(self, name, bunyi):
        self.name = name
        self.bunyi = bunyi

    def doSomething(self):
        self.keluarinBunyi()

    def keluarinBunyi(self):
        print(self.bunyi)

kucing = hewan('kocheng oren', 'meong')
# print(kucing.doSomething())
# # print(kucing)
# # print(kucing.name)
# # print(kucing.bunyi)
# kucing.umur = 4

# # hanya di dalam self
# # print(kucing.__dict__)
# # kucing.keluarinBunyi()

# tikus = hewan('mickey mouse', 'cit cit')
# # print(tikus.__dict__)

# # child class
# class Aves(hewan):
#     def __init__(self, name, bunyi, telur = 'besar'):
#         # saat child class punya init sendiri, init fn nya bakal override parent class nya
#         # kalau mau inherit parent init fn nya, panggil lagi parent init nya di init child nya
#         hewan.__init__(self, name, bunyi)

#         # gunakan super saat mau inherit semua methodnya juga
#         # super().__init__(name,bunyi)
#         self.telur = telur


# ayam = Aves('CikCik', 'pyak-pyak')
# # print(ayam.__dict__)
# # ayam.keluarinBunyi()


class BikinMenu:
    def __init__(self, namaPelanggan, menuList, hargaList):
        self.namaPelanggan = namaPelanggan
        self.menuList = menuList
        self.hargaList = hargaList
        self.history = []
    
    def get_menu(self):
        for idx, menu, harga in list(zip(range(len(self.menuList)), self.menuList, self.hargaList)):
            print('{}. {} harganya adalah {}'.format(idx+1, menu, harga))

    def menu_price(self):
        menuInput = int(input('Mau beli yang mana: '))
        menuChosen = list(zip(self.menuList, self.hargaList))[menuInput-1]
        foodPilih, pricePilih = menuChosen
        print('{} telah membeli {} dengan harga {}'.format(self.namaPelanggan, foodPilih, pricePilih))
        self.history.append(menuChosen)

    def print_list_history(self):
        list_buy = [item for item, harga in self.history]
        z = ''
        for i, item in enumerate(list_buy):
            z += item
            if i == (len(list_buy) - 2): # ambil item sebelum yg terakhir
                z += ' dan '
            elif i != (len(list_buy) - 1): # semua tambah , kecuali item paling akhir
                z += ', '
        return z

    def get_history(self):
        if len(self.history) > 1:
            print('{} telah membeli {}'.format(self.namaPelanggan, self.print_list_history()))
        else:
            print('{} telah membeli {} dengan harga {}'.format(self.namaPelanggan, self.history[0][0], self.history[0][1]))


Paul = BikinMenu('Paul',['Ayam Goreng', 'Nasi Bakar', 'Sate Kambing'], [1000,2000,3000])

Paul.get_menu()
Paul.menu_price()
Paul.menu_price()
Paul.menu_price()
Paul.menu_price()
Paul.menu_price()
Paul.get_history()