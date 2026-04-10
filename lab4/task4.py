def linear_search(sequence, element):
    comparison_count = 0
    iteration_count = 0
    shift_count = 0

    sequence.append(element)
    i = 0

    while True:
        comparison_count += 1

        if sequence[i] == element:
            break

        iteration_count += 1
        i += 1
        shift_count += 1

    sequence.pop()

    if i == len(sequence):
        return -1, comparison_count, iteration_count, shift_count

    return i, comparison_count, iteration_count, shift_count


def binary_search(sequence, required_element, start, end):
    comparison_count = 0
    iteration_count = 0
    shift_count = 0

    while start <= end:
        iteration_count += 1

        median = (start + end) // 2
        element = sequence[median]

        comparison_count += 1
        if element == required_element:
            return median, comparison_count, iteration_count, shift_count

        comparison_count += 1
        if element < required_element:
            start = median + 1
            shift_count += 1
        else:
            end = median - 1
            shift_count += 1

    return -1, comparison_count, iteration_count, shift_count


def interpolation_search(sequence, element):
    comparison_count = 0
    iteration_count = 0
    shift_count = 0

    left = 0
    right = len(sequence) - 1

    while True:
        comparison_count += 2
        if not (left <= right and sequence[left] <= element <= sequence[right]):
            break

        iteration_count += 1

        comparison_count += 1
        if sequence[left] == sequence[right]:
            comparison_count += 1
            if sequence[left] == element:
                return left, comparison_count, iteration_count, shift_count
            return -1, comparison_count, iteration_count, shift_count

        pos = left + (element - sequence[left]) * (right - left) // (sequence[right] - sequence[left])

        comparison_count += 1
        if sequence[pos] == element:
            return pos, comparison_count, iteration_count, shift_count

        comparison_count += 1
        if sequence[pos] < element:
            left = pos + 1
            shift_count += 1
        else:
            right = pos - 1
            shift_count += 1

    return -1, comparison_count, iteration_count, shift_count


def exponential_search(sequence, element):
    comparison_count = 0
    iteration_count = 0
    shift_count = 0

    border = 1
    length = len(sequence) - 1

    while border < length:
        comparison_count += 1
        if sequence[border] >= element:
            break

        iteration_count += 1
        border *= 2
        shift_count += 1

    if border > length:
        border = length

    result, c2, i2, s2 = binary_search(sequence, element, border // 2, border)

    comparison_count += c2
    iteration_count += i2
    shift_count += s2

    return result, comparison_count, iteration_count, shift_count


def test_searches():
    arr = list(range(1, 101))
    elements = [1, 50, 100, 150]

    print(f"{'Алгоритм':<20}{'Элемент':<10}{'Индекс':<10}{'Сравнения':<15}{'Итерации':<15}{'Сдвиги':<10}")
    print("-" * 80)

    for element in elements:
        res = linear_search(arr.copy(), element)
        print(f"{'Linear':<20}{element:<10}{res[0]:<10}{res[1]:<15}{res[2]:<15}{res[3]:<10}")

        res = binary_search(arr, element, 0, len(arr)-1)
        print(f"{'Binary':<20}{element:<10}{res[0]:<10}{res[1]:<15}{res[2]:<15}{res[3]:<10}")

        res = interpolation_search(arr, element)
        print(f"{'Interpolation':<20}{element:<10}{res[0]:<10}{res[1]:<15}{res[2]:<15}{res[3]:<10}")

        res = exponential_search(arr, element)
        print(f"{'Exponential':<20}{element:<10}{res[0]:<10}{res[1]:<15}{res[2]:<15}{res[3]:<10}")

        print("-" * 80)


test_searches()