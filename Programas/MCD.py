def primos(numero):
    """
    Funcion que dado un numero da los numeros primos que hay hasta este
    (int) -> list1D
    """
    primos = []
    for i in range(1, numero+1):
        cont = 0
        numeros = []
        for j in range(1, i+1):
            if i % j == 0:
                numeros.append(j)
                cont += 1
        if cont == 2:
            primos.append(i)
    return primos
def descomposicion(numero, primos):
    """
    Funcion que descompone un numero en numeros primos
    (int, list1D) -> list1D
    """
    cont = 0
    division = []
    while numero != 1:
        if numero % primos[cont] == 0:
            numero = numero // primos[cont]
            division.append(primos[cont])
        else:
            cont += 1
    return division
def apariciones(division):
    """
    Funcion que dada una lista da una matriz donde la priera fila
    son sus elementos sin repetir y en la segunda fila el
    numero de veces que aparecen
    (list1D) -> list2D
    """
    veces = [[], []]
    for i in division:
        if i not in veces[0]:
            veces[0].append(i)
            veces[1].append(1)
        else:
            for j in range(len(veces[0])):
                if i == veces[0][j]:
                    veces[1][j] += 1
    return veces
def mcd(aparicion1, aparicion2):
    """
    Funcion que dada la descomposcicion de dos numeros da el mcd de estos
    (list2D, list2D) -> int
    """
    bases_comunes = [[], []]
    for i in range(len(aparicion1[0])):
        for j in range(len(aparicion2[0])):
            if aparicion1[0][i] == aparicion2[0][j]:
                bases_comunes[0].append(aparicion1[0][i])
                if aparicion1[1][i] > aparicion2[1][j]:
                    bases_comunes[1].append(aparicion1[1][j])
                else:
                    bases_comunes[1].append(aparicion1[1][i])
    multiplicacion = 1
    for i in range(len(bases_comunes[0])):
        multiplicacion *= bases_comunes[0][i] ** bases_comunes[1][i]
    return multiplicacion
def main():
    numeros = input()
    while numeros != "":
        numero1, numero2 = numeros.split()
        numero1 = int(numero1)
        numero2 = int(numero2)
        primos1 = primos(numero1)
        primos2 = primos(numero2)
        division1 = descomposicion(numero1, primos1)
        division2 = descomposicion(numero2, primos2)
        aparicion1 = apariciones(division1)
        aparicion2 = apariciones(division2)
        print(mcd(aparicion1, aparicion2))
        numeros = input()
main()
