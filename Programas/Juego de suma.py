from sys import stdin
import math

def findMinimumSimbols(s,p,  symbols):
    if p == int(s):
        return symbols
    if p < 0:
        return math.inf
    #Make a cut
    mx = math.inf
    for i in range(1,len(s)):
        cut = s[0:i]
        mx = min(mx, findMinimumSimbols( s[i:len(s)], p - int(cut) , symbols+1))
    return mx

def solve(s,p):
    solution = findMinimumSimbols(s,int(p),0)
    print( -1 if solution == math.inf else solution )

def main():
    cases = int(stdin.readline().strip())
    for i in range(cases):
        s,p =  stdin.readline().strip().split()
        solve(s,int(p))
main()