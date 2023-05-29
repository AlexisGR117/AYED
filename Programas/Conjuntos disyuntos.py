class DisjointSet:
    def __init__(self, data=[]):
        self.data = []
        for e in data:
            if not isinstance(e, set):
                self.make_set(e)
            else:
                self.insert(e)

    # Encuentra el conjunto cuyo elemento caracteristico es e
    def find_set(self, e):
        for st in self.data:
            if e in st:
                return st
        return None

    # Intancia un conjunto unitario con elemento caracteristico e
    # Siempre y cuando no exista ya un conjunto con esta caracteristica
    def make_set(self, e):
        st = self.find_set(e)  # Buscamos un conjunto caracteristico que contenga a e
        if st is None:
            self.data.append({e})

    # Une dos conjuntos cuyos elementos caracteristicos son X y Y
    def union(self, x, y):
        st1, st2 = self.find_set(x), self.find_set(y)
        # No existe un conjunto de alguno de los parametros
        if st1 is None:
            self.make_set(x)
            st1 = self.find_set(x)
        if st2 is None:
            self.make_set(y)
            st2 = self.find_set(y)
        # Son elementos caracteristicos de conjuntos distintos
        if st1 != st2:
            st3 = st1.union(st2)
            self.data.remove(st1)
            self.data.remove(st2)
            self.data.append(st3)

    def __str__(self):
        return str(self.data)

    # Recibe un conjutno por parametro y añade los elementos que no tenfan conjunto caracteristico
    def insert(self, st1):
        # Existe un conjunto referencia para alguno de los elementos
        st_copy = st1.copy()
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
        # Todos los elementos de st1 son representantes de un cojunto en data


def main():
    dj = DisjointSet([i for i in range(12)])
    print(dj)
    dj.union(8,5)
    print(dj)
    dj.union(8, 1)
    print(dj)
    dj.insert({0,2,3,15})
    print(dj)
    dj.insert({20,9,7,8,15})
    print(dj)
    dj2 = DisjointSet([{1,2,3,4}, {5,6,7,8}, {11,12,13,8}])
    print(dj2)


main()
