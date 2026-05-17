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

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Индекс вне диапазона")

        if self.size >= self.capacity:
            self.resize()

        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Индекс вне диапазона")

        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.size -= 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Индекс вне диапазона")

        return self.data[index]

    def get_size(self):
        return self.size

    def print_array(self):
        print(self.data[:self.size])


arr = DynamicArray()
values = [5, 0, 1, 7, 9, 4, 6, 2, 1]

for value in values:
    arr.append(value)

arr.insert(7, 8)

arr.delete(5)

arr.print_array()
print("Размер списка:", arr.get_size())