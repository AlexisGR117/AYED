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
        """
        Funcion que dado un elemento cualquiera, lo inserta despues del tail
        que tiene la lista, colocandolo como previo el tail
        (LinkedList, any) -> None
        """
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
        """
        Funcion que dado un elemento cualquiera, si esta en la lista enlazada doble
        se devuelve el nodo que se encontro con este valor
        (LinkedList, any) -> (Node)
        """
        if self.is_empty():
            return None
        else:
            current = self.head
            while current is not None and current.get_value() != value:
                current = current.get_next()
            return current

    def delete_element(self, element):
        """
        Funcion que dado un elemento cualquiera, si esta en la lista enlazada doble se elimina de esta
        (LinkedList, any) -> (Node)
        """
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
        """
        Funcion que da el nodo previo
        (Node) -> (Node)
        """
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
        """
        Funcion que actualiza el nodo previo
        (Node, Node) -> None
        """
        if isinstance(new_prev, Node) or new_prev is None:
            self.prev = new_prev
        else:
            raise 'Error en actualización del Nodo'

    def clear(self):
        self.set_next(None)
        self.set_prev(None)


def main():
    print("Inserte los elementos de la lista separados por un espacio:")
    lista = stdin.readline().strip().split()
    lista = DoubleLinkedList(lista)
    print("Ingrese un elemento que este en la lista:")
    elemento = stdin.readline().strip()
    current = lista.search(elemento)
    anterior = current.get_prev()
    if anterior is not None:
        print("El valor del nodo que esta previo al elemento es:\n" + anterior.get_value())
    else:
        print("El valor del nodo que esta previo al elemento es:\n" + str(anterior))
    current.set_prev(Node('9'))
    print("Despues de usar la funcion set_prev('9') al elemento, el nuevo valor del nodo que esta previo a este es:\n" + current.get_prev().get_value())
    current.set_prev(anterior)
    lista.insert('16')
    print("la lista al insertarle el elemento '16':\n" + str(lista))
    lista.delete_element(current.get_value())
    print("Si le quitamos el elemento dado:\n" + str(lista))
    lista.delete_element(lista.head.get_value())
    print("Despues de eliminarle el que estaba en la cabeza:\n" + str(lista))
    lista.delete_element(lista.tail.get_value())
    print("Y por último sin el que esta en la cola:\n" + str(lista))


main()
