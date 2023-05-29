from sys import stdin
import math


def knapM(w, weights, resp, M):
    if w < min(weights.keys()):
        return 0
    max_price = -math.inf
    for weight in weights.keys():
        if weight <= w:
            max_price = max(max_price, weights[weight] + knapMemo(w - weight, weights, resp + [weight], M))

    return max_price


def knapMemo(w, weights, resp, M):
    if w in M.keys():
        return M[w]
    M[w] = knapM(w, weights, resp, M)
    return M[w]


def main():
    M = {}
    weights = {1: 1, 2: 2, 12: 4, 4: 10}
    result = knapMemo(15, weights, [], M)
    print(result)


main()
