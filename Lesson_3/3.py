#3.	В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint
N = 20
arr = [randint(0, 100) for _ in range(N)]
print(arr)

max_elem = arr[0]
max_pos = 0
min_elem = arr[0]
min_pos = 0
for i, v in enumerate(arr):
    if v > max_elem:
        max_elem = v
        max_pos = i
    if v < min_elem:
        min_elem = v
        min_pos = i
print(f"Минимальный элемент {min_elem} находится в позиции {min_pos}")
print(f"Максимальный элемент {max_elem} находится в позиции {max_pos}")
arr[max_pos], arr[min_pos] = arr[min_pos], arr[max_pos]
print(arr)

