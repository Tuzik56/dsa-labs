import time

def factorial_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_rec(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_rec(n - 1)


test_values = [100, 500, 900, 1000]

for n in test_values:
    try:
        start = time.time()
        factorial_iter(n)
        time_iter = time.time() - start

        start = time.time()
        factorial_rec(n)
        time_rec = time.time() - start

        print(f"n = {n}")
        print("Цикл:", time_iter)
        print("Рекурсия:", time_rec)
    except RecursionError:
        print("RecursionError при " + str(n))
