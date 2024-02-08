from math import sqrt, cos, tan, sin, log


def f(x, a, b):
    if x <= a:
        return sqrt(-x) * cos(x)
    elif a < x < b:
        return abs(tan(0.2 * x)) + x
    else:
        return log(x) + sin(x)


if __name__ == '__main__':
    while True:
        a = float(input('a: '))
        b = float(input('b: '))
        x = float(input('x: '))

        if a > b:
            a, b = b, a

        print(f'f({x}) = {f(x, a, b)}')
