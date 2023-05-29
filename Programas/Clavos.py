from sys import stdin


def recorrido(camino, posicion, velocidad):
    if posicion > len(camino) - 1:
        return recorrido(camino[::-1], posicion - len(camino) + 1, velocidad)
    if velocidad == 0:
        return True
    if camino[posicion] == "F":
        return False
    return recorrido(camino, velocidad + posicion, velocidad - 1)


def main():
    print("Ingresa el camino de clavos (sin espacios y con mayusculas):")
    camino = stdin.readline().strip()
    print("Ingresa la posicion desde la cual quiere empezar el recorrido:")
    posicion = int(stdin.readline().strip())
    print("Velocidad inicial:")
    velocidad = int(stdin.readline().strip())
    resultado = recorrido(camino, posicion - 1, velocidad)
    if resultado == False:
        print("No es posible detenerse sin tener que pisar un clavo")
    else:
        print("Es posible detenerse sin tener que pisar un clavo")

main()
