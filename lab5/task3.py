cargo_priority = [42, 17, 93, 58, 11, 76, 24, 65, 39, 88, 5, 71, 30, 54, 19, 93,
                  7, 80, 80, 48, 77, 98, 97, 56, 27, 94, 73, 74, 72, 47, 95, 70,
                  96, 93, 84, 53, 38, 90, 94, 85, 34, 88, 56, 29, 65, 84, 72, 60,
                  63, 59, 61, 61, 14, 42, 89, 97, 62, 27, 19, 36, 18, 89, 3, 64,
                  99, 38, 26, 99, 55, 40, 32, 99, 86, 44, 1, 100, 53, 74, 78, 68,
                  21, 24, 85, 32, 99, 68, 85, 12, 4, 18, 69, 46, 46, 50, 64, 7,
                  68, 27, 98, 77, 41, 76, 12, 12, 62, 75, 29, 52, 12, 91, 73, 14,
                  22, 47, 47, 16, 25, 64, 54, 66, 89, 20, 68, 82, 4, 7, 58, 42,
                  13, 3, 60, 10, 52, 25, 98, 64, 86, 48, 44, 38, 2, 33, 14, 28,
                  29, 40, 23, 83, 47, 35]

comparison_count = 0
max_recursion_depth = 0


def merge(sequence, support, ls, le, rs, re):
    global comparison_count

    for i in range(ls, re + 1):
        support[i] = sequence[i]

    l, r = ls, rs

    for i in range(ls, re + 1):
        if l > le:
            sequence[i] = support[r]
            r += 1
        elif r > re:
            sequence[i] = support[l]
            l += 1
        else:
            comparison_count += 1
            if support[l] < support[r]:
                sequence[i] = support[l]
                l += 1
            else:
                sequence[i] = support[r]
                r += 1

def merge_sort_recursive(sequence, support=None, start_index=None, stop_index=None, depth=1):
    global max_recursion_depth

    if support is None:
        support = sequence[:]
    if start_index is None:
        start_index = 0
    if stop_index is None:
        stop_index = len(sequence) - 1

    if stop_index <= start_index:
        return

    max_recursion_depth = max(max_recursion_depth, depth)
    mid = start_index + (stop_index - start_index) // 2

    merge_sort_recursive(sequence, support, start_index, mid, depth + 1)
    merge_sort_recursive(sequence, support, mid + 1, stop_index, depth + 1)
    merge(sequence, support, start_index, mid, mid + 1, stop_index)


# Итерационный вариант сортировки слиянием
def merge_sort_iterative(sequence):
    global comparison_count
    n = len(sequence)
    support = sequence[:]
    size = 1
    passes = 0

    while size < n:
        passes += 1
        j = 0
        while j < n - size:
            ls = j
            le = j + size - 1
            rs = j + size
            re = min(j + 2*size - 1, n - 1)
            merge(sequence, support, ls, le, rs, re)
            j += 2*size
        size *= 2
    return passes


print("Исходный массив (рекурсивный):")
print(cargo_priority)

sorted_recursive = cargo_priority[:]
merge_sort_recursive(sorted_recursive)

print("\nОтсортированный массив (рекурсивный):")
print(sorted_recursive)
print("Число сравнений:", comparison_count)
print("Максимальная глубина рекурсии:", max_recursion_depth)


comparison_count = 0
sorted_iterative = cargo_priority[:]
passes = merge_sort_iterative(sorted_iterative)

print("\nОтсортированный массив (итерационный):")
print(sorted_iterative)
print("Число сравнений:", comparison_count)
print("Число проходов:", passes)