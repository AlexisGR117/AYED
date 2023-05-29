# Autor: Jefer Alexis Gonzalez Romero
from sys import stdin


def super_digit(number):
    """
    Funcion encuentra el super digito de un numero
    (int) -> str
    """
    suma = 0
    for i in number:  # Ciclo de la invariante
        suma += int(i)
    number = str(suma)
    return number if len(number) == 1 else super_digit(number)


def concatenate(n, k):
    """
    Funcion que concatena el string n k veces
    (int, int) -> str
    """
    string = ''
    for i in range(k):
        string += n
    return string


def main():
    numbers = stdin.readline().strip()
    while numbers != '':
        n, k = list(map(int, numbers.split()))
        print(super_digit(concatenate(str(n), k)))
        numbers = stdin.readline().strip()


main()
