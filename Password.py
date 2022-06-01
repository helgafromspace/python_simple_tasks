import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars =''

n = int(input('Введите количество паролей для генерации' + '\n'))
length = int(input('Введите длину одного пароля' + '\n'))
dig = input('Пароль должен содержать цифры? (Да/Нет)' + '\n').lower().strip()
if dig == 'да':
     dig = True
upp = input('Пароль содержит прописные буквы? (Да/Нет)' + '\n').lower().strip()
if upp == 'да':
     upp = True
low =  input('Пароль содержит строчные буквы? (Да/Нет)' + '\n').lower().strip()
if low == 'да':
     low = True
symb = input('Пароль содержит символы "!#$%&*+-=?@^_"? (Да/Нет)' + '\n').lower().strip()
if symb == 'да':
     symb = True
exc = input('Исключать неоднозначные символы из пароля "il1Lo0O"? (Да/Нет)' + '\n').lower().strip()
if exc == 'да':
     exc = True
     
if dig == True:
    chars += digits
if upp == True:
    chars += uppercase_letters
if low == True:
    chars += lowercase_letters
if symb == True:
    chars += punctuation
if exc == True:
    chars = chars.replace('i','').replace('l','').replace('1','').replace('L','').replace('o','').replace('0','').replace('O','')

def generate_password(length,chars):
    password = ''
    for i in range(0, length):
        num = random.randint(0,len(chars))
        password += chars[num]
    print(password)
    
generate_password(length, chars)

for i in range(1,n): 
    generate_password(length,chars)
