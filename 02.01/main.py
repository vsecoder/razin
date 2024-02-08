from math import sin, log, tan
import random


def fun1(x):
    return abs(tan(0.2 * x)) + x

def fun2(x):
    return log(x) + sin(x)

def is_in(x, y):
    if fun2(x) <= y <= fun1(x):
        return True
    return False

def Rectangle(a, b, dx):
    s = 0
    x = a

    while x <= b:
        y = fun1(x) - fun2(x)
        s += y * dx
        x += dx

    return s

def Trapezoid_method(a, b, dx):
    s = 0
    x = a

    while x <= b:
        y = (fun1(x + dx) + fun1(x)) / 2 - (fun2(x + dx) + fun2(x)) / 2
        s += y * dx
        x += dx

    return s

def Monte_Carlo_method(n, a, b, c, d):
    m = 0
    x_ = abs(b - a)
    y_ = abs(d - c)
    l = x_ * y_
    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(c, d)

        r = is_in(x, y)

        m += int(r)

    return l * m / n


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


if __name__ == '__main__':
    a = float(input('a: '))
    b = float(input('b: '))
    dx = float(input('dx: '))
    n = int(input('dots: '))
    print(f'Методом прямоугольника: {Rectangle(a, b, dx)}')
    print(f'Методом трапеции: {Trapezoid_method(a, b, dx)}')
    c, d = min_max(a, b, dx)
    print(f'Методом Монте Карло: {Monte_Carlo_method(n, a, b, c, d)}')
