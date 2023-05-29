# Nombre: Jefer Alexis González Romero
# Carnet institucional: 2171737
# CC 1003618876
# Usuario: 1000046442

from queue import Queue
from random import randint
from sys import stdin

WHITE = "WITHE"
BLUE = "BLUE"
RED = "RED"


class Graph:
    def __init__(self, V={}, E={}, undirected=False):
        self.V = V
        self.E = E
        self.data = {}
        self.data_color = {}
        for v in self.V:
            self.data[v] = set()
            self.data_color[v] = WHITE
        for e in E:
            c_1, c_2 = e[0], e[1]
            self.data[c_1].add(c_2)
            if undirected:
                self.data[c_2].add(c_1)

    def get_neighbors(self, vertex):
        return list(self.data[vertex])

    def init_trv(self, s=None):
        for v in self.V:
            if v == s:
                self.data_color[v] = BLUE

    def colorable(self):
        s = list(self.V)[randint(0, len(self.V) - 1)]
        self.init_trv(s)
        Q = Queue()
        Q.put(s)
        while Q.qsize() > 0:
            u = Q.get()
            color = self.data_color[u]
            if color == BLUE:
                c = RED
            else:
                c = BLUE
            for v in self.get_neighbors(u):
                if self.data_color[v] == WHITE:
                    self.data_color[v] = c
                    Q.put(v)
                else:
                    if color == self.data_color[v]:
                        return False
        return True


def main():
    n = int(stdin.readline().strip())
    while n != 0:
        V = set([i for i in range(n)])
        E = set()
        l = int(stdin.readline().strip())
        for i in range(l):
            u, v = stdin.readline().strip().split()
            E.add((int(u), int(v)))
        graph = Graph(V, E, True)
        answer = graph.colorable()
        if answer:
            print("BICOLORABLE.")
        else:
            print("NOT BICOLORABLE.")
        n = int(stdin.readline().strip())


main()
