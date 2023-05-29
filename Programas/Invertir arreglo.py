# Autor: Jefer Alexis Gonzalez Romero
# Fecha: 04/09/2021
from sys import stdin


def invert(matrix):
    """
    Funcion recursiva que invierte los numeros de un arreglo
    (list1D) -> list1D
    """
    return matrix if len(matrix) == 1 else [matrix[-1]] + invert(matrix[: -1])


def main():
    print("Inserte los valores del arreglo separados por espacios:")
    matrix = list(map(int, stdin.readline().strip().split()))
    if len(matrix) > 1:
        print("El arreglo invertido es:", invert(matrix))
    else:
        print("El arreglo invertido es:", matrix)

main()
