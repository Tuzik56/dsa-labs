import random
import time
from matplotlib import pyplot as plt
from task1 import linear_search, binary_search


def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[len(nums) // 2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def generate_sequence(n):
    sequence = random.sample(range(0, 10000), n)

    return sequence


def measure_search_time(sort, search_func, sequence, k, *args):
    start = time.time()

    if sort:
        sequence = quick_sort(sequence)

    for i in range(k):
        search_func(sequence, random.choice(sequence), *args)
    end = time.time()

    return end - start


def test_searches(sequence, requests):
    linear_search_time = {}
    binary_search_time = {}

    for request in requests:
        linear_search_time[request] = measure_search_time(False, linear_search, sequence, request)
        binary_search_time[request] = measure_search_time(True, binary_search, sequence, request, 0, len(sequence))

    plt.plot(linear_search_time.keys(), linear_search_time.values())
    plt.plot(binary_search_time.keys(), binary_search_time.values())
    plt.xlabel("Число запросов")
    plt.ylabel("Время выполнения (сек)")
    plt.legend(["Linear total", "Sort + Binary total"])
    plt.show()

test_searches(generate_sequence(10000), [10, 30, 50, 70, 100, 200])
