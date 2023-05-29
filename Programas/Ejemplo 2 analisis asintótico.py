from sys import stdin

# pre: seq is sorted
# ele must be sorted into seq

# Peor Caso : len(seq) ---> N
def sortElement( seq, ele):                             #Cost    times
    index = 0                                           #c1        1
    while index < len(seq) and seq[index] < ele:        #c2        n + 1
        index+=1                                        #c3        n
    return seq[:index] + [ele] + seq[index:]            #c4       1 + 2*n
                                                        #T(n) = c1 + c2(n+1) + c3 n + c4(1+2*n)
                                                        #T(n) = O(n)

# Mejor Caso : len(seq) ---> N
def sortElement( seq, ele):                             #Cost    times
    index = 0                                           #c1        1
    while index < len(seq) and seq[index] < ele:        #c2        1
        index+=1                                        #c3        0
    return seq[:index] + [ele] + seq[index:]            #c4        1 + n
                                                        #T(n) = Ω(n)


# Peor Caso : len(seq) ---> N
def insertionSort(seq):                                                                         #Cost    times
    sortedSeq = seq[:]                                                                          # c1       1 + n
    for index in range(len(sortedSeq)):                                                         # c2       n + 1
        sortedSeq = sortElement( sortedSeq[:index], sortedSeq[index] ) + sortedSeq[index+1:]    # c3       n * ( 1 + 2*n + O(sortElement) )

    return sortedSeq                                                                            # c4       1
                                                                                                # T(n) = c1(1+n) + c2(n+1) + c3 ( n * ( 1 + 2*n + O(sortElement) ) )
                                                                                                # T(n) = c1(1+n) + c2(n+1) + c3 ( n * ( 1 + 2*n + n ) )
                                                                                                # T(n) = O(n^2)


# Mejor Caso : len(seq) ---> N
def _insertionSort(seq):                                                                         # Cost    times
    sortedSeq = seq[:]                                                                          # c1       1 + n
    for index in range(len(sortedSeq)):                                                         # c2       n + 1
        sortedSeq = sortElement(sortedSeq[:index], sortedSeq[index]) + sortedSeq[index + 1:]    # c3       n * ( 1 + 2*n + Ω(sortElement) )

    return sortedSeq                                                                            # c4       1
                                                                                                # T(n) = c1(1+n) + c2(n+1) + c3 ( n * ( 1 + 2*n + Ω(sortElement) ) )
                                                                                                # T(n) = c1(1+n) + c2(n+1) + c3 ( n * ( 1 + 2*n + n ) )
                                                                                                # T(n) = Ω(n^2)

# Peor Caso : len(seq) ---> N
# https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
def _insertionSort(seq):                                                                            # Cost            Times
    sortedSeq = seq[:]                                                                              #  c1(slice=O(n))    1 + n
    for index in range(len(sortedSeq)):                                                             #  c2              n + 1
        index = 0                                                                                   #  c3                n
        while index < len(sortedSeq[:index]) and sortedSeq[:index][index] < sortedSeq[index]:       #  c4             n  * (n) + 2*n
            index += 1                                                                              #  c5             n  * (n-1)
        sortedSeq = sortedSeq[:index][:index] + [sortedSeq[index]] + sortedSeq[:index][index:]      #  c6             n + 4*n
    return sortedSeq                                                                                #  c7                1
                                                                                                    # T(n) = c1(1 + n) + c2(n+1) + c3(n) + c4*(n^2 + 2n) + c5 * (n^2 - n) + c6 ( 5n ) + c7
                                                                                                    # T(n) = O(n^2)
# [1,2,3,4,5,6,7,8,9] [10] : (n-1) + 1

# Mejor Caso : len(seq) ---> N
# https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt
def __insertionSort(seq):                                                                            # Cost            Times
    sortedSeq = seq[:]                                                                              #  c1(slice=O(n))    1 + n
    for index in range(len(sortedSeq)):                                                             #  c2              n + 1
        index = 0                                                                                   #  c3                n
        while index < len(sortedSeq[:index]) and sortedSeq[:index][index] < sortedSeq[index]:       #  c4               1
            index += 1                                                                              #  c5               0
        sortedSeq = sortedSeq[:index][:index] + [sortedSeq[index]] + sortedSeq[:index][index:]      #  c6             n + 4*n
    return sortedSeq                                                                                #  c7                1
                                                                                                    # T(n) = c1(1 + n) + c2(n+1) + c3(n) + c4*(1) + c5 * (0) + c6 ( 5n ) + c7
                                                                                                    # T(n) = Ω(n)
# [1,2,3,4,5] [0] : (n-1) + 1



def main():
    line = stdin.readline().strip()
    while line != '':
        elements = list(map(int,line.split()))
        print(insertionSort(elements))
        line = stdin.readline().strip()

main()
