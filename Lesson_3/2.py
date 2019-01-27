"""
2.	Во втором массиве сохранить индексы четных элементов первого массива. 
Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив 
надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), 
т.к. именно в этих позициях первого массива стоят четные числа.
"""

from random import randint
N = 20
ina = [randint(0, 100) for _ in range(N)]

#1
res = []
for i, v in enumerate(ina):
    if v % 2 == 0:
        res.append(i)

print(ina)
print(res)
print()

#2
res = [i for i in range(len(ina)) if ina[i] % 2 == 0]
print(ina)
print(res)
