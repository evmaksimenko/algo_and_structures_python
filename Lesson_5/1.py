"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import defaultdict
from functools import reduce


def annual_profit(l):
    # Вычисляем годовую прибыль по квартальным прибылям
    profit = reduce(lambda acc, x: acc * (1 + x / 100), [1] + l)
    # Преобразуем в % и возвращаем
    return (profit - 1) * 100


company_number = int(input('Введите количество предприятий: '))
companies = defaultdict(list)
for i in range(company_number):
    company = input(f'Введите название {i + 1} компании: ')
    for quarter in range(4):
        q = float(input(f'Введите прибыль в % за {quarter + 1} квартал: '))
        companies[company].append(q)
print()

total = 0
for c in companies.values():
    # Вычисляем годовую прибыль по квартальным прибылям
    total += annual_profit(c)
# Средняя годовая прибыль среди всех предприятий
avg = total / company_number

print(f'Средняя годовая прибыль предприятий {avg:5.2f}')
print()

print('Предприятия с прибылью выше среднего:')
is_find = False
for c in companies.keys():
    if annual_profit(companies[c]) > avg:
        is_find = True
        print(c)
if not is_find:
    print('отсутствуют')

print('Предприятия с прибылью ниже среднего:')
is_find = False
for c in companies.keys():
    if annual_profit(companies[c]) < avg:
        is_find = True
        print(c)
if not is_find:
    print('отсутствуют')
