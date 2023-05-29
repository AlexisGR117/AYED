# Autor: Jefer Alexis Gonzalez Romero
# Fecha: 31/08/2021
from sys import stdin


def sum_sub_array(list_l, i, j, suma):
    """
    Funcion recursiva que da la suma de un subarreglo de N enteros
    (list1D, int, int, int) -> int
    """
    return suma if i - 1 == j else sum_sub_array(list_l, i + 1, j, suma + list_l[i])


def main():
    print("Inserte la lista de enteros separados por espacios:")
    list_l = list(map(int, stdin.readline().strip().split()))
    print("Introduzca los indices que limitan el subarreglo separados por un espacio:")
    i, j = list(map(int, stdin.readline().strip().split()))
    if i > j:
        mayor = i
        i = j
        j = mayor
    print("EL resultado de la suma del subarreglo es:", sum_sub_array(list_l, i, j, 0))


main()
