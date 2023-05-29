from sys import stdin


def combinations(change):
    coins = [1, 5, 10, 25, 50]
    ways = 1
    while change % 5 != 0:
        change -= 1
    if change == 0:
        return ways
    ways += change // 5
    print(ways)
    if change % 10 != 0:
        ways += (((change - 5) // 10) ** 2) + 1 * ((change - 5) // 10)
    else:
        ways += (change // 10) ** 2
    print(ways)
    return change, ways


def main():
    change = int(stdin.readline().strip())
    while change != '':
        print(combinations(change))
        change = int(stdin.readline().strip())


main()
