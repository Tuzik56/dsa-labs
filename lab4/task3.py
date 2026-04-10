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


def generate_array(n):
    arr = random.sample(range(0, 10000), n)

    return arr


def measure_search_time(sort, search_func, arr, k, *args):
    start = time.time()

    if sort:
        arr = quick_sort(arr)

    for i in range(k):
        search_func(arr, random.choice(arr), *args)
    end = time.time()

    return end - start


def test_searches(arr, requests):
    linear_search_time = {}
    binary_search_time = {}

    for request in requests:
        linear_search_time[request] = measure_search_time(False, linear_search, arr, request)
        binary_search_time[request] = measure_search_time(True, binary_search, arr, request, 0, len(arr))

    plt.plot(linear_search_time.keys(), linear_search_time.values())
    plt.plot(binary_search_time.keys(), binary_search_time.values())
    plt.xlabel("Число запросов")
    plt.ylabel("Время выполнения (сек)")
    plt.legend(["Linear total", "Sort + Binary total"])
    plt.show()

test_searches(generate_array(10000), [10, 30, 50, 70, 100, 200])
