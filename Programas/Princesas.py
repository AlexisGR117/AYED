# Autor: Jefer Alexis Gonzalez Romero
from sys import stdin
import math


def buscar(alturas, principe):
    m = len(alturas) // 2
    if (len(alturas) == 1 and alturas[0] >= principe) or len(alturas) <= 0:
        return -math.inf
    if len(alturas) == 1 and alturas[0] < principe:
        return alturas[m]
    if alturas[m] < principe:
        return buscar(alturas[m:], principe)
    if alturas[m] >= principe:
        return buscar(alturas[:m], principe)


def main():
    princesas = int(stdin.readline().strip())
    alturas = list(map(int, stdin.readline().strip().split()))
    alturas.sort()
    consultas = int(stdin.readline().strip())
    principe = list(map(int, stdin.readline().strip().split()))
    for i in principe:
        respuesta = buscar(alturas, i)
        if respuesta == -math.inf:
            print("X")
        else:
            print(respuesta)

main()
