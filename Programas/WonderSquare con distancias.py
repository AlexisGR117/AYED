from sys import stdin

def printWonderSquare(mat):
    for line in mat:
        print(' '.join(map(str,line)))

def distanceToCenter(i,j,ln):
    i_center, j_center = ln//2, ln//2
    distance = max(abs(i-i_center), abs(j-j_center)) + 1
    return distance

def wonderSquare(n):
    ln = 2*n-1
    mat = [[ distanceToCenter(i,j,ln) for j in range(ln)] for i in range(ln)]
    return mat

def main():
    line = stdin.readline().strip()
    while line != '':
        n = int(line)
        printWonderSquare(wonderSquare(n))
        line = stdin.readline().strip()
main()


