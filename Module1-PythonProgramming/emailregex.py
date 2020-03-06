import re

word = 'Cat Dog kamper cat.me+spambox_@gmail.co.id monkeyeye rizky_09@purwadhika.com dishwasher bobby@abcde.com kasses@yahoo.com sup rarara.099@gmail.com'

# valid email address may contains alphanumerics and specialchars: . _ + -
# domain name might contains -
regexEmail = re.compile(r'[a-z\d\.-_\+]+@{1}[a-z\d\.-]+', flags=re.I|re.M)

# this will return list
find_email = lambda txt: regexEmail.findall(txt)

for email in find_email(word):
    print(email)
