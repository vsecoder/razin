

while True:
    x1 = float(input('Введите значение x1: '))
    x2 = float(input('Введите значение x2: '))
    dx = float(input('Введите шаг dx: '))
    e = float(input('Введите погрешность e: '))

    print('\nРезультат:\n')

    if abs(x1) >= 1 or abs(x2) >= 1:
        print('Неверное значение x')
        print('\n----------------------------------------\n')
        continue

    i = x1
    while i < x2:
        digit = 0
        res = 0
        n = 0
        x_i = (i + 2) / (i**2 - 2*i - 3)

        while abs(x_i - res) > e:
            digit = ((-1) ** (n + 1) - 5 / 3 ** (n + 1)) * i**n
            res += digit / 4
            n += 1

        print(f'{i:>5g} {x_i:>10g} {res:>10g}')
        i += dx

    print('\n----------------------------------------\n')


