# Узел списка
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Односвязный список
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # добавление в начало
    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    # добавление в конец
    def add_last(self, value):
        new_node = Node(value)

        # если список пуст
        if self.head is None:
            self.head = new_node
        else:
            current = self.head

            # идем до последнего узла
            while current.next is not None:
                current = current.next

            current.next = new_node

        self.size += 1

    # удаление первого элемента
    def remove_first(self):
        if self.head is None:
            print("Список пуст")
            return

        self.head = self.head.next
        self.size -= 1

    # удаление последнего элемента
    def remove_last(self):
        if self.head is None:
            print("Список пуст")
            return

        # если в списке один элемент
        if self.head.next is None:
            self.head = None
        else:
            current = self.head

            # идем до предпоследнего узла
            while current.next.next is not None:
                current = current.next

            current.next = None

        self.size -= 1

    # получение элемента по индексу
    def get(self, index):
        if index < 0 or index >= self.size:
            print("Ошибка: неверный индекс")
            return None

        current = self.head

        for i in range(index):
            current = current.next

        return current.data

    # получение размера списка
    def get_size(self):
        return self.size

    # вывод списка
    def print_list(self):
        current = self.head

        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print()


lst = SinglyLinkedList()

lst.add_last(5)
lst.add_last(3)
lst.add_last(5)
lst.add_last(20)
lst.add_last(7)

lst.remove_first()

lst.remove_last()

lst.print_list()
print("Размер списка:", lst.get_size())