class MinHeap:
    def __init__(self, data=[]):
        self.data = []
        self.heap_size = len(data) - 1
        self.build_heap(data)

    def insert(self, element):
        self.data.append(element)
        self.heap_size += 1
        self.build_heap(self.data)

    def remove(self, element):
        self.data.remove(element)
        self.heap_size -= 1
        self.build_heap(self.data)

    def parent(self, index):
        return (index - 1) // 2

    def parent_value(self, index):
        index_child = self.parent(index)
        return self.data[index_child] if 0 <= index_child < len(self.data) else None

    def left(self, index):
        return 2 * index + 1

    def left_value(self, index):
        index_child = self.left(index)
        return self.data[index_child] if 0 <= index_child < len(self.data) else None

    def right(self, index):
        return 2 * (index + 1)

    def right_value(self, index):
        index_child = self.right(index)
        return self.data[index_child] if 0 <= index_child < len(self.data) else None

    def min_heapify(self, i):
        left, left_value, right, right_value = self.left(i), self.left_value(i), self.right(i), self.right_value(i)
        largest = None
        if left <= self.heap_size and left_value[1] < self.data[i][1]:
            largest = left
        else:
            largest = i
        if right <= self.heap_size and right_value[1] < self.data[largest][1]:
            largest = right
        if largest != i:
            self.data[largest], self.data[i] = self.data[i], self.data[largest]
            self.min_heapify(largest)

    def build_heap(self, data):
        self.data = data
        for i in range(len(self.data), -1, -1):
            self.min_heapify(i)

    def __str__(self):
        return str(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def get_top(self):
        if not self.is_empty():
            top = self.data.pop(0)
            self.heap_size -= 1
            self.build_heap(self.data)
            return top

    def __len__(self):
        return len(self.data)

    def heap_sort(self):
        for i in range(len(self) - 1, 0, -1):
            self.data[0], self.data[i] = self.data[i], self.data[0]
            self.heap_size -= 1
            self.min_heapify(0)
        return self.data


class MaxHeap:
    def __init__(self, data=[]):
        self.data = []
        self.heap_size = len(data) - 1
        self.build_heap(data)

    def insert(self, element):
        self.data.append(element)
        self.heap_size += 1
        self.build_heap(self.data)

    def remove(self, element):
        self.data.remove(element)
        self.heap_size -= 1
        self.build_heap(self.data)

    def parent(self, index):
        return (index - 1) // 2

    def parent_value(self, index):
        index_child = self.parent(index)
        return self.data[index_child] if 0 <= index_child < len(self.data) else None

    def left(self, index):
        return 2 * index + 1

    def left_value(self, index):
        index_child = self.left(index)
        return self.data[index_child] if 0 <= index_child < len(self.data) else None

    def right(self, index):
        return 2 * (index + 1)

    def right_value(self, index):
        index_child = self.right(index)
        return self.data[index_child] if 0 <= index_child < len(self.data) else None

    def max_heapify(self, i):
        left, left_value, right, right_value = self.left(i), self.left_value(i), self.right(i), self.right_value(i)
        largest = None
        if left <= self.heap_size and left_value[1] > self.data[i][1]:
            largest = left
        else:
            largest = i
        if right <= self.heap_size and right_value[1] > self.data[largest][1]:
            largest = right
        if largest != i:
            self.data[largest], self.data[i] = self.data[i], self.data[largest]
            self.max_heapify(largest)

    def build_heap(self, data):
        self.data = data
        for i in range(len(self.data), -1, -1):
            self.max_heapify(i)

    def __str__(self):
        return str(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def get_top(self):
        if not self.is_empty():
            top = self.data.pop(0)
            self.heap_size -= 1
            self.build_heap(self.data)
            return top

    def __len__(self):
        return len(self.data)

    def heap_sort(self):
        for i in range(len(self) - 1, 0, -1):
            self.data[0], self.data[i] = self.data[i], self.data[0]
            self.heap_size -= 1
            self.max_heapify(0)


class PriorityQueue:
    def __init__(self, data=[], policy=True):
        self.policy = policy
        if self.policy:
            self.data = MaxHeap(data)
        else:
            self.data = MinHeap(data)

    def enqueue(self, element):
        self.data.insert(element)

    def dequeue(self):
        return self.data.get_top()

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)


def main():
    print("======================================== Prototipo ========================================")
    print("Juan es un repartidor de una aplicación que permite hacer pedidos a domicilos")
    print("esta aplicación le asigna a cada encargo una prioridad que depende de varios factores")
    print("como el tipo de pedido y el lugar de destino. Juan al iniciar el día le llegan los siguientes")
    print("pedidos de 5 personas, con sus correspondientes prioridades:\n")
    pedidos = [("Juana", 12), ("Maria", 30), ("Pedro", 20), ("Julian", 32), ("Samuel", 24)]
    print("Pedidos:", pedidos, "\n")
    print("La aplicación se lo ordena en montón binario representado en el siguiente arreglo:\n")
    pedidos = PriorityQueue(pedidos, True)
    print("Pedidos:", pedidos, "\n")
    print("Despues de realizar la entrega de mayor prioridad que era la de Julian, queda de la siguiente manera:\n")
    pedidos.dequeue()
    print("Pedidos:", pedidos, "\n")
    print("Le llega un nuevo pedido de Martha con prioridad 22\n")
    pedidos.enqueue(("Martha", 22))
    print("Pedidos:", pedidos, "\n")
    print("Entrega 2 domicilios\n")
    pedidos.dequeue()
    pedidos.dequeue()
    print("Pedidos:", pedidos, "\n")
    print("Al finalizar la jornada de trabajo ya ha entregado todos los domicilios\n")
    pedidos.dequeue()
    pedidos.dequeue()
    pedidos.dequeue()
    print("Pedidos:", pedidos, "\n")


main()
