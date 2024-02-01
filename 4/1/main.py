import random

N = 3


def init(random_=False):
    v = []

    for _ in range(N):
        if random_:
            v.append(random.randint(-10_000, 10_000))
            continue
        v.append(
            int(input(": "))
        )

    return v


def add(): pass


def sub(): pass


def mul(): pass


def mod(): pass


def ang(): pass


def output(v): pass


if __name__ == "__main__":
    v = init(True)

    output(v)
