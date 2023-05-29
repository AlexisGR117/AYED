# Autor: Jefer Alexis Gonzalez Romero
# Fecha: 31/08/2021
from sys import stdin


def sum_evens(number, cont):
    """
    Funcion recursiva que da la suma de los numeros pares positivos
    desde un numero N dado hasta 2, incluyendo a N si es par y a 2
    (list1D, int) -> int
    """
    return cont if number <= 2 else sum_evens(number - 2, cont + number)


def main():
    print("Inserte un numero N entero:")
    number = int(stdin.readline().strip())
    if number % 2 != 0:
        number = number - 1
    print("EL resultado de la suma de los numeros pares positivos desde N hasta 2 es:", sum_evens(number, 2))


main()
