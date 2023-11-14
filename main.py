import re

def control_sum(num):
    numbers = [int(d) for d in num if d.isdigit()][:9]
    weights = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    control_sum = sum([a * b for a, b in zip(numbers[:9], weights)])
    if control_sum < 100:
        return control_sum == numbers[9] * 10 + numbers[10]
    elif control_sum == 100 or control_sum == 101:
        return numbers[9] == 0 and numbers[10] == 0
    else:
        return False

def is_valid_snils(num):
    pattern = r'^\d{3}-\d{3}-\d{3}\s\d{2}$'
    return bool(re.match(pattern, num))+bool(control_sum(num))

with open('data.txt', 'r') as file:
    for line in file:
        snils = line.strip()
        if is_valid_snils(snils):
            print(snils, 'Номер СНИЛС корректен')
        else:
            print(snils, 'Номер СНИЛС некорректен')