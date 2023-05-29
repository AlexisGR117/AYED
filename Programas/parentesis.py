# Nombre: Jefer Alexis Gonzalez Romero
# Carne: 2171737
# Identificacion: 1000046442
# CC: 1003618876


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

    def insert_head(self, element):
        if element is not None:
            new_node = Node(element)
            if self.is_empty():
                self.head = new_node
                self.tail = new_node
            else:
                current = self.head
                current.set_prev(new_node)
                new_node.set_next(current)
                self.head = new_node

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


class Stack:

    def __init__(self, data=[]):
        self.data = DoubleLinkedList()
        for dat in data:
            self.push(dat)

    def push(self, new_value):
        self.data.insert_head(new_value)

    def pop(self):
        current = self.data.head
        if not self.data.is_empty():
            return self.data.delete_element(current.get_value()).get_value()
        return None

    def __str__(self):
        return str(self.data)


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


def parentesis(cadena):
    lst = Stack()
    for i in cadena:
        if i == "(" or i == "[":
            lst.push(i)
        elif i == ")" or i == "]":
            anterior = lst.data.head
            if anterior is None:
                return 2
            else:
                anterior = anterior.get_value()
                if (anterior == "(" and i == ")") or (anterior == "[" and i == "]"):
                    lst.pop()
                else:
                    return 2
    if lst.data.is_empty():
        return 1
    else:
        return 2


def main():
    cases = int(stdin.readline().strip())
    for i in range(cases):
        cadena = stdin.readline().strip()
        rta = parentesis(cadena)
        if rta == 1:
            print("Yes")
        else:
            print("No")

main()
