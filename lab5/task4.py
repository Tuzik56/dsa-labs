import random

orders_random = [57, 14, 83, 29, 61, 45, 72, 10, 34, 98, 21, 66, 39, 50, 7, 66, 28, 64, 72, 62, 66, 26, 8, 29, 89, 35, 15, 32, 27, 55, 3, 59, 100, 21, 56, 85, 36, 23, 75, 18, 49, 18, 78, 44, 59, 59, 96, 68, 23, 81, 89, 4, 25, 90, 92, 72, 8, 82, 89, 44, 82, 55, 49, 23, 49, 80, 22, 84, 67, 21, 88, 65, 73, 99, 88, 49, 92, 39, 83, 66, 83, 26, 53, 75, 56, 94, 59, 89, 71, 37, 64, 99, 96, 73, 83, 30, 79, 78, 29, 7]

orders_many_duplicates = [5, 3, 5, 2, 5, 1, 5, 4, 5, 0, 5, 3, 5, 2, 5, 1, 9, 7, 0, 10, 4, 8, 2, 6, 3, 10, 5, 1, 9, 0, 4, 7, 2, 8, 3, 6, 10, 5, 1, 9, 4, 0, 7, 2, 8, 6, 3, 10, 5, 1, 9, 0, 4, 7, 8, 2, 6, 3, 10, 5, 1, 9, 0, 4, 7, 2, 8, 6, 3, 10, 5, 1, 9, 0, 4, 7, 2, 8, 6, 3, 10, 5, 1, 9, 0, 4, 7, 2, 8, 6, 3, 10, 5, 1, 9, 0, 4, 7, 2, 8]


class Stats:
    def __init__(self):
        self.comparisons = 0
        self.swaps = 0
        self.partitions = 0
        self.max_depth = 0


def choose_pivot(arr, l, r, mode):
    if mode == "first":
        return l
    elif mode == "middle":
        return (l + r) // 2
    elif mode == "random":
        return random.randint(l, r)


def partition_hoare(arr, l, r, stats, pivot_mode, log, depth):
    stats.partitions += 1

    pivot_index = choose_pivot(arr, l, r, pivot_mode)
    pivot = arr[pivot_index]

    i = l - 1
    j = r + 1

    while True:
        while True:
            i += 1
            stats.comparisons += 1
            if arr[i] >= pivot:
                break

        while True:
            j -= 1
            stats.comparisons += 1
            if arr[j] <= pivot:
                break

        if i >= j:
            if len(log) < 3:
                log.append((l, r, pivot, arr[l:r+1].copy(), j))
            return j

        arr[i], arr[j] = arr[j], arr[i]
        stats.swaps += 1


def partition_lomuto(arr, l, r, stats, pivot_mode, log, depth):
    stats.partitions += 1

    pivot_index = choose_pivot(arr, l, r, pivot_mode)
    arr[pivot_index], arr[r] = arr[r], arr[pivot_index]
    stats.swaps += 1

    pivot = arr[r]
    i = l - 1

    for j in range(l, r):
        stats.comparisons += 1
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            stats.swaps += 1

    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    stats.swaps += 1

    if len(log) < 3:
        log.append((l, r, pivot, arr[l:r+1].copy(), i+1))

    return i + 1


def quicksort(arr, l, r, stats, scheme, pivot_mode, depth=1, log=[]):
    stats.max_depth = max(stats.max_depth, depth)

    if l >= r:
        return

    if scheme == "hoare":
        p = partition_hoare(arr, l, r, stats, pivot_mode, log, depth)
        quicksort(arr, l, p, stats, scheme, pivot_mode, depth + 1, log)
        quicksort(arr, p + 1, r, stats, scheme, pivot_mode, depth + 1, log)

    else:  # lomuto
        p = partition_lomuto(arr, l, r, stats, pivot_mode, log, depth)
        quicksort(arr, l, p - 1, stats, scheme, pivot_mode, depth + 1, log)
        quicksort(arr, p + 1, r, stats, scheme, pivot_mode, depth + 1, log)


def run_test(arr):
    for scheme in ["hoare", "lomuto"]:
        for pivot_mode in ["first", "middle", "random"]:
            data = arr[:]
            stats = Stats()
            log = []

            quicksort(data, 0, len(data) - 1, stats, scheme, pivot_mode, log=log)

            print(f"\nСхема: {scheme}, pivot: {pivot_mode}")
            print("Отсортированный:", data)

            print("Сравнения:", stats.comparisons)
            print("Обмены:", stats.swaps)
            print("Разбиения:", stats.partitions)
            print("Глубина рекурсии:", stats.max_depth)

            print("Первые 3 разбиения:")
            for step in log:
                l, r, pivot, subarr, res = step
                print(f"[{l}, {r}], pivot={pivot}, результат={subarr[:30]}..., return={res}")


print("===== СЛУЧАЙНЫЙ МАССИВ =====")
run_test(orders_random)

print("\n===== МАССИВ С ДУБЛИКАТАМИ =====")
run_test(orders_many_duplicates)