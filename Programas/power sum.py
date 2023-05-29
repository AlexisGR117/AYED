# Autor: Jefer Alexis Gonzalez Romero
from sys import stdin
cont = 0

def power_sum(x, n, base):
    """
    Funcion que encuentra el numero de formas para obtener un entero dado
    expresado como la suma de potencias de n
    (int, int, int) -> int
    """
    global cont
    cont += 1
    if x == 0 or base ** n == x:
        return 1
    if x < 0 or base ** n > x:
        return 0
    return power_sum(x - base ** n, n, base + 1) + power_sum(x, n, base + 1)


def main():
    x = stdin.readline().strip()
    n = stdin.readline().strip()
    while x != '' or n != '':
        global cont
        cont = 0
        print(power_sum(int(x), int(n), 1))
        x = stdin.readline().strip()
        n = stdin.readline().strip()


main()
