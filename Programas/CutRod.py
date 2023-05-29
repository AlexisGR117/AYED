import math


def cutRod(L, cortes, answer):
    if L < min(cortes.keys()):
        #print(answer)
        return 0
    max_profit = -math.inf
    for corte in cortes.keys():
        if corte <= L:
            max_profit = max( max_profit, cortes[corte] + cutRod(L-corte, cortes, answer + [corte]))
    return max_profit

def cutRodM(L, cortes, M):
    if L < min(cortes.keys()):
        return 0
    max_profit = -math.inf
    for corte in cortes.keys():
        if corte <= L:
            max_profit = max( max_profit, cortes[corte] + cutRodMemo(L-corte, cortes, M))

    return max_profit

def cutRodMemo(L, cortes, answer, M):
    if L in M.keys():
        return M[L]
    M[L] = cutRodM(L, cortes, answer, M)
    return M[L]

def main():
    cortes = {  2 : -1, 10 : 5, 125: 15}
    M = {}
    print('================ Solving Problem Recursively ====================')
    print(cutRod(40, cortes, []))
    print('================ Solving Problem Recursively with Memory====================')
    result = cutRodMemo(40, cortes, [], M)
    print(result[0])
    #for key in M:
        #print(key, M[key])

main()