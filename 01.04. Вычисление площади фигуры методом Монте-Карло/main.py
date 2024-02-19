
from random import uniform
from math import pi

r1 = 5                                          # радиус малой окружности
r2 = 2 * r1                                     # радиус большой окружности

S = (pi * r2**2) / 2 + r2**2 + r1**2            # площадь фигуры
S0 = (2 * r2)**2                                # площадь квадрата, описанного вокруг фигуры

while True:
    N = int(input('Введите кол-во точек N: '))

    n = 0
    for _ in range(N):
        x = uniform(-r2, r2)
        y = uniform(-r2, r2)

        if 0 <= x <= r2 and 0 <= y <= r2 and x ** 2 + y ** 2 <= r2 ** 2 or \
                0 >= x >= -r2 and 0 >= y >= -r2 and x ** 2 + y ** 2 <= r2 ** 2 or \
                0 >= x >= -r1 and 0 <= y <= r1 or 0 <= x <= r1 and 0 >= y >= -r1:
            n += 1

        if r1 <= x <= r2 and 0 >= y >= -r2 or -r1 >= y >= -r2 and 0 <= x <= r2:
            n += 1

    Snk = S0 * n / N

    print('\nРезультат:\n')

    print(f'Метод Монте-Карло: {Snk:g}')
    print(f'Точное значение: {S:g}')
    print('\n----------------------------------------\n')




