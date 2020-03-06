import random

# Rizky Prilian
# JCDS0804

# kalau uangnya < 10000
    # sangat buruk - buruk - biasa 80%
    # baik 10%
    # sangat baik 10%

# kalau uangnya 10000 - 500000
    # sangat buruk 10%
    # buruk biasa baik 80%
    # sangat baik 10%

# kalau uangnya > 50000
    # sangat buruk 10%
    # buruk 10%
    # biasa baik sangatbaik 80%

# kategori ramalan kita simpan dalam skor ya

class ramal:
    def __init__(self, uang):
        self.uang = uang
        # sangat buruk = 0 ..... sangat baik = 4
        self.ramalan = {
            'asmara': {
                'template': 'Ramalan asmara anda bulan ini: {}',
                'ramalan': ['Ga ada harapan', 'Ditolak lagi sih pasti' ,'Awas tikungan tajam didepan', 'Bisa lah asal kuat modal aja', 'Wew, Kejutan dari pasangan nih']
            },
            'keuangan': {
                'template': 'Ramalan keuangan anda bulan ini: {}',
                'ramalan': ['Sekarat, Besok Bangkrut', 'Sengsara tak berujung', 'Belum ada pemasukan, lebaran masih lama', 'Waspada Debt Collector' ,'Menang undian Luwak White Coffee!']
            }
        }

    def print_menu(self):
        print('Menu Ramalan:')
        print('--------------')
        for i, menu in enumerate(self.ramalan):
            print('{}. Ramalan {}'.format(i+1, menu.capitalize()))
        print()

    def menu_input(self):
        self.print_menu()

        pilihanMenu = [menu for menu in self.ramalan]
        while(True):
            try:
                choice = int(input('Pilih menu: '))
                self.lihat_ramalan(pilihanMenu[choice-1])
                break
            except IndexError:
                print('Menu tidak tersedia')
                continue
            except ValueError:
                print('Invalid input')
                continue


    def decide_ramalan(self):
        listProb = [0,1,2,3,4]
        if self.uang < 10000:
            listProb = [random.randint(0,2) for i in range(8)] + [random.randint(3,4) for i in range(2)] 
        elif self.uang >= 10000 and self.uang < 50000:
            listProb = [random.randint(1,3) for i in range(8)] + [0 if random.randint(0,1) == 0 else 4 for i in range(2)]
        else:
            listProb = [random.randint(0,1) for i in range (2)] + [random.randint(2,4) for i in range(8)]

        print(listProb)
        return listProb[random.randint(0,len(listProb)-1)]

    def lihat_ramalan(self, pilihanMenu = 'asmara'):
        try:
            print(self.ramalan[pilihanMenu.lower()]['template'].format(self.ramalan[pilihanMenu.lower()]['ramalan'][self.decide_ramalan()]))
        except IndexError:
            print('Pilihan tidak tersedia')
        # print(self.ramalan[self.decide_ramalan()])

test = ramal(20000)

test.menu_input()
