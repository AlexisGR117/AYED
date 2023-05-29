from time import time
from sys import stdin



def fibo(n):
    return 1 if n <= 1 else fibo(n-1) + fibo(n-2)

def fiboM(n, M):
    return 1 if n <= 1 else fiboMemo(n - 1, M) + fiboMemo(n - 2, M)

# [] -> .........
# [None, None, None, ........] -> [n] is not None
def fiboMemo(n,M):
    #print(n, 'Before', M)
    if not M[n] is None:
        #print(n, 'Got Value', M)
        return M[n]
    M[n] = fiboM(n,M)
    #print(n, 'After', M)
    return M[n]

def fiboMemoDinamic(n,M):
    #print(n, 'Before', M)
    if len(M) > n:
        #print(n, 'Got Value', M)
        return M[n]
    diff = n - len(M)
    M+= [ None for i in range(diff + 1)]
    M[n] = fiboM(n,M)
    #print(n, 'After', M)
    return M[n]

def main():
    #Memoria Estatica
    M = [ None for i in range(255)]
    M_dinamic = []
    line = stdin.readline().strip()
    while line != '':
        n = int(line)
        #t_0 = time()
        #result = fibo(n)
        #t_1 = time()
        #print(result, '--> time:', t_1 - t_0)
        #t_2 = time()
        #result_mem = fiboMemo(n, M)
        #t_3 = time()
        #print(result_mem, '--> time:', t_3 - t_2, M)
        t_4 = time()
        result_mem_dinamic = fiboMemoDinamic(n, M_dinamic)
        t_5 = time()
        print(result_mem_dinamic, '--> time:', t_5 - t_4, M_dinamic)
        line = stdin.readline().strip()

main()

