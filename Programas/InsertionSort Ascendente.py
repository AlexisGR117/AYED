from sys import stdin


def sort_element(seq, ele):
    index = 0
    while index < len(seq) and seq[index] < ele:
        index += 1
    return seq[:index] + [ele] + seq[index:]


def insertion_sort(seq):
    sorted_seq = seq[:]
    for index in range(len(sorted_seq)):
        print(sorted_seq)
        sorted_seq = sort_element(sorted_seq[:index], sorted_seq[index] ) + sorted_seq[index+1:]
    return sorted_seq


def main():
    line = stdin.readline().strip()
    while line != '':
        elements = list(map(int, line.split()))
        print(insertion_sort(elements))
        line = stdin.readline().strip()

main()
