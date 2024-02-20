
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

    # вычисление площади численными методами

    if method == 1:                # метод прямоугольников
        x = a
        S = 0
        while x <= b:
            S += (abs(tan(0.2 * x)) + x - (log(x) + sin(x))) * dx
            x += dx

    if method == 2:                # метод трапеций
        x = a
        S = 0
        while x <= b:
            S += ((abs(tan(0.2 * (x + dx))) + (x + dx) + abs(tan(0.2 * x)) + x) -
                  (log(x + dx) + sin(x + dx) + log(x) + sin(x))) / 2 * dx
            x += dx

    # получение максимума функции по y на данном промежутке
    x = a
    max_y = abs(tan(0.2 * x)) + x
    while x <= b:
        y = abs(tan(0.2 * x)) + x
        max_y = max(max_y, y)
        x += dx

    # получение минимума функции по y на данном промежутке
    x = a
    min_y = log(x) + sin(x)
    while x <= b:
        y = log(x) + sin(x)
        min_y = min(min_y, y)
        x += dx

    # площадь прямоугольника, описанного вокруг фигуры
    S0 = (b - a) * (max_y - min_y)

    # вычисление площади методом Монте-Карло
    n = 0
    for _ in range(N):
        x = uniform(a, b)
        y = uniform(min_y, max_y)
        if log(x) + sin(x) <= y <= abs(tan(0.2 * x)) + x:
            n += 1

    Smk = S0 * n / N

    print('\nРезультат:\n')

    if method == 1:
        print(f'Метод прямоугольников: {S:g}')
    else:
        print(f'Метод трапеций: {S:g}')

    print(f'Метод Монте-Карло: {Smk:g}')

    print('\n----------------------------------------\n')




