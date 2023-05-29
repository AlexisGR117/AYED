# Autor: Jefer Alexis Gonzalez Romero
from sys import stdin


def faltante(array, length):
    m = len(array) // 2
    if array[m] - array[m - 1] > 1:
        return int(array[m] - 1)
    return faltante(array[m:], length + m) if array[m] == length + m + 1 else faltante(array[:m + 1], length)


def main():
    print("Inserte los valores del arreglo separados por espacios:")
    array = list(map(int, stdin.readline().split()))
    print("El entero faltante es:", faltante(array, 0))


main()
