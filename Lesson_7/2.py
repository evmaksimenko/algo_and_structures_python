"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""
from random import random


def merge_sort(a):
    if len(a) <= 1:
        return a
    left = merge_sort(a[:len(a)//2])
    right = merge_sort(a[len(a)//2:])
    merge = []
    while True:
        if not left and not right:
            break
        if not left:
            merge.append(right.pop(0))
        elif not right:
            merge.append(left.pop(0))
        else:
            if left[0] <= right[0]:
                merge.append(left.pop(0))
            else:
                merge.append(right.pop(0))

    return merge


N = 10
arr = [round(random() * 50, 3) for _ in range(N)]
print(arr)
print(merge_sort(arr))
