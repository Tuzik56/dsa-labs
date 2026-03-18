import time


def power_iter(base, exp):
    result = 1
    for _ in range(exp):
        result *= base
    return result


def power_rec(base, exp):
    if exp == 0:
        return 1

    if exp % 2 == 0:
        half = power_rec(base, exp / 2)
        return half * half
    else:
        return base * power_rec(base, exp - 1)


tests = [1000, 5000, 10000]

for n in tests:
    start = time.time()
    power_iter(2, n)
    iter_time = time.time() - start

    start = time.time()
    power_rec(2, n)
    rec_time = time.time() - start

    print(f"Степень {n}")
    print("Цикл:", iter_time)
    print("Быстрое возведение:", rec_time)