# 3.	По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
x1 = float(input("Введите координату x точки 1: "))
y1 = float(input("Введите координату y точки 1: "))
x2 = float(input("Введите координату x точки 2: "))
y2 = float(input("Введите координату y точки 2: "))

if x1 != x2:
    k = (y2-y1)/(x2-x1)
    b = y1-k*x1
    print("k = %.2f" % k)
    print("b = %.2f" % b)
else:
    print("Невозможно построить уравнение прямой")
