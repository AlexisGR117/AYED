from sys import stdin
m = {}

def monedas_memo(n, caso, m):
    print(m)
    if (n, caso) in m:
        return m[(n, caso)]
    m[(n, caso)] = monedas(n, caso, m)
    return m[(n, caso)]


def monedas(n, caso, m):
    if n < 1:
        return [caso]
    return monedas_memo(n - 1, caso + "C", m) + monedas_memo(n - 1, caso + "S", m)


def main():
    n = stdin.readline().strip()
    while n != "":
        n = int(n)
        print(monedas(n, "", m))
        n = stdin.readline().strip()

main()