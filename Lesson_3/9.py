# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import randint
N = 5
M = 10

a = []
for i in range(N):
    b = []
    for j in range(M):
        v = randint(0, 100)
        b.append(v)
        print("%3d" % v, end='')
    a.append(b)
    print()

print('Минимальные зачения столбцов')
min_values = []
for j in range(M):
    t = []
    for i in range(N):
        t.append(a[i][j])
    print('%3d' % min(t), end='')
    min_values.append(min(t))
print()

print(f'Максимум среди минимумов {max(min_values)}')
