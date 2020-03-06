# Rizky Prilian
# JCDS 0804
# Homework5: Dictionary

# buat warnain terminal
txtColorWarning = '\033[93m'
txtColorFail = '\033[91m'
txtColorGreen = '\033[92m'
txtColorBlue = '\033[1m\033[94m'
txtEndColor = '\033[0m'

def getRemainingSeat(reservedSeat):
    allCount = 0
    for row in reservedSeat:
        allCount += len(row)
    return 20 - allCount

# fungsi untuk print 
# 00000000X
# 000000000
def displayReservedSeat(reservedSeat):
    z = '\n'
    for row in reservedSeat:
        for seat in range(10):
            if seat in row:
                z += txtColorWarning + 'X' + txtEndColor
            else:
                z += txtColorGreen + '0' + txtEndColor
        z += '\n'
    
    z += txtColorWarning + 'X' + txtEndColor + ': Reserved. ' + txtColorGreen + '0' + txtEndColor + ': Available. \n'
    z += 'Remaining Seat Available: ' + str(getRemainingSeat(reservedSeat)) + '\n'
    return z

def displayMenuFromList(menuList, judulMenu = ''):
    z = ''

    if len(judulMenu) > 0:
        z += '-----------\n'
        z += judulMenu + '\n'
        z += '-----------\n'

    for index,judul in enumerate(menuList):
        z += '{}. {}'.format(index+1, str(judul).capitalize())
        z += '\n'
    return z


# Validate user input
def validateIntegerOnly(inputCommand, min = None, max = None):
    try:
        validatedInput = int(inputCommand)
    except:
        raise ValueError('Value must be integer')
    if min is not None and validatedInput < min:
        raise ValueError('Value cannot be less than ' + str(min) )
    if max is not None and validatedInput > max:
        raise ValueError('Value cannot be more than ' + str(max))
    return validatedInput

def validateInputFromMenuList(inputCommand, menuList):
    # input must be integer
    try:
        validatedInput = validateIntegerOnly(inputCommand, 1, len(menuList))
    except:
        raise
    try:
        menuList[validatedInput-1]
        return validatedInput
    except:
        raise IndexError('Not available')

def validateIfSeatAvailable(reservedSeat, row, seat):
    if seat-1 in reservedSeat[row-1] or len(reservedSeat[row-1]) >= 10:
        return False
    else:
        return True


shows = [
    {
        'judul': 'The Incredibles',
        'reservasi': {
            'siang': [[],[]],
            'malam': [[],[]]
        }
    },
    {
        'judul': 'Toy Story',
        'reservasi': {
            'siang': [[],[]],
            'malam': [[],[]]
        }
    }
]


menuUtama = ['pesan tiket', 'lihat histori reservasi', 'keluar']
menuJudulFilm = [film['judul'] for film in shows]
menuJadwal = ['siang', 'malam']
reservationHistory = []

while(True):
    
    print(displayMenuFromList(menuUtama))

    try:
        inputCommand = validateInputFromMenuList(input(txtColorBlue + 'Pilih : ' + txtEndColor), menuUtama)
    except Exception as e:
        print(txtColorFail + str(e) + txtEndColor)
        continue

    if inputCommand == 1:
        
        # question: pass vs break
        # bisa ga pass vs break itu ada di function berbeda
        # best practice nya buat handling input kaya gimana?
        # python tuh boleh ya buat variable ga di declare dulu?
        # 

        while(True):
            print(displayMenuFromList(menuJudulFilm, 'Pertunjukkan Hari Ini: '))
            try:
                inputCommand = validateInputFromMenuList(input(txtColorBlue + 'Pilih : ' + txtEndColor), menuJudulFilm)
                break
            except Exception as e:
                print(txtColorFail + str(e) + txtEndColor)
                continue

        selectedShowIdx = inputCommand - 1
        selectedShow = shows[selectedShowIdx]

        while(True):
            print(displayMenuFromList(menuJadwal, 'Pilih Jadwal'))
            try:
                inputCommand = validateInputFromMenuList(input(txtColorBlue + 'Pilih : ' + txtEndColor), menuJadwal)
                break
            except Exception as e:
                print(txtColorFail + str(e) + txtEndColor)
                continue

        selectedSchedule = menuJadwal[inputCommand-1]
        # 1 --> siang
        # 2 --> malam

        numOfRemainingSeat = getRemainingSeat(selectedShow['reservasi'][selectedSchedule])

        if numOfRemainingSeat <= 0:
            print(txtColorFail + 'Studio sudah terisi penuh.' + txtEndColor)
            continue # to main menu
        else:
            requestedSeatNumber =  validateIntegerOnly(input(txtColorBlue + 'Jumlah kursi yang ingin dipesan maks. '+ str(numOfRemainingSeat) +' : ' + txtEndColor), 1, numOfRemainingSeat) 
        
        for order in range(requestedSeatNumber):
            while(True):
                print(displayReservedSeat(selectedShow['reservasi'][selectedSchedule]))
                try:
                    rowSelection = validateIntegerOnly(input(txtColorBlue + 'Pilih Row : ' + txtEndColor), 1, 2)
                    seatSelection = validateIntegerOnly(input(txtColorBlue + 'Pilih Seat : ' + txtEndColor), 1, 10)
                    pass
                except Exception as e:
                    print(txtColorFail + str(e) + txtEndColor)
                    continue

                # check if seat available?
                if validateIfSeatAvailable(selectedShow['reservasi'][selectedSchedule], rowSelection, seatSelection):
                    break
                else:
                    print(txtColorFail + 'Kursi yang anda pilih tidak tersedia' + txtEndColor)
                    continue
            
            # add to reservation list
            selectedShow['reservasi'][selectedSchedule][rowSelection-1].append(seatSelection-1)
            # shows[selectedShowIdx] = selectedShow

            print(shows)
            print(displayReservedSeat(selectedShow['reservasi'][selectedSchedule]))
            # print selected reservation
            print('Reservasi untuk Film {}, jadwal {}, Row/Seat: {}/{}, Berhasil!'.format(selectedShow['judul'], selectedSchedule, rowSelection, seatSelection))

            print()
            # add to history list
            reservationHistory.append('Film {}, jadwal {}, Row/Seat: {}/{}'.format(selectedShow['judul'], selectedSchedule, rowSelection, seatSelection))

        print('Terima kasih. Selamat menikmati film nya.\n')

    elif inputCommand == 2:
        print()
        if len(reservationHistory) > 0:
            for history in reservationHistory:
                print(history)
        else:
            print('Belum ada reservasi')
        (print)
        continue
    elif inputCommand == 3:
        print('Terima kasih')
        break # from main menu