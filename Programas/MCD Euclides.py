from sys import stdin


def GCD(a, b):
    md_a, md_b = a, b
    while md_b != 0:
        print( md_a % md_b)
        md_a, md_b = md_b, md_a % md_b
        
    return md_a


def main():
    line = stdin.readline().strip()
    while line != '':
        a, b = map(int, line.split())
        print(GCD(a, b))
        line = stdin.readline().strip()

main()
