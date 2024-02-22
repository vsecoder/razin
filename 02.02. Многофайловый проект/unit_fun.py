
# -----------------------------------------------------------------------------
from math import sin, log, tan
import unit_var
import random
# -----------------------------------------------------------------------------


# функция, ограничивающая фигуру сверху
def fun1(x):
    return abs(tan(0.2 * x)) + x

# -----------------------------------------------------------------------------


# функция, ограничивающая фигуру снизу
def fun2(x):
    return log(x) + sin(x)

# -----------------------------------------------------------------------------


# вычисление площади фигуры методом прямоугольников
def Rectangle_method(a, b, dx):
    s = 0
    x = a
    while x <= b:
        y = fun1(x) - fun2(x)
        s += y * dx
        x += dx

    unit_var.S = s

# -----------------------------------------------------------------------------


# вычисление площади фигуры методом трапеций
def Trapezoid_method(a, b, dx):
    s = 0
    x = a

    while x <= b:
        y = ((fun1(x + dx) + fun1(x)) - (fun2(x + dx) + fun2(x))) / 2
        s += y * dx
        x += dx

    unit_var.S = s

# -----------------------------------------------------------------------------


# вычисление площади фигуры методом Монте-Карло
def Monte_Carlo_method(a, b, N):
    x = a
    max_y = fun1(x)
    min_y = fun2(x)

    dx = (b - a) / 1000

    while x <= b:
        max_y = max(max_y, fun1(x))
        min_y = min(min_y, fun2(x))
        x += dx

    S0 = (b - a) * (max_y - min_y)

    n = 0
    for _ in range(N):
        x = random.uniform(a, b)
        y = random.uniform(min_y, max_y)
        if fun2(x) <= y <= fun1(x):
            n += 1

    unit_var.Smk = S0 * n / N
