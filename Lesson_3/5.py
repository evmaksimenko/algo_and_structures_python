#5.	В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию (индекс) в массиве.
from random import randint
N = 20
arr = [randint(-100, 100) for _ in range(N)]
print(arr)

#1
find = False
max_neg = 0
max_neg_pos = 0
for i, v in enumerate(arr):
    if v < 0:
        if not find:
            max_neg = v
            max_neg_pos = i
            find = True
        elif v > max_neg:
            max_neg = v
            max_neg_pos = i

print(f'Максимальное отрицательное число {max_neg} находится по индексу {max_neg_pos}')

#2
max_neg = sorted(filter(lambda x: x < 0, arr))[-1]
max_neg_pos = arr.index(max_neg)
print(f'Максимальное отрицательное число {max_neg} находится по индексу {max_neg_pos}')

