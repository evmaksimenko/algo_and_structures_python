"""
2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3
четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

# 1
n = input("Введите число: ")
digits = list(map(int, n))
odd_digits = list(filter(lambda x: x % 2 == 1, digits))
even_digits = list(filter(lambda x: x % 2 == 0, digits))
print(f"Нечётных чисел {len(odd_digits)} {odd_digits}")
print(f"Чётных чисел {len(even_digits)} {even_digits}")

# 2
n = int(n)
odd_digits = []
even_digits = []
while n > 0:
    r = n % 10
    n //= 10
    if r % 2 == 0:
        even_digits.append(r)
    else:
        odd_digits.append(r)
print(f"Нечётных чисел {len(odd_digits)} {odd_digits}")
print(f"Чётных чисел {len(even_digits)} {even_digits}")
