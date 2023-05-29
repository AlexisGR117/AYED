from sys import stdin


class MaxHeap:
    def __init__(self, data=[]):
        self.data = []
        self.build_heap(data)

    def insert(self, element):
        self.data.append(element)
        self.build_heap(self.data)

    def remove(self, element):
        self.data.remove(element)
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
        # Maximo indice local
        if left < len(self.data) and left_value > self.data[i]:
            largest = left
        else:
            largest = i
        # Maximo inidice locar teniendo en cuenta los valores de la derecha
        if right < len(self.data) and right_value > self.data[largest]:
            largest = right
        # Si las prioridades cambiaron
        if largest != i:
            # Intercambiar largest con actual
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

    def get_top_priority(self):
        if not self.is_empty():
            top = self.data.pop(0)
            self.build_heap(self.data)
            return top


def solve(instrucciones):
    linea = stdin.readline().strip()
    if linea == "saque máximo":
        if not instrucciones.is_empty():
            print(instrucciones.get_top_priority())
    else:
        x = int(linea.split()[1])
        instrucciones.insert(x)


def main():
    lineas = int(stdin.readline().strip())
    instrucciones = MaxHeap()
    for i in range(lineas):
        solve(instrucciones)


main()
