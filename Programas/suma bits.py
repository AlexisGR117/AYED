# Autor: Jefer Alexis Gonzalez Romero
from sys import stdin
import math


def binary(number, bits):
    index = math.log(number, 2) // 1
    bits += 1
    number -= 2 ** index
    return bits if number == 0 else binary(number, bits)


def sum_bits(number, suma, cont):
    suma += binary(cont, 0)
    return cont if suma >= number else sum_bits(number, suma, cont + 1)


def main():
    print("Inserte un numero entero positivo:")
    number = int(stdin.readline().strip())
    print("El numero N tal que la suma de los bits de cada numero desde 1 hasta N sea al menos el numero dado es:")
    print(sum_bits(number, 0, 1))


main()
