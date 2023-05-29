# Autor: Jefer Alexis Gonzalez Romero
# Fecha: 04/09/2021
from sys import stdin
import math


def binary(number, transformation, index):
    """
    Funcion recursiva que tranforma un número entero positivo a notacion binaria
    (int) -> str
    """
    index_2 = math.log(number, 2) // 1
    while index - index_2 > 1:  # Ciclo de la invariante #1
        transformation += '0'
        index -= 1
    transformation += '1'
    number -= 2 ** index_2
    return transformation if number == 0 else binary(number, transformation, index_2)  # Ciclo de la invariante #2


def main():
    print("Inserte un numero entero positivo:")
    number = int(stdin.readline().strip())
    transformation = binary(number, '', 0)
    if number % 2 == 0:
        while len(transformation) != math.log(number, 2) // 1 + 1:  # Ciclo de la invariante #3
            transformation += '0'
    print("Numero en notacion binaria:", transformation)


main()
