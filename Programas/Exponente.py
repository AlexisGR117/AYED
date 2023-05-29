# Autor: Jefer Alexis Gonzalez Romero
from sys import stdin


def potencia(number, index, cont, resultado):
    return resultado if cont == index else potencia(number, index, cont + 1, resultado * number)


def main():
    print("Inserte la base y el exponente separado por un espacio:")
    number, index = list(map(int, stdin.readline().split()))
    print("La potencia es:", potencia(number, index, 0, 1))


main()
