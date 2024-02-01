from math import sqrt, cos, tan, sin, log


def f(x, a, b):
    if x <= a:
        return (
            sqrt(-x) * cos(x)
        ) if x <= 0 else 'Error'
    elif a < x < b:
        return abs(tan(0.2 * x)) + x
    return (
            log(x) + sin(x)
        ) if x <= 0 else 'Error'


if __name__ == "__main__":
    a = int(input("a: "))
    b = int(input("b: "))
    x = int(input("x: "))

    if a > b: a, b = b, a

    print(f"f({x}) = {f(x, a, b)}")
