"""
6.	В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. 
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import randint
N = 20
arr = [randint(0, 100) for _ in range(N)]
print(arr)

# 1
pos1 = arr.index(min(arr))
pos2 = arr.index(max(arr))
print(f'Позиция минимального элемента {pos1}')
print(f'Позиция максимального элемента {pos2}')
if pos1 > pos2:
    pos1, pos2 = pos2, pos1
s = sum(arr[pos1+1:pos2])
print(f'Сумма между элементами {s}')
print()

# 2
min_elem = arr[0]
min_elem_pos = 0
max_elem = arr[0]
max_elem_pos = 0
for i, v in enumerate(arr):
    if v > max_elem:
        max_elem = v
        max_elem_pos = i
    if v < min_elem:
        min_elem = v
        min_elem_pos = i
print(f'Позиция минимального элемента {min_elem_pos}')
print(f'Позиция максимального элемента {max_elem_pos}')
if min_elem_pos > max_elem_pos:
    min_elem_pos, max_elem_pos = max_elem_pos, min_elem_pos
s = sum(arr[min_elem_pos+1:max_elem_pos])
print(f'Сумма между элементами {s}')
