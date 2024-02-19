
from math import tan

while True:
    a = float(input('Введите нижний предел интегрирования a: '))
    b = float(input('Введите верхний предел интегрирования b: '))
    dx = float(input('Введите шаг интегрирования dx: '))

    s = 0
    x = a

    while x <= b:
        s += (abs(tan(0.2 * x)) + x) * dx
        x += dx

    print('\nРезультат:\n')

    print(f'Значение интеграла {s}')
    print('\n----------------------------------------\n')





