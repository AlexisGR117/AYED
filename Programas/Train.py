from sys import stdin


def swapping(length, permutation):
    a = 0
    b = 1
    swaps = 0
    while b < length:
        if permutation[b] < permutation[a]:
            highest = permutation[a]
            lower = permutation[b]
            permutation = permutation[:a] + [lower] + [highest] + permutation[b + 1:]
            swaps += 1
        if a >= 1 and permutation[a - 1] > permutation[a]:
            a -= 2
            b -= 2
        b += 1
        a += 1
    return swaps


def main():
    cases = int(stdin.readline().strip())
    for i in range(cases):
        length = int(stdin.readline().strip())
        permutation = list(map(int, stdin.readline().strip().split()))
        s = swapping(length, permutation)
        print("Optimal train swapping takes", s, "swaps.")


main()
