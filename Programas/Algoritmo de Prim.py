import math


class Graph:
    def __init__(self, V={}, E={}, undirected=False):
        new_V = set()
        i = 0
        for v in V:
            new_V.add((v, i))
            i += 1
        self.V = sorted(new_V, key=lambda indice: indice[1])
        self.E = E
        self.data = [[0 for i in range(len(self.V))] for j in range(len(self.V))]
        self.data_props = {}
        for v in self.V:
            self.data_props[v[0]] = {}
        for e in E:
            c_1, c_2 = self.get_vertex_index(e[0]), self.get_vertex_index(e[1])
            self.data[c_1][c_2] = 1
            if undirected:
                self.data[c_2][c_1] = 1

    def get_vertex_index(self, vertex):
        for v in self.V:
            if v[0] == vertex:
                return v[1]

    def get_vertex_from_index(self, index):
        for v in self.V:
            if v[1] == index:
                return v[0]

    def get_neighbors(self, vertex):
        neighbors, index = [], self.get_vertex_index(vertex)
        row = self.data[index]
        for neighbors_index in range(len(row)):
            if row[neighbors_index] != 0:
                neighbors.append(self.get_vertex_from_index(neighbors_index))
        return neighbors

    def get_near_by_arcs(self, vertex):
        near_arcs, neighbors = [], self.get_neighbors(vertex)
        for n in neighbors:
            for e in self.E:
                if (e[0] == n and e[1] == vertex) or (e[1] == n and e[0] == vertex):
                    w = e[2]
            near_arcs.append((vertex, n, w))
        return near_arcs

    def print_data(self):
        for row in self.data:
            print(", ".join(map(str, row)))

    def init_trv(self, r=None):
        for v in self.V:
            if v[0] == r:
                self.data_props[v[0]] = {
                    "key": 0,
                    "phi": None
                }
            else:
                self.data_props[v[0]] = {
                    "key": math.inf,
                    "phi": None
                }

    def print_trv_state(self, result):
        for v in result.keys():
            print("({}, {}, {})".format(result[v]["phi"], v, result[v]["key"]))

    def extract_min(self, Q):
        min_key, min_vertex = math.inf, None
        for v in Q:
            if self.data_props[v[0]]["key"] < min_key:
                min_key, min_vertex = self.data_props[v[0]]["key"], v[0]
        Q.remove(min_vertex)
        return min_vertex

    def prim(self, r):
        self.init_trv(r)
        Q = sorted([i[0] for i in self.V])
        while len(Q) > 0:
            u = self.extract_min(Q)
            for v in self.get_near_by_arcs(u):
                if v[1] in Q and v[2] < self.data_props[v[1]]["key"]:
                    self.data_props[v[1]]["phi"] = u
                    self.data_props[v[1]]["key"] = v[2]
        return self.data_props


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

    def init_trv(self, r=None):
        for v in self.V:
            if v == r:
                self.data_props[v] = {
                    "key": 0,
                    "phi": None
                }
            else:
                self.data_props[v] = {
                    "key": math.inf,
                    "phi": None
                }

    def print_trv_state(self, result):
        for v in result.keys():
            print("({}, {}, {})".format(result[v]["phi"], v, result[v]["key"]))

    def extract_min(self, Q):
        min_key, min_vertex = math.inf, None
        for v in Q:
            if self.data_props[v]["key"] < min_key:
                min_key, min_vertex = self.data_props[v]["key"], v
        Q.remove(min_vertex)
        return min_vertex

    def prim(self, r):
        self.init_trv(r)
        Q = sorted([i for i in self.V])
        print(Q)
        while len(Q) > 0:
            u = self.extract_min(Q)
            for v in self.get_near_by_arcs(u):
                if v[1] in Q and v[2] < self.data_props[v[1]]["key"]:
                    self.data_props[v[1]]["phi"] = u
                    self.data_props[v[1]]["key"] = v[2]
        return self.data_props


def main():
    print("======================================== Prototipo ========================================")
    print("Para el diseño de un circuito Juan requiere interconectar diversos componentes")
    print("eléctricos con un cable entre ellos, además el profesor le pide que use la menor ")
    print("cantidad posible de cable. Las componentes son nombradas con letras y se pueden")
    print("hacer las siguientes conexiones, con su respectiva longitud de cable que se requiere:")
    print("           conexiones")
    print("   a   <-->    b, longitud = 4")
    print("   a   <-->    h, longitud = 8")
    print("   b   <-->    h, longitud = 11")
    print("   b   <-->    c, longitud = 8")
    print("   c   <-->    d, longitud = 7")
    print("   c   <-->    f, longitud = 4")
    print("   c   <-->    i, longitud = 2")
    print("   d   <-->    e, longitud = 9")
    print("   d   <-->    f, longitud = 14")
    print("   e   <-->    f, longitud = 10")
    print("   f   <-->    g, longitud = 2")
    print("   g   <-->    h, longitud = 1")
    print("   g   <-->    i, longitud = 6")
    print("   h   <-->    i, longitud = 7")
    print("(EL grafo que representa el circuito se puede ver en el documento adjunto)")
    V = {"a", "b", "c", "d", "e", "f", "g", "h", "i"}
    E = {("a", "b", 4), ("a", "h", 8), ("b", "h", 11), ("b", "c", 8), ("c", "d", 7), ("c", "f", 4), ("c", "i", 2),
         ("d", "e", 9), ("d", "f", 14), ("e", "f", 10), ("f", "g", 2), ("g", "h", 1), ("g", "i", 6), ("h", "i", 7)}
    print("Ejecutando el algoritmo de prim comenzando desde la componente 'a' para las dos representaciones")
    print("da que las conexiones que debe hacer Juan para satisfacer lo que se le pedia son las siguientes:")
    print("======================= Con matriz de adyacencia =======================")
    graph = Graph(V, E, True)
    graph.print_data()
    print("Conexiones:")
    conexiones = graph.prim("a")
    graph.print_trv_state(conexiones)
    print("======================= Con lista de adyacencia =======================")
    graph_2 = GraphAdj(V, E, True)
    graph_2.print_data()
    print("Conexiones:")
    conexiones_2 = graph_2.prim("a")
    graph_2.print_trv_state(conexiones_2)
    print("======================= Otros casos =======================")
    print("Comienza desde la componente 'c':")
    conexiones_3 = graph_2.prim("c")
    graph_2.print_trv_state(conexiones_3)
    print("Comienza desde la componente 'e':")
    conexiones_4 = graph_2.prim("e")
    graph_2.print_trv_state(conexiones_4)


main()
