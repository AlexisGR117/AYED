from sys import stdin
from queue import Queue

GRAY = "GRAY"
WHITE = "WITHE"
BLACK = "BLACK"


class GraphAdj:
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

    def print_data(self):
        for key in self.data.keys():
            print("{} : {}".format(key, self.data[key]))

    def init_trv(self, s=None):
        for v in self.V:
            if v == s:
                self.data_color[v] = GRAY

    def bfs(self, s):
        self.init_trv(s)
        Q = Queue()
        Q.put(s)
        while Q.qsize() > 0:
            u = Q.get()
            for v in self.get_neighbors(u):
                if self.data_color[v] == WHITE:
                    self.data_color[v] = GRAY
                    Q.put(v)
            self.data_color[u] = BLACK
        return self.data_color

    def print_trv_state(self, result):
        for v in result.keys():
            print("{} : {}".format(v, str(result[v])))


def solve(comp):
    V = set([i for i in range(1, comp + 1)])
    E = set()
    line = stdin.readline().strip()
    afirmativas = 0
    negativas = 0
    while line != "":
        e, ci, cj = line.split()
        if e == "c":
            E.add((int(ci), int(cj)))
        else:
            graph = GraphAdj(V, E, True)
            state = graph.bfs(int(ci))
            if state[int(cj)] == BLACK:
                afirmativas += 1
            else:
                negativas += 1
        line = stdin.readline().strip()
    return afirmativas, negativas


def main():
    cases = int(stdin.readline().strip())
    vacio = stdin.readline().strip()
    rta = []
    for i in range(cases):
        comp = int(stdin.readline().strip())
        afirmativas, negativas = solve(comp)
        rta.append((afirmativas, negativas))
    for i in range(len(rta) - 1):
        print("{},{}".format(rta[i][0], rta[i][1]))
        print()
    print("{},{}".format(rta[-1][0], rta[-1][1]))


main()
