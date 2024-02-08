def f(x):
    return (x + 2) / (x**2 - 2*x - 3)


if __name__ == '__main__':
    x1 = float(input('x1: '))
    x2 = float(input('x2: '))
    dx = float(input('dx: '))
    e = float(input('e: '))

    if abs(x1) >= 1 or abs(x2) >= 1:
        print('Error: |x1,2| < 1')
        exit()

    i = x1
    while i < x2:
        digit = 0
        res = 0
        n = 0

        while abs(f(i) - res) > e:
            digit = ((-1) ** (n + 1) - 5 / 3 ** (n + 1)) * i**n
            res += digit / 4
            n += 1

        print(f'{i:g} {f(i):g} {res:g}')
        i += dx
