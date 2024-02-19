
r1 = 5       # радиус малой окружности
r2 = 2 * r1  # радиус большой окружности

while True:
    x = float(input('Введите координату x: '))
    y = float(input('Введите координату y: '))

    print('\nРезультат:\n')

    if 0 <= x <= r2 and 0 <= y <= r2 and x**2 + y**2 <= r2**2 or \
            0 >= x >= -r2 and 0 >= y >= -r2 and x**2 + y**2 <= r2**2 or \
            0 >= x >= -r1 and 0 <= y <= r1 or \
            0 <= x <= r1 and y >= -r1:
        print('Область попадания A')

    if -r1 >= x >= -r2 and 0 <= y <= r2 or \
            r1 <= y <= r2 and 0 >= x >= -r2:
        print('Область попадания B')

    if r1 <= x <= r2 and 0 >= y >= -r2 or \
            -r1 >= y >= -r2 and 0 <= x <= r2:
        print('Область попадания C')

    if abs(x) >= r2 or abs(y) >= r2 or \
            x * y > 0 and x**2 + y**2 >= r2**2:
        print('Область попадания D')

    print('\n----------------------------------------\n')
