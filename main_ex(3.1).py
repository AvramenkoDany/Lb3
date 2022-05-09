"""
1. Підрахувати k - кількість цифр в десятковому запису цілого невід'ємного числа n.
"""


def main(val):
    if val > 0:
        return len(str(val))
    else:
        return 'Error'

print('Enter the int value:')
value = int(input(''))
print(main(value))

