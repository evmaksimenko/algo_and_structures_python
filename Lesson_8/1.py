"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
from collections import defaultdict


class Node:
    """
    Узел дерева
    """
    def __init__(self, v=0, l=None, r=None):
        self.value = v
        self.left = l
        self.right = r

    def __str__(self):
        return '[' + str(self.value) + ']'

    def __repr__(self):
        return '[' + str(self.value) + '(' + str(self.left) + ',' + str(self.right) + ')]'


def get_freq(s0):
    """
    Функция вычисляет частоту символов в строке
    :param s0: исходная строка
    :return: массив с элементами (символ, Node), упорядоченный по количеству символов Node.value
    """
    d = defaultdict(Node)
    for c in s0:
        d[c].value += 1
    return sorted(d.items(), key=lambda kv: kv[1].value)


def build_tree(s0):
    """
    Функция строит дерево для преобразования Хаффмана
    :param s0: исходная строка
    :return: root Node
    """
    l = get_freq(s0)
    while True:
        l = sorted(l, key=lambda kv: kv[1].value)
        if len(l) > 1:
            v1 = l.pop(0)
            v2 = l.pop(0)
            v = ('', Node(v1[1].value + v2[1].value, v1, v2))
            l.append(v)
        else:
            break
    return l[0]


def get_code_dict(s0):
    """
    Функция строит словарь для преобразования Хаффмана
    :param s0: исходная строка
    :return: словарь с элементами {символ, строка битового представления}
    """
    d = build_tree(s0)
    d2 = defaultdict(str)

    def search_deep(item, val=''):
        if not item[1].right and not item[1].left:
            d2[item[0]] = val
        else:
            if item[1].left:
                search_deep(item[1].left, val + '0')
            if item[1].right:
                search_deep(item[1].right, val + '1')

    search_deep(d)
    return d2


def encode_str_haff(s0, d):
    """
    Функция кодирует строку методом Хаффмана
    :param s0: исходная строка
    :param d: словарь для кодирования
    :return: строка - битовое представление
    """
    res = ''
    for c in s0:
        res += d[c]
    return res

def encode_str_bin(s0):
    """
    Функция преобразует строку в битовое представление
    :param s0: исходная строка
    :return: битовая строка
    """
    res = ''
    for c in s0:
        res += '{0:08b}'.format(c) + ' '
    return res

if __name__ == "__main__":
    s = b"beep boop beer!"
    cd = get_code_dict(s) # Получаем словарь для кодирования строки
    print(f'Исходная строка {s}')
    print(f'Битовое представление строки {encode_str_bin(s)}')
    print('Частоты символов:')
    for k,v in get_freq(s):
        print(f'"{chr(k)}" - {v.value}')
    print('Словарь для сжатия:')
    for k,v in cd.items():
        print(f'"{chr(k)}" -> "{v}"')
    print(f'После сжатия {encode_str_haff(s, cd)}')
