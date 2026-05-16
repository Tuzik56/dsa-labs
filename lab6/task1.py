class DynamicArray:
    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.data = [0] * self.capacity

    # увеличение массива в 2 раза
    def resize(self):
        self.capacity *= 2
        new_data = [0] * self.capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data

    # добавление в конец
    def append(self, value):
        if self.size >= self.capacity:
            self.resize()

        self.data[self.size] = value
        self.size += 1

    # вставка по индексу
    def insert(self, index, value):
        if index < 0 or index > self.size:
            print("Ошибка: неверный индекс")
            return

        if self.size >= self.capacity:
            self.resize()

        # сдвиг элементов вправо
        for i in range(self.size, index, -1):
            self.data[i] = self.data[i - 1]

        self.data[index] = value
        self.size += 1

    # удаление по индексу
    def delete(self, index):
        if index < 0 or index >= self.size:
            print("Ошибка: неверный индекс")
            return

        # сдвиг элементов влево
        for i in range(index, self.size - 1):
            self.data[i] = self.data[i + 1]

        self.size -= 1

    # получение элемента
    def get(self, index):
        if index < 0 or index >= self.size:
            print("Ошибка: неверный индекс")
            return None

        return self.data[index]

    # получение размера
    def get_size(self):
        return self.size

    # вывод массива
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