# -*- coding: utf-8 -*-
"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
"""
Windows 8.1 x64
python 3.7 x32
Обе версии программы потребляют одинаковое количество памяти - 12.7 MiB 
"""

# 4.	Определить, какое число в массиве встречается чаще всего.
from random import randint
from memory_profiler import profile

#1
@profile
def func1():
    N = 10000
    arr = [randint(0, 10) for _ in range(N)]

    d = {}
    for v in arr:
        d[v] = d.get(v, 0) + 1
    max_count = max(d.values())
    print('Числа, встречающиеся в массиве чаще всего')
    for (k, v) in d.items():
        if v == max_count:
            print(f'{k} встречается {v} раз(a)')
"""
Line #    Mem usage    Increment   Line Contents
================================================
    21     12.7 MiB     12.7 MiB   @profile
    22                             def func1():
    23     12.7 MiB      0.0 MiB       N = 10000
    24     12.7 MiB      0.0 MiB       arr = [randint(0, 10) for _ in range(N)]
    25                             
    26     12.7 MiB      0.0 MiB       d = {}
    27     12.7 MiB      0.0 MiB       for v in arr:
    28     12.7 MiB      0.0 MiB           d[v] = d.get(v, 0) + 1
    29     12.7 MiB      0.0 MiB       max_count = max(d.values())
    30     12.7 MiB      0.0 MiB       print('Числа, встречающиеся в массиве чаще всего')
    31     12.7 MiB      0.0 MiB       for (k, v) in d.items():
    32     12.7 MiB      0.0 MiB           if v == max_count:
    33     12.7 MiB      0.0 MiB               print(f'{k} встречается {v} раз(a)')
    """
#2
@profile
def func2():
    N = 10000
    arr = [randint(0, 10) for _ in range(N)]
    uniq = list(set(arr))
    max_val = max([arr.count(x) for x in uniq])
    print('Числа, встречающиеся в массиве чаще всего')
    for i in uniq:
        if arr.count(i) == max_val:
            print(f'{i} встречается {max_val} раз(a)')
"""
Line #    Mem usage    Increment   Line Contents
================================================
    36     12.7 MiB     12.7 MiB   @profile
    37                             def func2():
    38     12.7 MiB      0.0 MiB       N = 10000
    39     12.7 MiB      0.0 MiB       arr = [randint(0, 10) for _ in range(N)]
    40     12.7 MiB      0.0 MiB       uniq = list(set(arr))
    41     12.7 MiB      0.0 MiB       max_val = max([arr.count(x) for x in uniq])
    42     12.7 MiB      0.0 MiB       print('Числа, встречающиеся в массиве чаще всего')
    43     12.7 MiB      0.0 MiB       for i in uniq:
    44     12.7 MiB      0.0 MiB           if arr.count(i) == max_val:
    45     12.7 MiB      0.0 MiB               print(f'{i} встречается {max_val} раз(a)')
"""

if __name__ == "__main__":
    func1()
    func2()
