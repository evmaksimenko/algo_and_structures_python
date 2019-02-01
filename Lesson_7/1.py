"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
from random import randrange


def bubble_sort(array, reverse=False):
    a = array[:]
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            condition = a[j] < a[j + 1] if reverse else a[j] > a[j + 1]
            if condition:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


N = 20
arr = [randrange(-100, 100) for _ in range(N)]

print('Исходный массив:')
print(arr)
print('Отсортированный массив по убыванию:')
print(bubble_sort(arr, reverse=True))
