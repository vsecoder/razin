from math import log, sin


def y_(x):
    return log(x) + sin(x)


def f(a, b, dx):
    s = 0
    x = a

    while x <= b:
        y = y_(x)
        s += y * dx
        x += dx

    return s


if __name__ == "__main__":
    a = int(input("a: "))
    b = int(input("b: "))
    dx = int(input("dx: "))

    print(f"S = {f(a, b, dx)}")
