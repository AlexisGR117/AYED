from sys import stdin
import math


class GraphAdj:
    def __init__(self, V={}, E={}, undirected=False):
        self.V = V
        self.E = E
        self.data = {}
        self.data_w = {}
        self.data_props = {}
        for v in self.V:
            self.data[v] = set()
            self.data_w[v] = set()
            self.data_props[v] = {}
        for e in E:
            c_1, c_2 = e[0], e[1]
            self.data[c_1].add(c_2)
            self.data_w[c_1].add(e)
            if undirected:
                self.data[c_2].add(c_1)
                if len(e) > 2:
                    self.data_w[c_2].add((e[1], e[0], e[2]))
                else:
                    self.data_w[c_2].add((c_2, c_1))

    def get_neighbors(self, vertex):
        return list(self.data[vertex])

    def get_near_by_arcs(self, vertex):
        return list(self.data_w[vertex])

    def print_data(self):
        for key in self.data.keys():
            print("{} : {}".format(key, self.data[key]))

    def relax(self, arc):
        u, v, w = arc
        if self.data_props[v]["tiempo"] > self.data_props[u]["tiempo"] + w:
            self.data_props[v]["tiempo"] = self.data_props[u]["tiempo"] + w
            self.data_props[v]["phi"] = u

    def init_trv(self, s=None):
        for v in self.V:
            if v == s:
                self.data_props[v] = {
                    "tiempo": 0,
                    "phi": None
                }
            else:
                self.data_props[v] = {
                    "tiempo": math.inf,
                    "phi": None
                }

    def compose_route(self, v, state):
        route = str(v)
        current_phi = state[v]["phi"]
        while current_phi is not None:
            route = str(current_phi) + "->" + route
            current_phi = state[current_phi]["phi"]
        return route

    def print_trv_state(self, result):
        for v in result.keys():
            result[v]["route"] = self.compose_route(v, result)
            print("{} : {}".format(v, str(result[v])))

    def extract_min(self, visited):
        min_distance, min_vertex = math.inf, None
        for v in self.V:
            if v not in visited and self.data_props[v]["tiempo"] <= min_distance:
                min_distance, min_vertex = self.data_props[v]["tiempo"], v
        return min_vertex

    def dijkstra(self, s):
        self.init_trv(s)
        visited = set()
        Q = [i for i in self.V]
        while len(Q) > 0:
            u = self.extract_min(visited)
            Q.remove(u)
            visited.add(u)
            for e in self.get_near_by_arcs(u):
                self.relax(e)
        return self.data_props


def solve():
    ratones = 0
    celdas = int(stdin.readline().strip())
    V = [i for i in range(1, celdas + 1)]
    salida = int(stdin.readline().strip())
    temp = int(stdin.readline().strip())
    conexiones = int(stdin.readline().strip())
    E = set()
    for i in range(conexiones):
        a, b, t = stdin.readline().strip().split()
        E.add((int(a), int(b), int(t)))
    grafo = GraphAdj(V, E)
    # grafo.print_data()
    for i in grafo.V:
        camino = grafo.dijkstra(i)
        # grafo.print_trv_state(camino)
        if camino[salida]["tiempo"] <= temp:
            ratones += 1
    return ratones


def main():
    cases = int(stdin.readline().strip())
    vacio = stdin.readline().strip()
    for i in range(cases - 1):
        print(solve())
        print()
        vacio = stdin.readline().strip()
    print(solve())


main()
