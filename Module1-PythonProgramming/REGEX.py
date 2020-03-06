import re

# regular expression

# search
# findall
# sub
# split
# compile

months = ['January', 'February', 'March', 'April', 'May', 'June']

# .search untuk mencari match regex di string 
# for month in months:
#     if re.search(r'a', month):
#         print(month)

# metacharacters
# -----------------

# ^ untuk cek kalau string nya diawali dengan kata atau huruf
# hellos = ['hello', 'world', 'hello world', 'world hello', 'hmiaow']
# for hello in hellos:
#     if re.search(r'^hello', hello):
#         print(hello)

# $ untuk cek kalau stringnya diakhiri dengan kata atau huruf sebelumnya
# hellos = ['hello', 'world', 'hello world', 'helloworld', '1helloworld', 'serviced']
# for hello in hellos:
#     if re.search(r'world$', hello):
#         print(hello)

# findall hasilnya list yang matches
# strings = 'February March April May June 123'
# match = re.findall(r'[a-zA-Z]+', strings)
# print(match)

# # [^] ^ di dalam set jadi inversenya
# match = re.findall(r'[^a-zA-Z]+', strings)
# print(match)

# word = '25.5 usd'
# match = re.findall(r'[a-zA-Z]+|\d+\.\d+', word)
# print(match)


word = 'Cat Dog kamper cat+spambox@gmail.co.id monkeyeye rizky_09@purwadhika.com dishwasher bobby@abcde.com kasses@yahoo.com sup rarara@google.com'

# valid email address may contains alphanumerics and specialchars: . _ + -
# domain name might contains -
regexEmail = re.compile(r'[a-z\d\.-_\+]+@[a-z\d\.-]+', flags = re.IGNORECASE)

def find_email(txt):
    return regexEmail.findall(txt)

for email in find_email(word):
    print(email)