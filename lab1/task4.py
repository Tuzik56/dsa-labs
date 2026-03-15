import random
import time
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


sizes = [1000, 2000, 5000, 10000]

bubble_times = []
python_times = []

for n in sizes:
    arr = [random.randint(0, 10000) for _ in range(n)]

    # Пузырёк
    start = time.perf_counter()
    bubble_sort(arr.copy())
    end = time.perf_counter()
    bubble_times.append(end - start)

    # Встроенная сортировка
    start = time.perf_counter()
    sorted(arr.copy())
    end = time.perf_counter()
    python_times.append(end - start)


plt.plot(sizes, bubble_times)
plt.plot(sizes, python_times)

plt.xlabel("n")
plt.ylabel("Time")
plt.title("O(n^2) vs O(n log n)")
plt.legend(["Bubble Sort", "Python sorted()"])

plt.show()