import random
from main import fun1, fun2


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
