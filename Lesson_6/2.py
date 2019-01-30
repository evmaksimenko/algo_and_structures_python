"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""
"""
Windows 8.1 x64
python 2.7 x32
"""
from pympler import asizeof
# Класс с использование __slots__
class MyClassWithSlots:
    __slots__ = 'X', 'Y', 'data'

    def __init__(self):
        self.X = 0
        self.Y = 0
        self.data = "New point"
# Обычный класс
class MyClassWithoutSlots:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.data = "New point"


a = MyClassWithSlots()
print(f'Размер экземпляра класса с использованием __slots__ равен {asizeof.asizeof(a)} байт') # 96 байт
print(f'Словарь аттрибутов класса: {MyClassWithSlots.__dict__}')
try:
    print(f'Словарь аттрибутов экземпляра: {a.__dict__}')
except AttributeError:
    print('У экземпляра a отсутствует __dict__')
print()

b = MyClassWithoutSlots()
print(f'Размер экземпляра класса без использования __slots__ равен {asizeof.asizeof(b)} байт') # 256 байт
print(f'Словарь аттрибутов класса: {MyClassWithoutSlots.__dict__}')
print(f'Словарь аттрибутов экземпляра: {b.__dict__}')
