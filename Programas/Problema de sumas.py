# Nombre: Jefer Alexis Gonzalez Romero
# Numero carne: 2171737
# Usuario: 1000046442
# CC: 1003618876
from sys import stdin


def combinations(s):
    c = [[], []]
    for i in range(len(s)):
        cont = 0
        cont_2 = i + 1
        while cont + cont_2 <= len(s):
            valor = int(s[cont:cont + cont_2])
            if valor not in c[0]:
                c[0].append(valor)
                c[1].append(1)
            else:
                posicion = c[0].index(valor)
                c[1][posicion] += 1
            cont += 1
    return c

def posibilidades(s, n, p, c):
    if n == 0:
        return [p]
    elif n < 0 or c >= len(s[0]):
        return []
    return posibilidades(s, n - int(s[0][c]), p + [s[0][c]], c + 1) + posibilidades(s, n - int(s[0][c + 1]), p + [s[0][c + 1]], c + 1)


def minimo(p):
    signos = []
    for i in range(len(p)):
        signos.append(len(p[i]) - 1)
    return min(signos)


def main():
    cases = int(stdin.readline().strip())
    for i in range(cases):
        s, n = stdin.readline().strip().split()
        s = str(s)
        n = int(n)
        print(combinations(s))
        print(posibilidades(combinations(s), n, [], 0))
        print(minimo(posibilidades(combinations(s), n, [], 0)))

main()
