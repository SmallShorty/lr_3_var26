import re

def is_valid_snils(num):
    pattern = r'^\d{3}-\d{3}-\d{3}\s\d{2}$'
    return bool(re.match(pattern, num))

snils = ''

while snils != '0':
    snils = input('Введите номер СНИЛС: ')
    if is_valid_snils(snils):
        print('Номер СНИЛС корректен')
    else:
        print('Номер СНИЛС некорректен')