# v27. A+C
import random
from math import pi


def shoot(x, y, r1, r2):
    if x * y >= 0:
        if x**2 + y**2 <= r2**2:
            return True

    if abs(x) <= r2 and abs(y) <= r2:
        if x >= 0 >= y:
            return True
    
    if abs(x) <= r1 and abs(y) <= r1:
        if x <= 0 <= y:
            return True

    return False


def monte_carlo(n):
    m = 0
    l = 20 ** 2

    for _ in range(n):
        x = random.uniform(-10, 10)
        y = random.uniform(-10, 10)

        c = shoot(x, y, 5, 10)

        if c:
            m += 1

    return l * m / n


def s():
    circle = (pi * 10 ** 2) / 2
    square_big = 10 ** 2
    square_mini = 5 ** 2
    return circle + square_big + square_mini


if __name__ == "__main__":
    n = int(input("n: "))
    monte = monte_carlo(n)
    S = s()
    print(f"Метод Монте-Карло: {monte}")
    print(f"Вычислениями: {S}")
    print(f"Разница: {abs(monte-S)}")
