class MinHeap:
    def __init__(self, data=[]):
        self.data = []
        self.heap_size = len(data) - 1
        self.build_heap(data)

    def min_heap_insert(self, element):
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
        if left <= self.heap_size and left_value < self.data[i]:
            largest = left
        else:
            largest = i
        if right <= self.heap_size and right_value < self.data[largest]:
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

    def heap_extract_minimum(self):
        if not self.is_empty():
            top = self.data.pop(0)
            self.heap_size -= 1
            self.build_heap(self.data)
            return top

    def heap_minimum(self):
        if not self.is_empty():
            top = self.data[0]
            return top
        return None

    def __len__(self):
        return len(self.data)

    def heap_decrease_key(self, index, key):
        if key > self.data[index]:
            print("La nueva llave es mas grande que la llave actual")
        self.data[index] = key
        while index > 0 and self.data[self.parent(index)] > self.data[index]:
            self.data[index], self.data[self.parent(index)] = self.data[self.parent(index)], self.data[index]
            index = self.parent(index)


def main():
    dt = MinHeap([15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1])
    print("======== Al hacer un MinHeap con el arreglo dado queda =======")
    print(dt)
    print("======== Operación heap_minimum ========")
    print("Retorna el menor valor:", dt.heap_minimum())
    print("======== Operación heap_extract_minimum ========")
    print("Valor que se remueve del heap:", dt.heap_extract_minimum())
    print("El heap queda:", dt)
    print("======== Si cambiamos el 9 por un 3 usando heap_decrease_key ========")
    dt.heap_decrease_key(10, 3)
    print(dt)
    print("======== Insertamos 10 al heap (min_heap_insert) ========")
    dt.min_heap_insert(10)
    print(dt)


main()
