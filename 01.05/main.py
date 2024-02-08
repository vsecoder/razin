from math import sin, log, tan
import random


def y1(x):
    return abs(tan(0.2 * x)) + x


def y2(x):
    return log(x) + sin(x)


def is_in(x, y):
    if y2(x) <= y <= y1(x):
        return True
    return False


def f1(a, b, dx):
    s = 0
    x = a

    while x <= b:
        y = y1(x) - y2(x)
        s += y * dx
        x += dx

    return s


def f2(a, b, dx):
    s = 0
    x = a

    while x <= b:
        y = (y1(x + dx) + y1(x)) / 2 - (y2(x + dx) + y2(x)) / 2
        s += y * dx
        x += dx

    return s


def monte_carlo(n, a, b, c, d):
    m = 0
    l = abs(b - a) * abs(d - c)

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
        y = [y1(x), y2(x)]

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
    print(f'Методом прямоугольника: {f1(a, b, dx)}')
    print(f'Методом трапеции: {f2(a, b, dx)}')
    c, d = min_max(a, b, dx)
    print(f'Методом Монте-Карло: {monte_carlo(n, a, b, c, d)}')
