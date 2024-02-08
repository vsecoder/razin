
from math import sqrt, cos, tan, sin, log

a = float(input('Введите значение a: '))
b = float(input('Введите значение b: '))

while True:
    x = float(input('x: '))

    if x <= a:
        y = sqrt(-x) * cos(x)
    elif a < x < b:
        y = abs(tan(0.2 * x)) + x
    else:
        y = log(x) + sin(x)

    print(f'y: {y}')
