
inputTxt = input('Masukkan kalimat: ')
dictWords = {}

# dictWords.keys() ---> ['Saya','Kamu']
# dict_keys()

listWords = [word.capitalize() for word in inputTxt.split(' ')]

print(listWords)

for word in listWords:
    # print(dictWords.keys())

    # if dictWords[word] == word

    if word in dictWords.keys():
        dictWords[word] += 1
    else:
        dictWords[word] = 1

        # dictWords['Saya'] = 1

# print(dictWords)
# print(dictWords.items())

for kata, jumlah in dictWords.items():
    print('Kata {} ada sebanyak {} buah'.format(kata, jumlah))