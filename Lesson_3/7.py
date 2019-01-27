"""
7.	В одномерном массиве целых чисел определить два наименьших элемента. 
Они могут быть как равны между собой (оба являться минимальными), так и различаться. 
"""
from random import randint
N = 20
a = [randint(0, 100) for _ in range(N)]
print(a)


# 1
def min_elem(a, m):
    min_elem_pos = 0
    min_elem = a[0]
    is_find = False
    for i, v in enumerate(a):
        if not is_find and m[i] == 0:
            is_find = True
            min_elem_pos = i
            min_elem = v
        elif m[i] == 0 and v < min_elem:
            min_elem_pos = i
            min_elem = v
    if is_find:
        m[min_elem_pos] = 1
        return min_elem_pos
    else:
        return -1


m = [0] * len(a)
min1_pos = min_elem(a, m)
if min1_pos >= 0:
    print(f'Первый минимальный элемент {a[min1_pos]} находится в позиции {min1_pos}')
min2_pos = min_elem(a, m)
if min2_pos >= 0:
    print(f'Второй минимальный элемент {a[min2_pos]} находится в позиции {min2_pos}')
print()

# 2
min1 = min(a)
min1_pos = a.index(min1)
a.remove(min1)
min2 = min(a)
min2_pos = a.index(min2)
if min2_pos >= min1_pos:
    min2_pos += 1
print(f'Первый минимальный элемент {min1} находится в позиции {min1_pos}')
print(f'Второй минимальный элемент {min2} находится в позиции {min2_pos}')
