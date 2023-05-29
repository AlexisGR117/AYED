from sys import stdin


class LinkedList:

    def __init__(self, elements=[]):
        self.head = None
        for e in elements:
            self.insert(e)

    def __str__(self):
        if self.is_empty():
            return "[]"
        else:
            return "[" + str(self.head) + "]"

    def is_empty(self):
        return self.head == None

    def insert(self, element):
        new_node = Node(element)
        if element is not None:
            if self.is_empty():
                self.head = new_node
            else:
                current = self.head
                while current.get_next() is not None:
                    current = current.get_next()
                current.set_next(new_node)

    def search(self, value):
        if self.is_empty():
            return None
        else:
            current = self.head
            while current is not None and current.get_value() != value:
                current = current.get_next()
            return current
        
    def search_prev(self, value):
        if self.is_empty():
            return None
        else:
            current = self.head
            while current is not None and current.get_next() != value:
                current = current.get_next()
            return current

    def invert(self):
        current = self.head
        anterior = None
        while current is not None and current.get_next() is not None:
            proximo = current.get_next()
            current.set_next(anterior)
            anterior = current
            current = proximo
        current.set_next(anterior)
        self.head = current
        return current

    def delete_element(self, value):
        elemento = self.search(value)
        if elemento is not None:
            if elemento == self.head and elemento.get_next() is None:
                self.head = None
            elif elemento == self.head:
                self.head = elemento.get_next()
            elif elemento.get_next() is None:
                anterior = self.search_prev(elemento)
                anterior.set_next(None)
            else:
                anterior = self.search_prev(elemento)
                anterior.set_next(elemento.get_next())
                elemento.set_next(None)
            return elemento
        else:
            return None



class Node:

    def __init__(self, value, next=None):
        self.set_value(value)
        self.set_next(next)

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def __str__(self):
        return '(' + str(self.value) + ')' + ((' --> ' + str(self.next)) if self.next is not None else '')

    def set_value(self, new_value):
        self.value = new_value

    def set_next(self, new_next):
        if isinstance(new_next, Node) or new_next is None:
            self.next = new_next
        else:
            raise 'Error en actualización del Nodo'


def main():
    lista = stdin.readline().strip().split()
    valores = stdin.readline().strip().split()
    lista = LinkedList(lista)
    for i in valores:
        lista.delete_element(i)
    print(lista)    
    


main()
