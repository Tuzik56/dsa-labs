import random


def random_multiply(n, depth):
    if depth == 0:  # базовый случай
        return n

    k = random.uniform(0.5, 1.5)
    return random_multiply(n * k, depth - 1)


print(random_multiply(10, 5))