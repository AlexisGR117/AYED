from sys import stdin


def merge(one, two):
    cont = 0
    index_left, index_right = 0, 0
    result_array = []
    while index_left < len(one) and index_right < len(two):
        if one[index_left] < two[index_right]:
            result_array.append(one[index_left])
            index_left += 1
        else:
            result_array.append(two[index_right])
            index_right += 1
            cont += len(one) - index_left
    if index_left < len(one):
        result_array += one[index_left:]
    if index_right < len(two):
        result_array += two[index_right:]

    return result_array, cont


def merge_sort(one):
    if len(one) <= 1:
        return one[:], 0
    mid = len(one) // 2
    left_one = merge_sort(one[:mid])
    right_one = merge_sort(one[mid:])
    merged = merge(left_one[0], right_one[0])
    cont = left_one[1] + right_one[1] + merged[1]
    return merged[0], cont


def main():
    length = int(stdin.readline().strip())
    while length != 0:
        sequence = [int(stdin.readline().strip()) for i in range(length)]
        print(merge_sort(sequence)[1])
        length = int(stdin.readline().strip())


main()
