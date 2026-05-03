def bubble_sort(arr): #адаптивная
    a = arr.copy()
    n = len(a)
    comparisons = 0
    swaps = 0
    passes = 0

    for i in range(n):
        swapped = False
        passes += 1

        for j in range(0, n - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True

        if not swapped:
            break

    return a, comparisons, swaps, passes


def shaker_sort(arr):
    a = arr.copy()
    left = 0
    right = len(a) - 1

    comparisons = 0
    swaps = 0
    passes = 0

    while left < right:
        swapped = False
        passes += 1

        for i in range(left, right):
            comparisons += 1
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swaps += 1
                swapped = True
        right -= 1

        for i in range(right, left, -1):
            comparisons += 1
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]
                swaps += 1
                swapped = True
        left += 1

        if not swapped:
            break

    return a, comparisons, swaps, passes


def gnome_sort(arr):
    a = arr.copy()
    i = 1

    comparisons = 0
    swaps = 0
    steps = 0

    while i < len(a):
        steps += 1

        if i == 0:
            i += 1

        comparisons += 1
        if a[i] >= a[i - 1]:
            i += 1
        else:
            a[i], a[i - 1] = a[i - 1], a[i]
            swaps += 1
            i -= 1

    return a, comparisons, swaps, steps


def test_all(data):
    print("\nИсходный массив:", data)

    # Пузырьковая
    res = bubble_sort(data)
    print("\nПузырьковая сортировка:")
    print("Отсортированный:", res[0])
    print("Сравнения:", res[1])
    print("Перестановки:", res[2])
    print("Проходы:", res[3])

    # Перемешиванием
    res = shaker_sort(data)
    print("\nСортировка перемешиванием:")
    print("Отсортированный:", res[0])
    print("Сравнения:", res[1])
    print("Перестановки:", res[2])
    print("Проходы:", res[3])

    # Гномья
    res = gnome_sort(data)
    print("\nГномья сортировка:")
    print("Отсортированный:", res[0])
    print("Сравнения:", res[1])
    print("Перестановки:", res[2])
    print("Шаги:", res[3])


# Данные
data1 = [1, 2, 3, 4, 6, 5, 7, 8, 9, 10]
data2 = [2, 1, 3, 4, 5, 6, 7, 8, 10, 9]
data3 = [1, 3, 2, 4, 5, 7, 6, 8, 10, 9]
data4 = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]

datasets = [
    ("data1", data1),
    ("data2", data2),
    ("data3", data3),
    ("data4", data4)
]

for name, data in datasets:
    print(f"\n===== {name} =====")
    test_all(data)