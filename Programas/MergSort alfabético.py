# Autor: Jefer Alexis Gonzalez Romero
from sys import stdin


def merge(one, two):
    index_left, index_right = 0, 0
    result_array = []
    while index_left < len(one) and index_right < len(two):
        if one[index_left] < two[index_right]:
            result_array.append(one[index_left])
            index_left += 1
        else:
            result_array.append(two[index_right])
            index_right += 1
    if index_left < len(one):
        result_array += one[index_left:]
    if index_right < len(two):
        result_array += two[index_right:]

    return result_array


def merge_sort(one):
    if len(one) <= 1:
        return one[:]
    mid = len(one) // 2
    left_one = merge_sort(one[:mid])
    right_one = merge_sort(one[mid:])
    merged = merge(left_one, right_one)
    return merged


def main():
    print("Inserte la cadena de letras:")
    string = stdin.readline().strip()
    print("El arreglo con las letras ordenadas de la cadena dada es:", merge_sort(string))


main()
