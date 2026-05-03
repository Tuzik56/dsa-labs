# ---------------- ДАННЫЕ ----------------
records1 = [("A1", 4), ("A2", 2), ("A3", 4), ("A4", 1), ("A5", 3),
            ("A6", 2), ("A7", 4), ("A8", 1), ("A9", 3), ("A10", 2)]

records2 = [("B1", 5), ("B2", 5), ("B3", 5), ("B4", 2), ("B5", 2),
            ("B6", 3), ("B7", 3), ("B8", 3), ("B9", 1), ("B10", 1)]

records3 = [("C1", 3), ("C2", 1), ("C3", 3), ("C4", 2), ("C5", 3),
            ("C6", 1), ("C7", 2), ("C8", 3), ("C9", 1), ("C10", 2),
            ("C11", 3), ("C12", 1)]

# ---------------- СОРТИРОВКИ ----------------

# УСТОЙЧИВЫЕ

def bubble_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j][1] > a[j + 1][1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


def insertion_sort(arr):
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j][1] > key[1]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


# НЕУСТОЙЧИВЫЕ

def selection_sort(arr):
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j][1] < a[min_idx][1]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def quick_sort(arr):
    a = arr[:]

    def qs(l, r):
        if l >= r:
            return
        pivot = a[r][1]
        i = l - 1
        for j in range(l, r):
            if a[j][1] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
        a[i + 1], a[r] = a[r], a[i + 1]
        p = i + 1
        qs(l, p - 1)
        qs(p + 1, r)

    qs(0, len(a) - 1)
    return a


# ---------------- ПРОВЕРКА УСТОЙЧИВОСТИ ----------------

def is_stable(original, sorted_arr):
    from collections import defaultdict

    original_order = defaultdict(list)
    sorted_order = defaultdict(list)

    for id_, key in original:
        original_order[key].append(id_)

    for id_, key in sorted_arr:
        sorted_order[key].append(id_)

    return original_order == sorted_order


# ---------------- ЗАПУСК ----------------

algorithms = [
    ("Bubble (устойчивый)", bubble_sort),
    ("Insertion (устойчивый)", insertion_sort),
    ("Selection (неустойчивый)", selection_sort),
    ("Quick (неустойчивый)", quick_sort),
]


def run(records, name):
    print(f"\n===== {name} =====")
    print("Исходный:", records)

    for alg_name, func in algorithms:
        result = func(records)
        stable = is_stable(records, result)

        print(f"\n{alg_name}")
        print("Результат:", result)
        print("Сохранился порядок:", stable)


run(records1, "RECORDS 1")
run(records2, "RECORDS 2")
run(records3, "RECORDS 3")


# ---------------- МНОГОКРИТЕРИАЛЬНАЯ СОРТИРОВКА ----------------

def multi_sort(records):
    print("\n===== МНОГОКРИТЕРИАЛЬНАЯ СОРТИРОВКА =====")

    # 1. Сортируем по ID
    step1 = sorted(records, key=lambda x: x[0])
    print("После сортировки по ID:", step1)

    # 2. Устойчивая сортировка по ключу
    stable_result = insertion_sort(step1)

    # 3. Неустойчивая сортировка
    unstable_result = selection_sort(step1)

    print("\nУстойчивая сортировка по ключу:")
    print(stable_result)

    print("\nНеустойчивая сортировка по ключу:")
    print(unstable_result)


multi_sort(records1)