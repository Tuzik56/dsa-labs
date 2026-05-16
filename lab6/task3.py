# Узел списка
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Стек на основе односвязного списка
class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    # push — добавление в стек
    def push(self, value):
        new_node = Node(value)

        new_node.next = self.head
        self.head = new_node

        self.count += 1

    # pop — удаление верхнего элемента
    def pop(self):
        if self.head is None:
            print("Стек пуст")
            return None

        value = self.head.data
        self.head = self.head.next

        self.count -= 1

        return value

    # peek — просмотр верхнего элемента
    def peek(self):
        if self.head is None:
            print("Стек пуст")
            return None

        return self.head.data

    # size — количество элементов
    def size(self):
        return self.count

    # вывод стека
    def print_stack(self):
        current = self.head

        print("Содержимое стека:", end=" ")

        while current is not None:
            print(current.data, end=" ")
            current = current.next

        print()


stack = Stack()

stack.push(5)
stack.push(0)
stack.push(1)
stack.push(7)
stack.push(9)

print("Верхний элемент:", stack.peek())
print("Удален элемент:", stack.pop())
print("Удален элемент:", stack.pop())
print("Новый верхний элемент:", stack.peek())
print("Размер стека:", stack.size())

stack.print_stack()