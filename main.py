import re

def is_valid_snils(num):
    pattern = r'^\d{3}-\d{3}-\d{3}\s\d{2}$'
    return bool(re.match(pattern, num))

with open('snils.txt', 'r') as file:
    for line in file:
        snils = line.strip()
        if is_valid_snils(snils):
            print(snils, 'Номер СНИЛС корректен')
        else:
            print(snils, 'Номер СНИЛС некорректен')