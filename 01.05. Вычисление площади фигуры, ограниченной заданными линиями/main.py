from math import sin, log, tan
from random import uniform

while True:
    print('Для выбора метода интегрирования введите требуемое число:')
    print('1 - метод прямоугольников')
    print('2 - метод трапеций')
    method = int(input())
    a = float(input('Введите нижний предел интегрирования a: '))
    b = float(input('Введите верхний предел интегрирования b: '))
    dx = float(input('Введите шаг интегрирования dx: '))
    N = int(input('\nВведите количество точек N: '))

    min_y, max_y = None, 0
    S = 0

    x = a
    while x <= b:
        if method:
            S += (abs(tan(0.2 * x)) + x - log(x) + sin(x)) * dx
        else:
            xdx = x + dx
            S += ((abs(tan(0.2 * xdx)) + xdx + abs(tan(0.2 * x)) + x) / 2 -
                  (log(xdx) + sin(xdx) + log(x) + sin(x)) / 2) * dx

        y = [abs(tan(0.2 * x)) + x, log(x) + sin(x)]
        if min_y is None:
            min_y = min(y)
        if min_y > min(y):
            min_y = min(y)
        if max_y < max(y):
            max_y = max(y)
        x = x + dx
    S0 = abs(b - a) * abs(min_y - max_y)

    n = 0
    for _ in range(N):
        x = uniform(a, b)
        y = uniform(max_y, min_y)
        if log(x) + sin(x) <= y <= abs(tan(0.2 * x)) + x:
            n += 1
    Snk = S0 * n / N

    print('\nРезультат:\n')

    if method:
        print(f'Метод прямоугольника: {S:g}')
    else:
        print(f'Метод трапеции: {S:g}')
    print(f'Метод Монте-Карло: {Snk:g}')

    print('\n----------------------------------------\n')
