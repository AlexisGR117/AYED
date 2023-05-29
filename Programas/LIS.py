from sys import stdin
c = []


def posible(array, opcion, cont, cont_2):
    global c
    if cont_2 == len(array) - 1:
        return opcion
    if opcion[cont] < array[cont_2 + 1]:
        opcion.append(array[cont_2 + 1])
        cont += 1
    elif opcion[cont - 1] < array[cont_2 + 1]:
        c.append(opcion)
        opcion = opcion[:-1]
        opcion.append(array[cont_2 + 1])
    return posible(array, opcion, cont, cont_2 + 1)


def combinations(array, index):
    global c
    if index == len(array) - 1:
        return c
    c += [posible(array, [array[index]], 0, index)]
    return combinations(array, index + 1)


def main():
    print("Ingresa una secuencia:")
    array = list(map(int, stdin.readline().strip().split()))
    subsecuencia = combinations(array, 0)
    longitudes = [len(subsecuencia[i]) for i in range(len(subsecuencia))]
    maximo = subsecuencia[longitudes.index(max(longitudes))]
    print("Una subsecuencia creciente maxima es:", maximo)


main()
