"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""

from random import randint, randrange
from timeit import timeit


def get_median_s(a):
    """
    Поиск медианы в массиве из его отсортированной копии
    :param a: массив для поиска медианы
    :return: значение элемента массива-медианы
    """
    a = sorted(a)
    if len(a) % 2 == 1:
        return a[len(a) // 2]
    else:
        return 0.5 * (a[len(a) // 2 - 1] + a[len(a) // 2])


def median_ns(a, k: int):
    """
    Рекурсивный поиск медианы в массиве методом медианы медиан (quickselect) без сортировки массива
    :param a: массив для поиска медианы
    :param k: позиция элемента-медианы
    :return: Значение элемента массива-медианы
    """
    if len(a) == 1:
        return a[0]
    index = randrange(len(a))
    less_part = [x for x in a if x < a[index]]
    bigger_part = [x for x in a if x > a[index]]
    if k <= len(less_part):
        return median_ns(less_part, k)
    elif k > len(a) - len(bigger_part):
        return median_ns(bigger_part, k - (len(a) - len(bigger_part)))
    else:
        return a[index]


def get_median_ns(a):
    """
    Хелпер для вызова функции median_ns, проверяет длину массива на корректность
    :param a: массив для поиска медианы
    :return: None, если длина массива чётная, или значение медианы
    """
    if len(a) % 2 != 1:
        print('Длина массива должна быть нечётной')
        return
    return median_ns(a, len(a) // 2 + 1)


M = 100
arr = [randint(0, 50) for _ in range(2 * M + 1)]
print(f'Исходный массив')
print(arr)
print(f'Отсортированный массив')
print(sorted(arr))
print(f'Медиана из сортировки равна: {get_median_s(arr)}')
print(f'Медиана из рекурсивного поиска равна: {get_median_ns(arr)}')
