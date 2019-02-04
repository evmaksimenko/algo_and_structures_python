"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
from typing import List

P = 31 # Множитель для варианта строк только из маленьких латинских букв.
R = 2**32

def hash_poly(s: str):
    """
    Получаем полиномиальный хеш
    hash(s) = s[0] * P^(M-1) + s[1] * P^(M-2) + ... + s[M-1] * P^0, где M - длина строки

    :param s: строка для вычисления хеша
    :return: хеш значение
    """
    h = 0
    for i, c in enumerate(s):
        h += (P**(len(s) - i - 1)) * (ord(c) - ord('a') + 1)
    h %= R
    return h


def count_s(s1: str, s2: str) -> List:
    """
    Поиск вхождений строки в строку
    :param s1: строка в которой проводится поиск
    :param s2: искомая строка
    :return: список с найденными позициями
    """
    res = []
    l1 = len(s1)
    l2 = len(s2)
    if l1 < l2:
        return []
    h1 = hash_poly(s1[:l2])
    h2 = hash_poly(s2)
    for i in range(l1 - l2):
        if h1 == h2:
            res.append(i)
        h1 = (P * h1 - (P ** l2) * hash_poly(s1[i]) + hash_poly(s1[i + l2])) % R
    return res


main_str = 'instr string finst'
str_to_find = 'in'
print(f'Строка "{str_to_find}" входит в строку "{main_str}" в позициях {count_s(main_str, str_to_find)}')
