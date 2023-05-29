# Autor: Jefer Alexis Gonzalez Romero
from sys import stdin


def menor(array):
    middle = len(array) // 2
    if len(array) == 1:
        return int(array[0])
    if 0 < middle < len(array) - 1:
        if array[middle - 1] >= array[middle] and array[middle + 1] >= array[middle]:
            return array[middle]
    elif middle == 0:
        if array[middle + 1] >= array[middle]:
            return array[middle]
        else:
            return array[middle + 1]
    elif middle == len(array) - 1:
        if array[middle - 1] >= array[middle]:
            return array[middle]
        else:
            return array[middle - 1]
    return menor(array[:middle + 1]) if array[middle + 1] > array[middle] else menor(array[middle:])


def main():
    print("Inserte los valores del arreglo separados por espacios:")
    array = list(map(int, stdin.readline().split()))
    print("El menor numero en el arreglo es:", menor(array))


main()
