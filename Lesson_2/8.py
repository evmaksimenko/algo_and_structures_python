"""
8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел
 и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""
num_count = int(input("Введите количество чисел: "))
digit_to_find = int(input("Введите цифру для поиска: "))

digit_count = 0

for i in range(num_count):
    current_num = input("Введите число: ")
    digit_count += sum(list(filter(lambda x: x == digit_to_find, map(int, current_num))))

print(f"Цифра встречается {digit_count} раз.")
