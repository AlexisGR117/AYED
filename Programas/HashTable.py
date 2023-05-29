from random import randint

class HashTable:

    def __init__(self, m = 10):
        self.size = m
        self.data = [ [] for x in range(self.size)]

    def _hash(self, n):
        return hash(n) % self.size

    def __str__(self):
        return self.data

    def printTable(self):
        for e in range(len(self.data)):
            print('On Category {}'.format(e))
            print('Present {} values: {} '.format(len(self.data[e]), self.data[e]))


    def insert(self, key, element):
        hash_index = self._hash(key)
        self.data[hash_index].append(element)

    def search(self, key, element):
        hash_index = self._hash(key)
        collisions = self.data[hash_index]
        return collisions[collisions.index(element)]

    def delete(self, key, element):
        hash_index = self._hash(key)
        self.data[hash_index].remove(element)

class Dictionary:

    def __init__(self, m = 10):
        self.size = m
        self.data = [ None for x in range(self.size)]

    def _hash(self, n):
        return hash(n) % self.size

    def __str__(self):
        return self.data

    def printTable(self):
        for e in range(len(self.data)):
            print('On Category {}'.format(e))
            print('Present {} values: {} '.format(1 if self.data[e] is not None else 0, self.data[e]))


    def insert(self, key, element):
        hash_index = self._hash(key)
        self.data[hash_index] = element

    def search(self, key):
        hash_index = self._hash(key)
        return self.data[hash_index]

    def delete(self, key):
        hash_index = self._hash(key)
        self.data[hash_index] = None

MAX_VALUE = 1e6
MAX_SIZE = 100

def main():
    ht = HashTable(int(1e6))

    ht.insert('pizza', 4.50)
    ht.insert('Burger', 2.50)
    ht.insert('Toy', 10.20)

    #ht.printTable()

    print(ht.search('pizza', 4.50))
    print(ht.search('Burger', 2.50))



main()

