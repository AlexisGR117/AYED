
from sys import stdin
from random import randint

SIZE_MAX = int(1e6)
MAX_INT = int(1e6)
MIN_INT = int(-1*1e6)
SEARCHES = 10

def getRandomSortedSecuence():
    return sorted(getRandomSecuence())

def getRandomSecuence():
    return [ randint(int(MIN_INT), int(MAX_INT)) for i in range(randint(1,SIZE_MAX))]

def binSearch(A, e, count = 0):
    mid = len(A)//2
    if (len(A) == 1 and A[mid] != e) or len(A) < 1:
        return (False,count)
    if A[mid] == e:
        return (True, count)
    return binSearch(A[:mid], e, count + 1) if e < A[mid] else binSearch(A[mid+1:], e, count + 1)

def main():
    seq = getRandomSortedSecuence()
    print('Generated a sequence with size', len(seq))
    for search in range(SEARCHES):
        query = randint(MIN_INT, MAX_INT)
        result = binSearch(seq, query)
        print('Searching ', query, ' in seq', ':', result)


main()