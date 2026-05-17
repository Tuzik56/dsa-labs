import time


# ДИНАМИЧЕСКИЙ МАССИВ =========================
class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.data = [0] * self.capacity

    def resize(self):
        self.capacity *= 2
        new_data = [0] * self.capacity
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data = new_data

    def append(self, value):
        if self.size >= self.capacity:
            self.resize()
        self.data[self.size] = value
        self.size += 1

    def remove_first(self):
        if self.size == 0:
            return
        for i in range(self.size - 1):
            self.data[i] = self.data[i + 1]
        self.size -= 1

    def get(self, index):
        return self.data[index]

    def get_size(self):
        return self.size


# ОДНОСВЯЗНЫЙ СПИСОК ==========================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def remove_first(self):
        if self.head is None:
            return
        self.head = self.head.next
        self.size -= 1
        if self.head is None:
            self.tail = None

    def get(self, index):
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def get_size(self):
        return self.size


# ========================================================================

sizes = [10 ** 2, 10 ** 3, 10 ** 4]
trials = 100

print("-" * 110)
print(f"{'N':<10}{'Структура':<20}{'append':<20}{'remove_first':<20}{'get':<20}{'size':<20}")
print("-" * 110)

for N in sizes:

    # append
    append_time_total = 0
    for _ in range(trials):
        temp = DynamicArray()
        for i in range(N):
            temp.append(i)

        start = time.perf_counter()
        temp.append(0)
        append_time_total += (time.perf_counter() - start)
    arr_append_time = append_time_total / trials

    # remove_first
    remove_time_total = 0
    for _ in range(trials):
        temp = DynamicArray()
        for i in range(N):
            temp.append(i)

        start = time.perf_counter()
        temp.remove_first()
        remove_time_total += (time.perf_counter() - start)
    arr_remove_time = remove_time_total / trials

    arr = DynamicArray()
    for i in range(N):
        arr.append(i)

    # get
    start = time.perf_counter()
    for _ in range(trials):
        arr.get(N // 2)
    arr_get_time = (time.perf_counter() - start) / trials

    # size
    start = time.perf_counter()
    for _ in range(trials):
        arr.get_size()
    arr_size_time = (time.perf_counter() - start) / trials

    print(f"{N:<10}{'Массив':<20}"
          f"{arr_append_time:<20.8f}"
          f"{arr_remove_time:<20.8f}"
          f"{arr_get_time:<20.8f}"
          f"{arr_size_time:<20.8f}")

    # ====================================================================

    # append
    append_time_total = 0
    for _ in range(trials):
        temp = LinkedList()
        for i in range(N):
            temp.append(i)

        start = time.perf_counter()
        temp.append(999)
        append_time_total += (time.perf_counter() - start)
    lst_append_time = append_time_total / trials

    # remove_first
    remove_time_total = 0
    for _ in range(trials):
        temp = LinkedList()
        for i in range(N):
            temp.append(i)

        start = time.perf_counter()
        temp.remove_first()
        remove_time_total += (time.perf_counter() - start)
    lst_remove_time = remove_time_total / trials

    lst = LinkedList()
    for i in range(N):
        lst.append(i)

    # get
    start = time.perf_counter()
    for _ in range(trials):
        lst.get(N // 2)
    lst_get_time = (time.perf_counter() - start) / trials

    # size
    start = time.perf_counter()
    for _ in range(trials):
        lst.get_size()
    lst_size_time = (time.perf_counter() - start) / trials

    print(f"{N:<10}{'Связный список':<20}"
          f"{lst_append_time:<20.8f}"
          f"{lst_remove_time:<20.8f}"
          f"{lst_get_time:<20.8f}"
          f"{lst_size_time:<20.8f}")

    print("-" * 110)
