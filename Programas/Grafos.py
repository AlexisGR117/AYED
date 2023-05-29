import math
from queue import Queue
from random import randint
import heapq  # Python library for Max-heap y Min-heap, priority queue, deafult is Min Heap

GRAY = "GRAY"
WHITE = "WITHE"
BLACK = "BLACK"


# Con representación por matriz de adyacencia
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

    def print_data(self):
        for row in self.data:
            print(", ".join(map(str, row)))

    def init_trv(self, s=None):
        for v in self.V:
            if v[0] == s:
                self.data_props[v[0]] = {
                    "color": GRAY,
                    "distance": 0,
                    "phi": None
                }
            else:
                self.data_props[v[0]] = {
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

    def print_trv_state(self, result):
        for v in result.keys():
            result[v]["route"] = self.compose_route(v, result)
            print("{} : {}".format(v, str(result[v])))

    def dfs(self):
        for vertex in self.V:
            self.data_props[vertex[0]]["color"] = WHITE
            self.data_props[vertex[0]]["phi"] = None
        time = 0
        for u in self.V:
            if self.data_props[u[0]]["color"] == WHITE:
                time = self.dfs_visit(u[0], time)
        return self.data_props

    def dfs_visit(self, vertex, time):
        time = time + 1
        self.data_props[vertex]["distance"] = time
        self.data_props[vertex]["color"] = GRAY
        for v in self.get_neighbors(vertex):
            if self.data_props[v]["color"] == WHITE:
                self.data_props[v]["phi"] = vertex
                time = self.dfs_visit(v, time)
        self.data_props[vertex]["color"] = BLACK
        time = time + 1
        self.data_props[vertex]["distancie_final"] = time
        return time

    def kruskal(self):
        a = set([])
        v = [v[0] for v in self.V]
        dset = DisjointSet(v)
        sorted_arcs = sorted(self.E, key=lambda arc: (arc[2], arc[0], arc[1]))
        index = 0
        while index < len(sorted_arcs) and len(dset) > 1:
            arc = sorted_arcs[index]
            if dset.find_set(arc[0]) != dset.find_set(arc[1]):
                a.add(arc)
                dset.union(arc[0], arc[1])
            index += 1
        return a

    def init_trv_2(self, r=None):
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

    def print_trv_2_state(self, result):
        for v in result.keys():
            print("({}, {}, {})".format(result[v]["phi"], v, result[v]["key"]))

    def prim(self, r):
        self.init_trv_2(r)
        Q = set()
        for v in self.V:
            Q.add(v[0])
        Q = sorted(Q, reverse=True)
        while len(Q) > 0:
            u = Q.pop()
            for v in self.get_neighbors(u):
                w = -math.inf
                for i in self.E:
                    if i[0] == u and i[1] == v:
                        w = i[2]
                if v in Q and w < self.data_props[v]["key"]:
                    self.data_props[v]["phi"] = u
                    self.data_props[v]["key"] = w
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

    def relax(self, arc):
        u, v, w = arc
        if self.data_props[v]["distance"] > self.data_props[u]["distance"] + w:
            self.data_props[v]["distance"] = self.data_props[u]["distance"] + w
            self.data_props[v]["phi"] = u

    def bell_man_ford(self, s):
        self.init_trv(s)
        # Recorrer todos los arcos v-1 veces
        for i in range(len(self.V)-1):
            for e in self.E:
                self.relax(e)
        # Hay un signo negativo
        for (u, v, w ) in self.E:
            if self.data_props[v]["distance"] > self.data_props[u]["distance"] + w:
                return None
        return self.data_props


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

    def print_trv_state(self, result):
        for v in result.keys():
            result[v]["route"] = self.compose_route(v, result)
            print("{} : {}".format(v, str(result[v])))

    def dfs(self):
        for vertex in self.V:
            self.data_props[vertex]["color"] = WHITE
            self.data_props[vertex]["phi"] = None
        time = 0
        for u in self.V:
            if self.data_props[u]["color"] == WHITE:
                time = self.dfs_visit(u, time)
        return self.data_props

    def dfs_visit(self, vertex, time):
        time = time + 1
        self.data_props[vertex]["distance"] = time
        self.data_props[vertex]["color"] = GRAY
        # Reviso mis vecinos en profundidad
        for v in self.get_neighbors(vertex):
            if self.data_props[v]["color"] == WHITE:
                self.data_props[v]["phi"] = vertex
                time = self.dfs_visit(v, time)
        self.data_props[vertex]["color"] = BLACK
        time = time + 1
        self.data_props[vertex]["distancie_final"] = time
        return time

    def kruskal(self):
        a = set([])  # Arbol de expansión mínimo
        dset = DisjointSet(list(self.V))
        sorted_arcs = sorted(self.E, key=lambda arc: (arc[2], arc[0], arc[1]))
        index = 0
        while index < len(sorted_arcs) and len(dset) > 1:
            arc = sorted_arcs[index]
            if dset.find_set(arc[0]) != dset.find_set(arc[1]):
                a.add(arc)
                dset.union(arc[0], arc[1])
            index += 1
        return a

    def extract_min(self, visited):
        min_distance, min_vertex = math.inf, None
        for v in self.V:
            if v not in visited and self.data_props[v]["distance"] <= min_distance:
                min_distance, min_vertex = self.data_props[v]["distance"], v
        return min_vertex

    def prim(self):
        mst = set()
        selected_vertex = list(self.V)[randint(0, len(self.V)-1)]
        visited = set([selected_vertex])
        neighbor_arcs = [(w, u, v) for (u, v, w) in self.get_near_by_arcs(selected_vertex)]
        heapq.heapify(neighbor_arcs)  # Prioriza por la primera componente
        while neighbor_arcs:
            w, u, v = heapq.heappop(neighbor_arcs)
            if v not in visited:
                visited.add(v)
                mst.add((u, v, w))
                neighbors = self.get_near_by_arcs(v)
                for (u_1, v_1, w_1) in neighbors:
                    if v_1 not in visited:
                        heapq.heappush(neighbor_arcs, (w_1, u_1, v_1))
        return mst

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


def main():
    print("============= Undirected =============")
    graph = Graph({1, 2, 3, 4, 5},
                  {(1, 2), (1, 5), (2, 5), (2, 3), (2, 4), (3, 4), (4, 5)},
                  True
                  )
    undirected_graph = GraphAdj({1, 2, 3, 4, 5},
                                {(1, 2), (1, 5), (2, 5), (2, 3), (2, 4), (3, 4), (4, 5)},
                                True
                                )
    print("Adjacency - MATRIX")
    graph.print_data()
    print(graph.get_neighbors(1))
    print("Adjacency - LIST")
    undirected_graph.print_data()
    print(undirected_graph.get_neighbors(1))
    print("============= Directed =============")
    graph = Graph({1, 2, 3, 4, 5, 6},
                  {(1, 2), (1, 4), (2, 5), (3, 5), (3, 6), (4, 2), (5, 4), (6, 6)},
                  False
                  )
    directed_graph = GraphAdj({1, 2, 3, 4, 5, 6},
                              {(1, 2), (1, 4), (2, 5), (3, 5), (3, 6), (4, 2), (5, 4), (6, 6)},
                              False
                              )
    print("Adjacency - MATRIX")
    graph.print_data()
    print("Adjacency - LIST")
    directed_graph.print_data()

    print("============= BFS Tests =============")
    graph_bfs = GraphAdj({0, 1, 2, 3, 4},
                         {(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)},
                         False
                         )
    graph_bfs_mt = Graph({0, 1, 2, 3, 4},
                         {(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)},
                         False
                         )
    print("Adjacency - LIST")
    graph_bfs.print_data()
    print("Adjacency - MATRIX")
    graph_bfs_mt.print_data()
    source = 0
    state_result = graph_bfs.bfs(source)
    state_result_mt = graph_bfs_mt.bfs(source)
    print("Adjacency - LIST Reachable nodes from {}".format(source))
    graph_bfs.print_trv_state(state_result)
    print("Adjacency - MATRIX Reachable nodes from {}".format(source))
    graph_bfs_mt.print_trv_state(state_result_mt)
    print("============= BFS Tests PArcial =============")
    V = {0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11}
    E = {(0, 1), (1, 2), (1, 4), (2, 0), (2, 1), (3, 4), (3, 5), (3, 11), (4, 1), (4, 6), (5, 4), (5, 10), (6, 7),
         (6, 8), (7, 8), (8, 6), (8, 7), (11, 10)}
    graph_bfs = GraphAdj(V,
                         E,
                         False
                         )
    graph_bfs_mt = Graph(V,
                         E,
                         False
                         )
    print("Adjacency - LIST")
    graph_bfs.print_data()
    print("Adjacency - MATRIX")
    graph_bfs_mt.print_data()
    source = 5
    state_result = graph_bfs.bfs(source)
    state_result_mt = graph_bfs_mt.bfs(source)
    print("Adjacency - LIST Reachable nodes from {}".format(source))
    graph_bfs.print_trv_state(state_result)
    print("Adjacency - MATRIX Reachable nodes from {}".format(source))
    graph_bfs_mt.print_trv_state(state_result_mt)

    print("============= DFS Tests =============")
    print("Adjacency - LIST")
    graph_dfs = GraphAdj({1, 2, 3, 4, 5, 6, 7},
                         {(1, 2), (2, 3), (2, 4), (3, 6), (3, 5), (4, 6), (5, 7), (5, 6), (5, 4)},
                         False
                         )
    state_result_dfs = graph_dfs.dfs()
    graph_dfs.print_trv_state(state_result_dfs)
    print("Adjacency - MATRIX")
    graph_dfs_2 = Graph({1, 2, 3, 4, 5, 6, 7},
                        {(1, 2), (2, 3), (2, 4), (3, 6), (3, 5), (4, 6), (5, 7), (5, 6), (5, 4)},
                        False
                        )
    state_result_dfs_2 = graph_dfs_2.dfs()
    graph_dfs_2.print_trv_state(state_result_dfs_2)
    V = set([i for i in range(15)])
    E = {(0, 1), (1, 2), (2, 0),
         (3, 7), (5, 3), (7, 8), (8, 5),
         (9, 10), (9, 6), (10, 6),
         (11, 12), (12, 13), (13, 11)
         }
    graph_cp = GraphAdj(V, E)
    state_result_dfs = graph_cp.dfs().copy()
    connected_components = []
    print("============= Topological state =============")
    graph_cp.print_trv_state(state_result_dfs)
    print("============= DFS Tests PARCIAL =============")
    print("Adjacency - LIST")
    V = {0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 11}
    E = {(1, 0), (2, 1), (4, 1), (0, 2), (1, 2), (4, 3), (5, 3), (11, 3), (1, 4), (6, 4), (4, 5), (10, 5), (7, 6),
         (8, 6), (8, 7), (6, 8), (7, 8), (10, 11)}
    graph_dfs = GraphAdj(V,E, False)
    state_result_dfs = graph_dfs.dfs()
    graph_dfs.print_trv_state(state_result_dfs)
    print("Adjacency - MATRIX")
    graph_dfs_2 = Graph(V,E, False)
    state_result_dfs_2 = graph_dfs_2.dfs()
    graph_dfs_2.print_trv_state(state_result_dfs_2)
    graph_cp = GraphAdj(V, E)
    state_result_dfs = graph_cp.dfs().copy()
    connected_components = []
    print("============= Topological state =============")
    graph_cp.print_trv_state(state_result_dfs)
    print("============= Find coneccted components using BFS an DFS =============")
    for v in state_result_dfs.keys():
        if state_result_dfs[v]["phi"] is None:
            # print("Found a root of isolated component", v)
            state_result = graph_cp.bfs(v)
            # graph_cp.print_trv_state(state_result)
            component_structure = []
            for node in state_result.keys():
                if state_result[node]["color"] == BLACK:
                    component_structure.append(node)
            if len(component_structure) > 1:
                connected_components.append(set(component_structure))
    print("The connected components f G(V, E) are:")
    print(connected_components)
    print("============= With Matrix Adjacency =============")
    V = set([i for i in range(15)])
    E = {(0, 1), (1, 2), (2, 0),
         (3, 7), (5, 3), (7, 8), (8, 5),
         (9, 10), (9, 6), (10, 6),
         (11, 12), (12, 13), (13, 11)
         }
    graph_cp_2 = Graph(V, E)
    state_result_dfs_2 = graph_cp_2.dfs().copy()
    connected_components_2 = []
    print("============= Topological state =============")
    graph_cp_2.print_trv_state(state_result_dfs_2)
    print("============= Find coneccted components using BFS an DFS =============")
    for v in state_result_dfs_2.keys():
        if state_result_dfs_2[v]["phi"] is None:
            state_result_2 = graph_cp_2.bfs(v)
            component_structure_2 = []
            for node in state_result_2.keys():
                if state_result_2[node]["color"] == BLACK:
                    component_structure_2.append(node)
            if len(component_structure_2) > 1:
                connected_components_2.append(set(component_structure_2))
    print("The connected components f G(V, E) are:")
    print(connected_components_2)
    print("============= Find coneccted components using Disjoin Sets =============")
    ds = DisjointSet()
    for e in E:
        print("Arc", e)
        ds.union(e[0], e[1])
        print(ds)
    print("============= Find coneccted components using Disjoin Sets parcial=============")
    ds = DisjointSet()
    E = {(1, 2), (1, 17), (2, 1), (2, 17), (3, 4), (3, 7), (4, 3), (4, 6), (5, 6), (5, 7), (6, 4), (6, 5), (7, 3),
         (7, 5), (8, 9), (8, 11), (9, 8), (9, 10), (10, 9), (10, 11), (11, 8), (11, 10), (15, 16), (16, 15), (17, 1),
         (17, 2), (17, 17)}
    for e in E:
        print("Arc", e)
        ds.union(e[0], e[1])
        print(ds)
    print("============= Kruskal Test List adjacency =============")
    V = {"a", "b", "c", "d", "e", "f", "g", "h", "i"}
    E = {("a", "b", 4), ("a", "h", 8), ("b", "h", 11), ("b", "c", 8), ("c", "d", 7), ("c", "f", 4), ("c", "i", 2),
         ("d", "e", 9), ("d", "f", 14), ("e", "f", 10), ("f", "g", 2), ("g", "h", 1), ("g", "i", 6), ("h", "i", 7)}
    graph_undirected = GraphAdj(V, E, True)
    mst_tree = graph_undirected.kruskal()
    print(mst_tree)
    print("============= Kruskal Test matrix adjacency =============")
    graph_undirected_2 = Graph(V, E, True)
    mst_tree_2 = graph_undirected_2.kruskal()
    print(mst_tree_2)
    print("============= Prim Test =============")
    mst_tree_3 = graph_undirected.prim()
    print(mst_tree_3)
    print("============= Prim Test =============")
    #mst_tree_4 = graph_undirected_2.prim()
    #graph_undirected.print_trv_state(mst_tree_4)
    print("============= BellManFord Test =============")
    V = {0, 1, 2, 3, 4}
    E = {(0, 1, 2), (0, 2, 6), (0, 3, 7),
         (1, 3, 3), (1, 4, 6), (2, 4, 1),
         (3, 4, 5)
         }
    graph_directed = GraphAdj(V, E)
    ssp_tree = graph_directed.bell_man_ford(0)
    graph_directed.print_trv_state(ssp_tree)
    print("============= Dijkstra Test =============")
    V = {"s", "y", "z", "t", "x"}
    E = {("s", "y", 5), ("s", "t", 10), ("y", "z", 2),
         ("y", "x", 9), ("y", "t", 3), ("z", "x", 6),
         ("z", "s", 7), ("t", "x", 1), ("t", "y", 2),
         ("x", "z", 4)
         }
    graph_directed_2 = GraphAdj(V, E)
    ssp_tree_2 = graph_directed_2.dijkstra("s")
    graph_directed_2.print_trv_state(ssp_tree_2)
    print("============= BellManFord Test P=============")
    V = {0, 1, 2, 3, 4, 5, 6}
    E = {(0, 1, 5), (1, 5, 8), (1, 2, 1),
         (1, 6, 2), (2, 6, 2), (4, 3, 1),
         (5, 3, 2), (5, 4, 2), (6, 5, 0)
         }
    graph_directed = GraphAdj(V, E)
    ssp_tree = graph_directed.bell_man_ford(0)
    graph_directed.print_trv_state(ssp_tree)
    print("============= Dijkstra Test P =============")
    V = {0, 1, 2, 3, 4, 5, 6}
    E = {(0, 1, 5), (1, 5, 8), (1, 2, 1),
         (1, 6, 2), (2, 6, 2), (4, 3, 1),
         (5, 3, 2), (5, 4, 2), (6, 5, 0)
         }
    graph_directed_2 = GraphAdj(V, E)
    ssp_tree_2 = graph_directed_2.dijkstra(0)
    graph_directed_2.print_trv_state(ssp_tree_2)
main()
