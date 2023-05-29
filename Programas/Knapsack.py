from sys import stdin
import math
pe = [1, 1, 2, 4, 12]
pr = [1, 2, 2, 10, 4]


def combinations(c, i, t_pe, t_pr):
    if c == 0:
        return [[t_pe, t_pr]]
    elif c < 0 or i >= len(pe):
        return []
    return combinations(c - pe[i], i, t_pe + [pe[i]], t_pr + [pr[i]]) + combinations(c, i + 1, t_pe, t_pr)

def main():
    print("Ingresa la capacidad que tiene la mochila:")
    capacidad = int(stdin.readline().strip())
    combinaciones = combinations(capacidad, 0, [], [])
    maximo = -math.inf
    mejor = [[], []]
    for i in combinaciones:
        precio = 0
        for j in i[1]:
            precio += j
        if precio >= maximo:
            maximo = precio
            mejor = [i[0]] + [i[1]]
    casos = [[], []]
    for i in range(len(mejor[0])):
        if str(mejor[0][i]) + str(mejor[1][i]) not in casos[0]:
            casos[0].append(str(mejor[0][i]) + str(mejor[1][i]))
            casos[1].append(1)
        else:
            posicion = casos[0].index(str(mejor[0][i]) + str(mejor[1][i]))
            casos[1][posicion] +=1
    print("Para maximizar las ganancias para una capacidad de", capacidad, "se necesitan los siguientes objetos:")
    for i in range(len(casos[1])):
        print("Del que pesa", casos[0][i][0], "y cuesta", casos[0][i][1:], "se necesitan", casos[1][i])


main()
