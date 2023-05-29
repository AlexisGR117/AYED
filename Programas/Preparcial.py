# Escribir un programa usando la estructura de datos de pila, en donde puedas añadir una lista de tareas,
# y puedas ir quitando las tareas según las terminas.
from sys import stdin
class Stack:

    def __init__(self, elements=[]):
        self.head = None
        self.tail = None
        for e in elements:
            self.anadir_tarea(e)

    def __str__(self):
        if self.is_empty():
            return "[]"
        else:

            return "[" + str(self.tail) + "]"

    def anadir_tarea(self, nueva_tarea):
        if nueva_tarea is not None:
            new_node = Node(nueva_tarea)
            if self.is_empty():
                self.head = new_node
                self.tail = new_node
            else:
                current = self.head
                current.set_next(new_node)
                self.head = new_node

    def quitar_tarea(self):
        if not self.is_empty():
            current = self.tail

            while current is not None and current.get_next() != self.head:
                print(current)
                current = current.get_next()
            if current is not None:
                current.set_next(None)
                self.head = current
            else:
                self.tail = None


    def is_empty(self):
        return self.tail == None


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

    def clear(self):
        self.set_next(None)

def main():
    tareas = [1]
    tareas = Stack(tareas)
    print(tareas)
    tareas.anadir_tarea(6)
    print(tareas)
    tareas.quitar_tarea()
    print(tareas)
    tareas.quitar_tarea()
    print(tareas)
    tareas.quitar_tarea()
    print(tareas)

main()
