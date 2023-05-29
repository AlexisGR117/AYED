def mayor_repeticiones(cadena):
    """
    Funcion que dada una cadena da el caracter que mas se repite
    (str) -> str, int
    """
    caracteres = [[], []]
    for i in cadena:
        if i not in caracteres[0]:
            caracteres[0].append(i)
            caracteres[1].append(1)
        else:
            for j in range(len(caracteres[0])):
                if i == caracteres[0][j]:
                    caracteres[1][j] += 1
    mayor = caracteres[1][0]
    caracter = caracteres[0][0]
    for i in range(1, len(caracteres[1])):
        if caracteres[1][i] >= mayor:
                   mayor = caracteres[1][i]
                   caracter = caracteres[0][i]
    return caracter, mayor
def main():
    cadena = input()
    while cadena != "":
        caracter, mayor = mayor_repeticiones(cadena)
        print(caracter, " -> ", mayor)
        cadena = input()
main()
