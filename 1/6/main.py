def f(x):
    return (x + 2) / (x**2 - 2*x - 3)


if __name__ == "__main__":
    x = float(input("x: "))
    e = float(input("e: "))
    digit = 0
    res = 0
    n = 0

    if abs(x) >= 1:
        print("Error: |x| < 1")
        exit()

    while abs(f(x) - res) > e:
        digit = ((-1) ** (n + 1) - 5 / 3 ** (n + 1)) * x**n
        res += digit / 4
        n += 1

    print(f(x))
    print(res)
