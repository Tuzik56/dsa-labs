import time
import numpy as np
from task1 import exponential_search


def index_search(sequence, element):
    result = sequence.index(element)
    return result


def np_search(sequence, element):
    result = np.searchsorted(sequence, element)
    return result


def measure_search_time(search_func, sequence, element, trials):
    start = time.time()

    for _ in range(trials):
        search_func(sequence, element)

    end = time.time()
    return (end - start) / trials


def format_time(seconds):
    return f"{seconds * 1000:.6f} ms"


def test_searches():
    sequence = list(range(1, 1001))
    elements = [1, 100, 500, 1000]
    trials = 200

    print(f"{'Алгоритм':<20}{'Элемент':<10}{'Время':<10}")
    print("-" * 55)

    for element in elements:
        exponential_search_time = measure_search_time(exponential_search, sequence, element, trials)
        print(f"{'Exponential':<20}{element:<10}{format_time(exponential_search_time):<10}")

        index_search_time = measure_search_time(index_search, sequence, element, trials)
        print(f"{'Index':<20}{element:<10}{format_time(index_search_time):<10}")

        np_search_time = measure_search_time(np_search, np.array(sequence), element, trials)
        print(f"{'NumPy':<20}{element:<10}{format_time(np_search_time):<10}")

        print("-" * 55)

test_searches()