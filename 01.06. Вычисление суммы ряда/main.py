

while True:
    x = float(input('Введите значение x: '))
    e = float(input('Введите погрешность e: '))

    print('\nРезультат:\n')
    if abs(x) >= 1:
        print('Неверное значение x\n')
        print('\n----------------------------------------\n')
        continue

    digit = 0
    res = 0
    n = 0

    sum_ = (x + 2) / (x**2 - 2*x - 3)

    while abs(sum_ - res) > e:
        digit = ((-1)**(n + 1) - 5 / 3**(n + 1)) * x**n
        res += digit / 4
        n += 1

    print(f'Левая часть равенства {sum_:g}')
    print(f'Правая часть равенства {res:g}')
    print('\n----------------------------------------\n')



