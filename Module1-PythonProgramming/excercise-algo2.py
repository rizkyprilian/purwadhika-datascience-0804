# def reverseText(text):
#     return text[::-1]

reverseText = lambda text : text[::-1]

def spinWords(string):
    splitString = [reverseText(word) if len(word) >= 5 else word for word in string.split()]
    


    z = ''
    if (len(splitString) > 0):
        for i, word in enumerate(splitString):
            z += word
            # z += ' '

            if i < len(splitString)-1:
                z += ' '
    else:
        z = splitString[0]
    
    return z

testWords = [
    'Hey fellow warriors',
    'This is a test',
    'This is another test'
]

for test in testWords:
    print(spinWords(test))

print(str(False) == 0)


print('asdsa asdasdas asdasd'.upper())

print(str.upper('asdsa asdasdas asdasd'))
print(str.join(' ', ['this','is','spartaaaa']))