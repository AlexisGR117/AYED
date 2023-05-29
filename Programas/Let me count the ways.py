from sys import stdin
coins = [1, 5, 10, 25, 50]
m = {}
max_bound = 30001


def combinations(change, index, m):
    if change == 0:
        return 1
    elif change < 0 or index >= len(coins):
        return 0
    return combinations_memo(change - coins[index], index, m) + combinations_memo(change, index + 1, m)


def combinations_memo(change, index, m):
    if (change, index) in m.keys():
        return m[(change, index)]
    m[(change, index)] = combinations(change, index, m)
    return m[(change, index)]


def main():
    change = stdin.readline().strip()
    for i in range(max_bound):
        combinations_memo(i, 0, m)
    print(m)
    while change != '':
        change = int(change)
        ways = m[(change, 0)]
        if ways == 1:
            print("There is only 1 way to produce {} cents change.".format(change))
        else:
            print("There are {} ways to produce {} cents change.".format(ways, change))
        change = stdin.readline().strip()


main()
