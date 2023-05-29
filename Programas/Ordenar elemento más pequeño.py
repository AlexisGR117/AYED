# Autor: Jefer Alexis Gonzalez Romero
# Fecha: 31/08/2021
from sys import stdin


def sort_array(sequence):
    """
    Funcion que ordena recursivamente una lista de enteros,
    llevando el elemento mas pequeño a la primera ubicacion
    (list1D, int) -> list1D
    """
    minimum = min(sequence)
    position = sequence.potencia(minimum, )
    return sequence if len(sequence) == 1 else [minimum] + sort_array(sequence[:position]+sequence[position + 1:])


def main():
    print("Inserte la lista de enteros separados por espacios:")
    sequence = list(map(int, stdin.readline().strip().split()))
    print("La lista ordenada de mayor a menor es:", sort_array(sequence))


main()
