def matriz_ceros(numero):
    """
    Funcion que dado un numero n da una matriz de nxn llena de ceros
    (int) -> list 2D
    """
    matriz = []
    for i in range((numero*2)-1):
        matriz.append([])
        for j in range((numero*2)-1):
            matriz[i].append(0)
    return matriz
def llenar(matriz, numero):
    """
    Funcion que dado un numero n da el wondersquare de n
    (list 2D, int) -> list2D
    """
    numero2 = (numero*2)-2
    for i in range(numero):
        for j in range(i, numero2+1):
            matriz[i][j] = numero
            matriz[numero2][j] = numero
        for k in range(i+1, numero2+1):
            matriz[k][i] = numero
            matriz[k][numero2] = numero
        numero2 -= 1
        numero -= 1
    return matriz
def main():
    numero = int(input())
    matriz = matriz_ceros(numero)
    wondersquare = llenar(matriz, numero)
    for i in wondersquare:
        j = -1
        for j in range(len(i)-1):
            print(i[j], end = " ")
        print(i[j + 1], end = "")
        print()
main()
