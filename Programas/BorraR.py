class DoubleLinkedList:
    def __init__(self, elements=[]):
        self.head, self.tail = None, None        for e in elements:
            self.insert(e)
    def __str__(self):
        if self.isEmpty():
            return "[]"        else:
            return "["+ str(self.head) + "]"    def isEmpty(self):
        return self.head == None and self.tail == None    def insert(self, element):
        if element is not None:
            new_node = Node(element)
            if self.isEmpty():
                self.head = new_node                self.tail = new_node            else:
                #La actual Cola                current = self.tail                current.setNext(new_node)
                new_node.setPrev(current)
                self.tail = new_node    def insertHead(self, element):
        if element is not None:
            new_node = Node(element)
            if self.isEmpty():
                self.head = new_node                self.tail = new_node            else:
                # La actual Cabeza                current = self.head                current.setPrev(new_node)
                new_node.setNext(current)
                self.head = new_node    def search(self, value):
        if self.isEmpty():
            return None        else:
            current = self.head            while current is not None and current.getValue() != value:
                current = current.getNext()
            return current    def searchValue(self, value):
        node = self.search(value)
        if node is not None:
            return node.getValue()
        return node    def deleteElement(self, value):
        to_delete = self.search(value)
        if to_delete is not None:
            if to_delete == self.head and to_delete == self.tail:
                self.head, self.tail = None, None            elif to_delete == self.head:
                self.head = to_delete.getNext()
                if self.head is not None:
                    self.head.setPrev(None)
            elif to_delete == self.tail:
                self.tail = to_delete.getPrev()
                if self.tail is not None:
                    self.tail.setNext(None)
            else:
                current = to_delete.getPrev()
                to_maintain = to_delete.getNext()
                current.setNext(to_maintain)
                to_maintain.setPrev(current)
            to_delete.clear()
            return to_delete        else:
          return None#LIFOclass Stack:
    def __init__(self, data = []):
        self.data = DoubleLinkedList()
        for dat in data:
            self.push(dat)
    #Añadir a la cabeza    def push(self, new_value):
        self.data.insertHead(new_value)
    def pop(self):
        current = self.data.head        if not self.data.isEmpty():
            return self.data.deleteElement(current.getValue()).getValue()
        return None    def __str__(self):
        return str(self.data)
class Node:
    def __init__(self, value, next = None, prev = None):
        self.setValue(value)
        self.setNext(next)
        self.setPrev(prev)
    def getValue(self):
        return self.value    def getNext(self):
        return self.next    def getPrev(self):
        return self.prev    def __str__(self):
        return '(' + str(self.value) + ')' + (('<-->'+ str(self.next)) if self.next is not None else '')
    def setValue(self, new_value):
        self.value = new_value    def setNext(self, new_next):
        if (isinstance(new_next, Node) or new_next is None):
            self.next = new_next        else:
            raise Exception('Error en actualización del Nodo')
    def setPrev(self, new_prev):
        if (isinstance(new_prev, Node) or new_prev is None):
            self.prev = new_prev        else:
            raise Exception('Error en actualización del Nodo')
    def clear(self):
        self.setNext(None)
        self.setPrev(None)
def main():
    pila = Stack(['biologia', 'calculo', 'fisica'])
    print(pila)
    current = pila.pop()
    while current is not None:
        print(current)
        current = pila.pop()
    libros = ['Algoritmos', 'Geometria', 'Finanzas', 'Estructuras']
    for libro in libros:
        pila.push(libro)
        print(pila)
main(