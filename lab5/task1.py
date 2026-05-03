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


def selection_sort(arr): #сравнений всегда много, обменов мало
    a = arr.copy()
    n = len(a)
    comparisons = 0
    swaps = 0
    passes = 0

    for i in range(n):
        passes += 1
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_index]:
                min_index = j

        if min_index != i:
            a[i], a[min_index] = a[min_index], a[i]
            swaps += 1

    return a, comparisons, swaps, passes


def insertion_sort(arr): #быстрая на почти отсортированном
    a = arr.copy()
    comparisons = 0
    shifts = 0
    passes = 0

    for i in range(1, len(a)):
        passes += 1
        key = a[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break

        a[j + 1] = key

    return a, comparisons, shifts, passes


def test_all(data):
    print("\nИсходный массив:", data)

    res = bubble_sort(data)
    print("\nПузырьковая сортировка:")
    print("Отсортированный массив:", res[0])
    print("Сравнения:", res[1])
    print("Обмены:", res[2])
    print("Проходы:", res[3])

    res = selection_sort(data)
    print("\nСортировка выбором:")
    print("Отсортированный массив:", res[0])
    print("Сравнения:", res[1])
    print("Обмены:", res[2])
    print("Проходы:", res[3])

    res = insertion_sort(data)
    print("\nСортировка вставками:")
    print("Отсортированный массив:", res[0])
    print("Сравнения:", res[1])
    print("Сдвиги:", res[2])
    print("Проходы:", res[3])


data_random = [57, 12, 89, 34, 76, 11, 90, 43, 65, 28, 71, 5, 39, 84, 22]
data_sorted = [5, 11, 12, 22, 28, 34, 39, 43, 57, 65, 71, 76, 84, 89, 90]
data_reverse = [90, 89, 84, 76, 71, 65, 57, 43, 39, 34, 28, 22, 12, 11, 5]
data_almost_sorted = [5, 11, 12, 22, 28, 34, 43, 39, 57, 65, 71, 76, 84, 89, 90]

datasets = [
    ("Случайный", data_random),
    ("Отсортированный", data_sorted),
    ("Обратный", data_reverse),
    ("Почти отсортированный", data_almost_sorted)
]

for name, data in datasets:
    print(f"\n===== {name} массив =====")
    test_all(data)