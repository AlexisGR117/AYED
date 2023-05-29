from sys import stdin

def isPalindrome(s):
    ispal, index = True, 0
    while ispal and index < len(s)//2:
        ispal = s[index] == s[len(s)-(index+1)]
        index+=1
    return ispal

def main():
    line = stdin.readline().strip()
    while line != '':
        print(isPalindrome(line))
        line = stdin.readline().strip()
main()


