from math import tan


def y(x):
    return abs(tan(0.2*x)) + x


def f(a, b, dx):
    s = 0
    x = a

    while x <= b:
        s += y(x) * dx
        x += dx

    return s


if __name__ == "__main__":
    a = int(input("a: "))
    b = int(input("b: "))
    dx = int(input("dx: "))

    print(f"S = {f(a, b, dx)}")
