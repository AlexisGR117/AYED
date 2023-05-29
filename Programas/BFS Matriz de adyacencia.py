import math
from queue import Queue

GRAY = "Gray"
WHITE = "WITHE"
BLACK = "BLACK"


class Graph:
    def __init__(self, V={}, E={}, undirected=False):
        self.V = V
        self.E = E
        self.data = [[0 for i in range(len(self.V))] for j in range(len(self.V))]
        self.data_props = {}
        for v in self.V:
            self.data_props[v] = {}
        for e in E:
            c_1, c_2 = self.get_vertex_index(e[0]), self.get_vertex_index(e[1])
            self.data[c_1][c_2] = 1
            if undirected:
                self.data[c_2][c_1] = 1

    def get_vertex_index(self, vertex):
        return vertex - 1

    def get_vertex_from_index(self, index):
        return index + 1

    def get_neighbors(self, vertex):
        neighbors, index = [], self.get_vertex_index(vertex)
        row = self.data[index]
        for neighbors_index in range(len(row)):
            if row[neighbors_index] != 0:
                neighbors.append(self.get_vertex_from_index(neighbors_index))
        return neighbors

    def print_data(self):
        for row in self.data:
            print(", ".join(map(str, row)))

    def init_trv(self, s=None):
        for v in self.V:
            if v == s:
                self.data_props[v] = {
                    "color": GRAY,
                    "distance": 0,
                    "phi": None
                }
            else:
                self.data_props[v] = {
                    "color": WHITE,
                    "distance": math.inf,
                    "phi": None
                }

    def bfs(self, s):
        self.init_trv(s)
        Q = Queue()
        Q.put(s)
        while Q.qsize() > 0:
            u = Q.get()
            for v in self.get_neighbors(u):
                if self.data_props[v]["color"] == WHITE:
                    self.data_props[v]["color"] = GRAY
                    self.data_props[v]["distance"] = self.data_props[u]["distance"] + 1
                    self.data_props[v]["phi"] = u
                    Q.put(v)
            self.data_props[u]["color"] = BLACK
        return self.data_props

    def compose_route(self, v, state):
        route = str(v)
        current_phi = state[v]["phi"]
        while current_phi is not None:
            route = str(current_phi) + "->" + route
            current_phi = state[current_phi]["phi"]
        return route

    def resultado(self, result):
        for v in result.keys():
            result[v]["route"] = self.compose_route(v, result)
            if result[v]["color"] == BLACK:
                print("{} : {}".format(v, result[v]["route"]))


def main():
    print("======================================== Prototipo ========================================")
    print("Juan quiere visitar algunas ciudades, para esto quiere saber a cuales puede ir")
    print("solo viajando por bus desde su ciudad de residencia, al buscar un poco encuentra")
    print("las siguientes rutas, donde cada número es una ciudad:")
    print("Inicio --> Destino")
    print("   1   -->    2")
    print("   2   -->    3")
    print("   2   -->    4")
    print("   3   -->    6")
    print("   3   -->    5")
    print("   4   -->    6")
    print("   5   -->    7")
    print("   5   -->    4")
    print("Las anteriores rutas se pueden ver en la siguiente matriz de adyacencia")
    graph = Graph({1, 2, 3, 4, 5, 6, 7},
                  {(1, 2), (2, 3), (2, 4), (3, 6), (3, 5), (5, 7), (5, 4)},
                  False
                  )
    graph.print_data()
    print("Si Juan vive en la ciudad 3, puede ir a las siguientes")
    print("ciudades con sus respectivas rutas:")
    state_result = graph.bfs(3)
    graph.resultado(state_result)
    print("Ahora si Juan vive en la ciudad 5, puede ir a las siguientes")
    print("ciudades con sus respectivas rutas:")
    state_result = graph.bfs(5)
    graph.resultado(state_result)
    print("En el caso de que viviera en la ciudad 6 no tendría opciones,")
    print("solo en la que vive:")
    state_result = graph.bfs(6)
    graph.resultado(state_result)
    print("La ciudad que le permitiría conocer mas ciudades es la 1:")
    state_result = graph.bfs(1)
    graph.resultado(state_result)


main()
