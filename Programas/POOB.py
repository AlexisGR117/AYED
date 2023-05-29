import math
from queue import Queue
from random import randint
import heapq  # Python library for Max-heap y Min-heap, priority queue, deafult is Min Heap

GRAY = "GRAY"
WHITE = "WITHE"
BLACK = "BLACK"


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
    undirected_graph = GraphAdj({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13},
                                {(1, 8, 101), (1, 9, 30), (1, 2, 100), (1, 3, 100), (2, 4, 75), (2, 5, 70), (2, 6, 82), (2, 7, 77), (3, 10, 73), (3, 11, 69), (3, 12, 83), (3, 13, 79)},
                                True
                                )
    print("Adjacency - LIST")
    undirected_graph.print_data()
    print(undirected_graph.get_neighbors(1))
    print(undirected_graph.get_near_by_arcs(1))
    state_result_dfs = undirected_graph.dfs()
    undirected_graph.print_trv_state(state_result_dfs)
main()

