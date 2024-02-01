# Variant 27
import random


def shoot(x, y, r1, r2):
    # 1 и 3 четверть
    if x * y > 0:
        # внешняя окружность
        if x ** 2 + y ** 2 > r2 ** 2:
            return 'D'
        # пересечение с внешней окружностью
        elif x ** 2 + y ** 2 == r2 ** 2:
            return 'A D'
        # внутри
        return 'A'
    # 2 и 4 четверть
    elif x * y < 0:
        if abs(x) > r2 or abs(y) > r2:
            return 'D'
        elif abs(x) == r2 or abs(y) == r2:
            return ('B ' if y > 0 else 'C ') + 'D'
        elif abs(x) > r1 or abs(y) > r1:
            return 'B' if y > 0 else 'C'
        elif abs(x) == r1 or abs(y) == r1 and y > 0: return True
        return 'A'
    # оси
    else:
        # ось Y
        if y == 0:
            return 'A ' + \
                ('C ' if r1 <= x <= r2 else '') + \
                ('B ' if r1 <= -x <= r2 else '') + \
                ('D' if abs(x) == r2 else '')
        # ось X
        elif x == 0:
            return 'A ' + \
                ('B ' if r1 <= y <= r2 else '') + \
                ('С ' if r1 <= -y <= r2 else '') + \
                ('D' if abs(y) == r2 else '')


if __name__ == "__main__":
    x = float(input("x: "))
    y = float(input("y: "))
    r1 = float(input("r1: "))
    r2 = float(input("r2: "))

    if r1 > r2: r1, r2 = r2, r1

    print(f"Попало в: {shoot(x, y, r1, r2)}")

    #for _ in range(20):
    #    x, y = random.randint(-10, 10), random.randint(-10, 10)
    #    print({(x, y): shoot(x, y, 5, 10)})