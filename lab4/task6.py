import time
from matplotlib import pyplot as plt
from task1 import linear_search, binary_search, interpolation_search, exponential_search


def measure_search_time(search_func, sequence, element, trials):
    start = time.time()

    for _ in range(trials):
        search_func(sequence, element)

    end = time.time()
    return (end - start) / trials


def test_searches():
    powers = [3, 4, 5, 6] 
    trials = 100
    funcs = [linear_search, binary_search, interpolation_search, exponential_search]
    names = ["Linear", "Binary", "Interpolation", "Exponential"]

    times = {name: [] for name in names}

    for func, name in zip(funcs, names):
        for power in powers:
            sequence = list(range(1, 10 ** power + 1))
            elements = [sequence[power // 10], sequence[power // 5], sequence[power // 2], sequence[power - 1]]
            avg_time = []

            for element in elements:
                avg_time.append(measure_search_time(func, sequence, element, trials))

            times[name].append(sum(avg_time) / len(elements)) 

    for name in names:
        plt.plot(powers, times[name], label=name)

    plt.xlabel("Размер массива (N) = 10^k")
    plt.ylabel("Среднее время поиска (ms)")
    plt.legend()
    plt.show()


test_searches()