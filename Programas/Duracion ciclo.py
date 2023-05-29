# Autor: Jefer Alexis Gonzalez Romero
from sys import stdin
import math


def cycle_length(i):
    """
    Funcion que encuentra la duracion del ciclo para el entero i
    (int, int) -> int
    """
    length = 1
    while i > 1:  # Ciclo de la invariante #1
        if i % 2 == 0:
            i = i // 2
        else:
            i = i * 3 + 1
        length += 1
    return length


def max_length(i, j):
    """
    Funcion que da la maxima duracion del ciclo de los enteros entre i y j.
    (int, int, int) -> int
    """
    mayor = -math.inf
    for k in range(i, j + 1):  # Ciclo de la invariante #2
        new = cycle_length(k)
        if new > mayor:
            mayor = new
    return mayor


def main():
    numbers = stdin.readline().strip()
    while numbers != '':
        i, j = list(map(int, numbers.split()))
        if i > j:
            print(i, j, max_length(j, i))
        else:
            print(i, j, max_length(i, j))
        numbers = stdin.readline().strip()


main()
