import random
import time
import matplotlib.pyplot as plt


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


sizes = [100, 200, 400, 800, 1600, 3200]
average_times = []

for n in sizes:
    total_time = 0

    for _ in range(5):
        arr = [random.randint(0, 10000) for _ in range(n)]

        start = time.perf_counter()
        bubble_sort(arr)
        end = time.perf_counter()

        total_time += (end - start)

    average_times.append(total_time)

plt.plot(sizes, average_times)
plt.xlabel("n")
plt.ylabel("Time")
plt.title("Bubble Sort")
plt.show()

n_squared = [n**2 for n in sizes]

plt.plot(n_squared, average_times)
plt.xlabel("n^2")
plt.ylabel("Time")
plt.title("Bubble Sort")
plt.show()