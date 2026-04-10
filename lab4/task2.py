import matplotlib.pyplot as plt
import random
import time
from lab4.task1 import exponential_search

def generate_arrays(n):
    arr_uniform = [i * 10 for i in range(n)]
    arr_quadratic = [i ** 2 for i in range(n)]
    arr_exponential = [int(1.2 ** i) for i in range(n)]
    arr_random = random.sample(range(0, 10000), n)
    arr_random.sort()

    return {"Равномерное": arr_uniform,
            "Квадратичное": arr_quadratic,
            "Экспоненциальное": arr_exponential,
            "Случайное": arr_random}

def measure_search_time(search_func, arr, trials=100):
    times = []
    for _ in range(trials):
        start = time.time()
        search_func(arr, random.choice(arr))
        end = time.time()
        times.append(end - start)
    return sum(times) / trials

def test_search_times(n):
    arrays = generate_arrays(n)
    results = {}
    for name, arr in arrays.items():
        average_time = measure_search_time(exponential_search, arr)
        results[name] = average_time
    return results

results = test_search_times(2000)
print(results)

plt.bar(results.keys(), results.values(), color=['blue', 'green', 'red', 'orange'])
plt.ylabel("Среднее время поиска (сек)")
plt.show()