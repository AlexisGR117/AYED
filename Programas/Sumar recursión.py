from sys import stdin


def sumarCola(A):
    return 0 if len(A) == 0 else A[0] + sumarCola(A[1:])

def sumarHelper(A):
    return sumarPila(0,0,len(A), A)

def sumarPila(acum, index, N, A):
    return acum if index == N else sumarPila(acum + A[index], index + 1, N, A)

def main():
    A = list(map(int,stdin.readline().strip().split()))
    print(A)
    print(sumarCola(A))
    print(sumarHelper(A), sumarPila(0, 4, 6, A))   # Sumar de forma creciente en un rango [)

main()