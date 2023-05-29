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
        if self.data_props[v]["estaciones"] > self.data_props[u]["estaciones"] + w:
            self.data_props[v]["estaciones"] = self.data_props[u]["estaciones"] + w
            self.data_props[v]["phi"] = u

    def init_trv(self, s=None):
        for v in self.V:
            if v == s:
                self.data_props[v] = {
                    "estaciones": 1,
                    "phi": None
                }
            else:
                self.data_props[v] = {
                    "estaciones": math.inf,
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
            if v not in visited and self.data_props[v]["estaciones"] <= min_distance:
                min_distance, min_vertex = self.data_props[v]["estaciones"], v
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


def estaciones(cantidad):
    E = set()
    V = set()
    for i in range(cantidad):
        estaciones = stdin.readline().strip().split(",")
        if estaciones[0].split()[1] not in V:
            V.add(estaciones[0].split()[1])
        for j in range(1, len(estaciones)):
            E.add((estaciones[0].split()[1], estaciones[j].split()[1], 1))
            if estaciones[j].split()[1] not in V:
                V.add(estaciones[j].split()[1])
    return V, E


def main():
    cantidad = int(stdin.readline().strip())
    V, E = estaciones(cantidad)
    grafo = GraphAdj(V, E)
    #grafo.print_data()
    ruta = stdin.readline().strip().split(",")
    inicio, fin = ruta[0].split()[1], ruta[1].split()[1]
    rutas = grafo.dijkstra(inicio)
    #grafo.print_trv_state(rutas)
    print("La cantidad de estaciones por las que se pasa son:", rutas[fin]["estaciones"])


main()
