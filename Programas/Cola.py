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

    def invert(self):
        current = self.head
        self.tail = current
        anterior = None
        while current is not None and current.get_next() is not None:
            proximo = current.get_next()
            current.set_next(anterior)
            current.set_prev(proximo)
            anterior = current
            current = proximo
        current.set_next(anterior)
        self.head = current

        return current

    def delete_duplicate(self):
        self.invert()
        current = self.head
        elementos = []
        while current is not None:
            if current.get_value() not in elementos:
                elementos.append(current.get_value())
            else:
                self.delete_element(current.get_value())
            current = current.get_next()
        self.invert()

    def unir(self, lista2):
        head2 = lista2.head
        tail1 = self.tail
        tail2 = lista2.tail
        head2.set_prev(tail1)
        tail1.set_next(head2)
        self.tail = tail2

# LIFO
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
        if self.data.is_empty():
            return ""
        else:
            current = self.data.head
            texto = ""
            while current.get_next() is not None:
                texto += current.get_value() + "\n"
                current = current.get_next()
            texto += current.get_value()
            return texto


class Queue:

    def __init__(self, data=[]):
        self.lifo = Stack()
        self.fifo = Stack()
        for dat in data:
            self.enqueue(dat)

    def enqueue(self, new_value):
        self.lifo.push(new_value)
        current = self.lifo.data.head
        self.fifo = Stack()
        while current is not None:
            self.fifo.push(current.get_value())
            current = current.get_next()

    def dequeue(self):
        if not self.fifo.data.is_empty():
            self.fifo.pop()
            self.lifo = Stack()
            current = self.fifo.data.head
            while current is not None:
                self.lifo.push(current.get_value())
                current = current.get_next()

    def __str__(self):
        current = self.fifo.data.head
        texto = ""
        while current is not None and current.get_next() is not None:
            texto += current.get_value() + " --> "
            current = current.get_next()
        if current is not None:
            texto += current.get_value()
        return texto


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


def main():
    print("==================Simulacion para uso de la estructura lineal Pila==================\n")
    print("Tenemos unos libros de estudio apilados de la siguiente manera:\n")
    libros = []
    libros.append("Calculo")
    libros.append("Ingles")
    libros.append("Historia")
    libros.append("Quimica")
    libros.append("Fisica")
    pila = Stack(libros)
    print(pila, "\n")
    print("Si apilamos el libro de programacion queda:\n")
    pila.push("Programacion")
    print(pila, "\n")
    print("Por ultimo, al sacar 3 libros:\n")
    for i in range(3):
        pila.pop()
    print(pila, "\n")
    print("==================Simulacion para uso de la estructura lineal Cola==================\n")
    print("Unos amigos hacen una fila para el cine, estan ubicados de la siguiente forma:\n")
    amigos = []
    amigos.append("Natalia")
    amigos.append("Juan")
    amigos.append("Martha")
    amigos.append("Laura")
    amigos.append("Sebastian")
    cola = Queue(amigos)
    print(cola, "\n")
    print("Su amigo Camilo acaba de llegar, así queda la fila:\n")
    cola.enqueue("Camilo")
    print(cola, "\n")
    print("Los cuatro primeros entran a la sala de cine, despues de esto la fila es:\n")
    for i in range(4):
        cola.dequeue()
    print(cola)

main()
