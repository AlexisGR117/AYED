from sys import stdin


class DoubleLinkedList:

    def __init__(self, elements=[]):
        self.head = None
        self.tail = None
        for e in elements:
            self.insert(e)

    def __str__(self):
        if self.is_empty():
            return "[]"
        else:
            return "[" + str(self.head) + "]"

    def is_empty(self):
        return self.head is None and self.tail is None

    def insert(self, element):
        if element is not None:
            new_node = Node(element)
            if self.is_empty():
                self.head = new_node
                self.tail = new_node
            else:
                current = self.tail
                current.set_next(new_node)
                new_node.set_prev(current)
                self.tail = new_node

    def search(self, value):
        if self.is_empty():
            return None
        else:
            current = self.head
            while current is not None and current.get_value() != value:
                current = current.get_next()
            return current

    def delete_element(self, element):
        to_delete = self.search(element)
        if to_delete is not None:
            if to_delete == self.head and to_delete == self.tail:
                self.head, self.tail = None, None
            elif to_delete == self.head:
                self.head = to_delete.get_next()
                if self.head is not None:
                    self.head.set_prev(None)
            elif to_delete == self.tail:
                self.tail = to_delete.get_prev()
                if self.tail is not None:
                    self.tail.set_next(None)
            else:
                current = to_delete.get_prev()
                to_maintain = to_delete.get_next()
                current.set_next(to_maintain)
                to_maintain.set_prev(current)
            to_delete.clear()
            return to_delete
        else:
            return None


class Node:

    def __init__(self, value, next=None, previous=None):
        self.set_value(value)
        self.set_next(next)
        self.set_prev(previous)

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def get_prev(self):
        return self.prev

    def __str__(self):
        return '(' + str(self.value) + ')' + ((' <--> ' + str(self.next)) if self.next is not None else '')

    def set_value(self, new_value):
        self.value = new_value

    def set_next(self, new_next):
        if isinstance(new_next, Node) or new_next is None:
            self.next = new_next
        else:
            raise 'Error en actualización del Nodo'

    def set_prev(self, new_prev):
        if isinstance(new_prev, Node) or new_prev is None:
            self.prev = new_prev
        else:
            raise 'Error en actualización del Nodo'

    def clear(self):
        self.set_next(None)
        self.set_prev(None)


class Queue:

    def __init__(self, data=[]):
        self.data = DoubleLinkedList()
        for dat in data:
            self.enqueue(dat)

    def enqueue(self, new_value):
        self.data.insert(new_value)

    def dequeue(self):
        if not self.data.is_empty():
            if self.data.head == self.data.tail:
                self.data.head, self.data.tail = None, None
            else:
                current = self.data.head
                self.data.head = current.get_next()
                if self.data.head is not None:
                    self.data.head.set_prev(None)
                current.clear()
                return self.data.head
        return None

    def __str__(self):
        current = self.data.head
        texto = ""
        while current is not None and current.get_next() is not None:
            texto += str(current.get_value()) + " --> "
            current = current.get_next()
        if current is not None:
            texto += str(current.get_value())
        return texto


def deque(mazo, discarded):
    while mazo.data.head.get_value() != mazo.data.tail.get_value():
        discarded += str(mazo.data.head.get_value()) + ", "
        mazo.dequeue()
        mazo.enqueue(mazo.data.head.get_value())
        mazo.dequeue()
    return discarded[:-2], mazo.data.head.get_value()


def main():
    cards = int(stdin.readline().strip())
    while cards != 0:
        mazo = Queue()
        for i in range(1, cards + 1):
            mazo.enqueue(i)
        discarded = deque(mazo, "")[0]
        remaining = deque(mazo, "")[1]
        print("Discarded cards:", discarded)
        print("Remaining card:", remaining)
        cards = int(stdin.readline().strip())


main()
