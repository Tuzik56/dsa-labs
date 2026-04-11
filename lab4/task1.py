def linear_search(sequence, element):
    sequence.append(element)
    i = 0

    while sequence[i] != element:
        i += 1

    sequence.pop()

    if i == len(sequence):
        return -1
    return i


def binary_search(sequence, required_element, start=0, end=None):
    if end is None:
        end = len(sequence) - 1

    while start <= end:
        median = (start + end) // 2
        element = sequence[median]

        if element == required_element:
            return median
        if element < required_element:
            start = median + 1
        else:
            end = median - 1
    return -1


def interpolation_search(sequence, element):
    left = 0
    right = len(sequence) - 1

    while left <= right and sequence[left] <= element <= sequence[right]:

        if sequence[left] == sequence[right]:
            if sequence[left] == element:
                return left
            return -1

        pos = left + (element - sequence[left]) * (right - left) // (sequence[right] - sequence[left])

        if sequence[pos] == element:
            return pos
        elif sequence[pos] < element:
            left = pos + 1
        else:
            right = pos - 1
    return -1


def exponential_search(sequence, element):
    border = 1
    length = len(sequence) - 1

    while border < length and sequence[border] < element:
        border *= 2

    if border > length:
        border = length
    return binary_search(sequence, element, border // 2, border)
