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
        # Minimo indice local
        if left <= self.heap_size and left_value < self.data[i]:
            largest = left
        else:
            largest = i
        # Minimo inidice locar teniendo en cuenta los valores de la derecha
        if right <= self.heap_size and right_value < self.data[largest]:
            largest = right
        # Si las prioridades cambiaron
        if largest != i:
            # Intercambiar largest con actual
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
        # Maximo indice local
        if left <= self.heap_size and left_value > self.data[i]:
            largest = left
        else:
            largest = i
        # Maximo inidice locar teniendo en cuenta los valores de la derecha
        if right <= self.heap_size and right_value > self.data[largest]:
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


def main():
    print("============= MaxHeap =============")
    print("Crear el MaxHeap:")
    heap = MaxHeap([5, 13, 2, 25, 7, 17, 20, 8, 4])
    print(heap)
    print("Remover 4 del heap:")
    heap.remove(4)
    print(heap)
    print("Insertar 3 al heap:")
    heap.insert(3)
    print(heap)
    print("Extraer el elemento de mayor valor:")
    print(heap.get_top())
    print(heap)
    print("============= Minimo =============")
    print("Crear el MinHeap:")
    heap = MinHeap([5, 13, 2, 25, 7, 17, 20, 8, 4])
    print(heap)
    print("Remover 4 del heap:")
    heap.remove(4)
    print(heap)
    print("Insertar 3 al heap:")
    heap.insert(3)
    print(heap)
    print("Extraer el elemento de menor valor:")
    print(heap.get_top())
    print(heap)


main()
