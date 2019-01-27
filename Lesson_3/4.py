# 4.	Определить, какое число в массиве встречается чаще всего.
from random import randint
N = 20
arr = [randint(0, 10) for _ in range(N)]

#1
d = {}
for v in arr:
    d[v] = d.get(v, 0) + 1
max_count = max(d.values())
print('Числа, встречающиеся в массиве чаще всего')
for (k, v) in d.items():
    if v == max_count:
        print(f'{k} встречается {v} раз(a)')

#2
uniq = list(set(arr))
max_val = max([arr.count(x) for x in uniq])
print('Числа, встречающиеся в массиве чаще всего')
for i in uniq:
    if arr.count(i) == max_val:
        print(f'{i} встречается {max_val} раз(a)')
