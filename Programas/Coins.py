from sys import stdin
import itertools

def coins(N, e):
    return set([e]) if N == 0 else coins(N-1, e + 'C').union(coins(N-1, e + 'S'))


def coinsSet(N):
    return set(itertools.product({'C', 'S'}, coinsSet(N-1))) if N > 1 else {'C', 'S'}

def tupleToString(tp):
    if isinstance(tp, tuple):
        if isinstance(tp[1], tuple):
            return str(tp[0]) + tupleToString(tp[1])
        else:
            return str(tp[0]) + str(tp[1])
    else:
        return tp


def main():
    n = stdin.readline().strip()
    while n != '':
        print(coins(int(n), ''))
        print(set(map(tupleToString, coinsSet(int(n)))))
        n = stdin.readline().strip()
main()

