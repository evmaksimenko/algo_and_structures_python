"""
9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму
его цифр.
"""

max_num = 0
max_sum = 0

while True:
    n = input("Введите число (или пустую строку для выхода): ")
    if n == "":
        break
    current_sum = sum(list(map(int, n)))
    if current_sum > max_sum:
        max_sum = current_sum
        max_num = n

print(f"Число с наибольшей суммой цифр {max_num}. Сумма цифр {max_sum}.")