from sys import stdin
import math

ASCII_SIZE = 256

def findMaxOcurrencies(s):
    maxOcurr, charMaxOcurr = -math.inf, None
    ascii_dic = [ 0 for i in range(ASCII_SIZE)]
    for ci in s:
        ascii_dic[ord(ci)]+=1
        print(ascii_dic)
        if ascii_dic[ord(ci)] > maxOcurr :
            maxOcurr, charMaxOcurr = ascii_dic[ord(ci)], ci

    return charMaxOcurr + ' -> ' + str(maxOcurr)

def main():
    line = stdin.readline().strip()
    while line != '':
        print(findMaxOcurrencies(line))
        line = stdin.readline().strip()

main()


