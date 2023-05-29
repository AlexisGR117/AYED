from sys import stdin
from math import log


def hadamard_matrix(n, values):
    matrix = []
    cont = 0
    for i in range(n):
        row = []
        for j in range(n):
            row.append(values[cont])
            cont += 1
        matrix.append(row)
    return matrix


def hadamard(n, values):
    if log(n, 2) % 1 != 0:
        return "Imposible"
    else:
        matrix = hadamard_matrix(n, values)
        if n == 1:
            if matrix[0][0] == "T":
                return "Hadamard"
            else:
                return "No Hadamard"
        for i in range(1, n):
            cont = 0
            for j in range(n):
                if matrix[i][j] != matrix[i - 1][j]:
                    cont += 1
            if cont != n // 2:
                return "No Hadamard"
    return "Hadamard"


def main():
    n = int(stdin.readline().strip())
    values = stdin.readline().strip().split()
    print(hadamard(n, values))


main()
