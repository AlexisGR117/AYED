# Cuente numeros primos entre 0 y un numero

from sys import stdin


def numero_primo(numero, primos):
    cont = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            cont += 1
    if cont == 2:
        primos += 1
    return primos if numero <= 1 else numero_primo(numero - 1, primos)


def main():
    number = int(stdin.readline().strip())
    print(numero_primo(number, 0))


main()
