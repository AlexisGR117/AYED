# Nombre: Jefer Alexis González Romero
# Carnet institucional: 2171737
# CC 1003618876
# Usuario: 1000046442

from sys import stdin

m = {}


def memo(n, back, m):
    if (n, back) in m:
        return m[(n, back)]
    m[(n, back)] = trib(n, back, m)
    return m[(n, back)]


def trib(n, back, m):
    if n <= 0:
        return 1
    if n == 1:
        return 1
    acum = 0
    for i in range(1, back + 1):
        acum = acum + memo(n - i, back, m)
    return acum


def main():
    linea = stdin.readline().strip()
    cont_2 = 0
    while linea != "":
        n, back = linea.split()
        cont_2 += 1
        if int(n) > 1:
            rta = trib(int(n), int(back), m) + 2 ** (int(n) - 2)
        else:
            rta = trib(int(n), int(back), m)
        print("Case {}: {}".format(cont_2, rta))
        linea = stdin.readline().strip()


main()
