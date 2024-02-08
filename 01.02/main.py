# Variant 27
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
        # вне квадрата
        if abs(x) > r2 or abs(y) > r2:
            return 'D'
        # на границе
        elif abs(x) == r2 or abs(y) == r2:
            if y > 0:
                return 'B D'
            return 'C D'
        # вне малого квадрата
        elif abs(x) > r1 or abs(y) > r1:
            if y > 0:
                return 'B'
            return 'C'
        # на границе малого круга
        elif abs(x) == r1 or abs(y) == r1:
            if y > 0:
                return 'A B'
            return 'A C'
        # центр
        return 'A'
    # оси
    else:
        # ось Y
        if y == 0:
            return 'A ' + \
                ('B ' if r1 <= -x <= r2 else '') + \
                ('C ' if r1 <= x <= r2 else '') + \
                ('D' if abs(x) == r2 else '')
        # ось X
        elif x == 0:
            return 'A ' + \
                ('B ' if r1 <= y <= r2 else '') + \
                ('С ' if r1 <= -y <= r2 else '') + \
                ('D' if abs(y) == r2 else '')


if __name__ == '__main__':
    x = float(input('x: '))
    y = float(input('y: '))
    r1 = float(input('r1: '))
    r2 = float(input('r2: '))

    if r1 > r2:
        r1, r2 = r2, r1

    print(f'Попало в: {shoot(x, y, r1, r2)}')

    # import random
    # for _ in range(20):
    #     x, y = random.randint(-10, 10), random.randint(-10, 10)
    #     print({(x, y): shoot(x, y, 5, 10)})