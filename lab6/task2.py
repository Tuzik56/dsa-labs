class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  # Добавили указатель на последний узел
        self.size = 0

    def add_first(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

        if self.tail is None:
            self.tail = new_node

        self.size += 1

    def add_last(self, value):
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
            raise IndexError("Попытка удаления из пустого списка")

        self.head = self.head.next
        self.size -= 1

        if self.head is None:
            self.tail = None

    def remove_last(self):
        if self.head is None:
            raise IndexError("Попытка удаления из пустого списка")

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            current = self.head

            while current.next.next is not None:
                current = current.next

            current.next = None
            self.tail = current

        self.size -= 1

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Индекс вне диапазона")

        current = self.head

        for i in range(index):
            current = current.next

        return current.data

    def get_size(self):
        return self.size

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