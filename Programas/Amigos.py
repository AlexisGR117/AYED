from sys import stdin
m = {}

def parejas(amigos, cont, s):
    if cont == amigos + 1:
        return s
    s.append([cont])
    for i in range(1, amigos + 1):
        if i > cont and [cont, i] not in s:
            s.append([cont, i])
        elif i < cont and [i, cont] not in s:
            s.append([i, cont])
    return parejas(amigos, cont + 1, s)


def formas(p, opcion, index, c):
    if c > len(p) - 1:
        return opcion
    if len(p[index]) == 1:
        if p[index][0] not in p[c]:
            return formas(p, opcion + [p[c]], index, c + 1)
        return formas(p, opcion, index, c + 1)
    if len(p[index]) == 2:
        if p[index][0] not in p[c] and p[index][1] not in p[c]:
            return formas(p, opcion + [p[c]], index, c + 1)
        return formas(p, opcion, index, c + 1)

def combinaciones(p, amigos, cont):
    c = 0
    for i in p:
        c += len(i)
    if c == amigos:
        p.sort(key=lambda x: x[0])
        return p
    r = formas(p, [p[cont]], cont, 0)
    return combinaciones(r, amigos, cont + 1)


def main():
    amigos = int(stdin.readline().strip())
    p = parejas(amigos, 1, [])
    p.sort(key=len)
    print(p)
    comb = []
    for i in range(len(p)):
        resultado = combinaciones(p, amigos, i)
        if resultado not in comb:
            print(resultado)
            comb.append(resultado)
    print("Formas de que los", amigos, "amigos pueden quedar solos o emparejados", comb)

main()
