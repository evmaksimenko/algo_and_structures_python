"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

"""
#1
class Hex:
    @staticmethod
    def to_num(digits_list):
        return int(''.join(digits_list), 16)

    @staticmethod
    def to_hex(num):
        return Hex(hex(num)[2:])

    def __init__(self, value):
        self.hex_digits = [ch for ch in (value.upper())]

    def __add__(self, other):
        return Hex.to_hex(Hex.to_num(self.hex_digits) + Hex.to_num(other.hex_digits))

    def __mul__(self, other):
        return Hex.to_hex(Hex.to_num(self.hex_digits) * Hex.to_num(other.hex_digits))

    def __str__(self):
        return str(self.hex_digits)


a = Hex('A2')
print(a)
b = Hex('C4F')
print(b)
c = a + b
print(c)
d = a * b
print(d)
"""

"""
# 2
import string

a = [ch.upper() for ch in input("Введите первое число: ") if ch in string.hexdigits]
b = [ch.upper() for ch in input("Введите второе число: ") if ch in string.hexdigits]
print(a)
print(b)
c = [ch.upper() for ch in hex(int(''.join(a), 16) + int(''.join(b), 16))[2:]]
d = [ch.upper() for ch in hex(int(''.join(a), 16) * int(''.join(b), 16))[2:]]
print(f'Сумма чисел равна {c}')
print(f'Произведение чисел равно {d}')
"""
