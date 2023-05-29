from sys import stdin


def problema_sumas(s, n, index):
    if n == 0:
        return 1
    elif n < 0:
        return problema_sumas(s, n + int(s[index - 1]), index)
    elif index + 1 > len(s):
        return 0
    return problema_sumas(s, n - int(s[index]), index + 1)


def main():
    case = list(map(int, stdin.readline().strip().split()))
    while case[0] != 0 and case[1] != 0:
        n = case[0]
        valores = case[1]
        lista = case[2:]
        sumas = 0
        for j in range(valores):
            sumas += problema_sumas(lista, n, j)
        print("Sums of " + str(n) + ":")
        if sumas == 0:
            print("NONE")
        else:
            print(sumas)
        case = list(map(int, stdin.readline().strip().split()))


main()
