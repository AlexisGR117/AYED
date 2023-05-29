# Nombre: Jefer Alexis González Romero
# Carnet institucional: 2171737
# CC 1003618876
# Usuario: 1000046442

from sys import stdin
import math


class DisjointSet:
    def __init__(self, data=[]):
        self.data = []
        for e in data:
            if not isinstance(e, set):
                self.make_set(e)
            else:
                self.insert(e)

    def find_set(self, e):
        for st in self.data:
            if e in st:
                return st
        return None

    def make_set(self, e):
        st = self.find_set(e)
        if st is None:
            self.data.append({e})

    def union(self, x, y):
        st1, st2 = self.find_set(x), self.find_set(y)
        if st1 is None:
            self.make_set(x)
            st1 = self.find_set(x)
        if st2 is None:
            self.make_set(y)
            st2 = self.find_set(y)
        if st1 != st2:
            st3 = st1.union(st2)
            self.data.remove(st1)
            self.data.remove(st2)
            self.data.append(st3)

    def __str__(self):
        return str(self.data)

    def __len__(self):
        return len(self.data)

    def insert(self, st1):
        sreference = set()
        for e in st1:
            if self.find_set(e) is not None:
                sreference.add(e)
        sdiference = st1.difference(sreference)
        for e1 in sdiference:
            self.make_set(e1)
        for e1 in st1:
            for e2 in st1:
                self.union(e1, e2)


def solve(arcs):
    ds = DisjointSet()
    for i in range(arcs):
        u, v = stdin.readline().strip().split()
        ds.union(u, v)
    maximum = -math.inf
    minimum = math.inf
    for com in ds.data:
        if len(com) < minimum:
            minimum = len(com)
        if len(com) > maximum:
            maximum = len(com)
    return minimum, maximum


def main():
    arcs = int(stdin.readline().strip())
    answer = solve(arcs)
    print(answer[0], answer[1])


main()
