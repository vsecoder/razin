from square import *
from math import sin, log, tan


def fun1(x):
    return abs(tan(0.2 * x)) + x


def fun2(x):
    return log(x) + sin(x)


def min_max(a, b, dx):
    y_min, y_max = None, 0
    x = a

    while x <= b:
        y = [fun1(x), fun2(x)]

        if y_min == None: y_min = min(y)

        if y_min > min(y): y_min = min(y)
        if y_max < max(y): y_max = max(y)

        x += dx

    return y_min, y_max


if __name__ == "__main__":
    a = float(input("a: "))
    b = float(input("b: "))
    dx = float(input("dx: "))
    n = int(input("dots: "))

    print(f"Методом прямоугольника: {Rectangle(a, b, dx)}")
    print(f"Методом трапеции: {Trapezoid_method(a, b, dx)}")

    c, d = min_max(a, b, dx)
    print(f"Методом Монте Карло: {Monte_Carlo_method(n, a, b, c, d)}")
