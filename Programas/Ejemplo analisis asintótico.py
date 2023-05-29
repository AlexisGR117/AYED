from sys import stdin
# len(S) --> N
def isPalindrome(s):                                #Cost    Times
    ispal, index = True, 0                          #c1        1
    while ispal and index < len(s)//2:              #c2       n/2 + 1
        ispal = s[index] == s[len(s)-(index+1)]     #c3       n/2
        index+=1                                    #c4       n/2
    return ispal                                    #c5        1
                                                    # T(n) = c1 + c2(n/2 + 1) + c3(n/2) + c4(n/2) + c5
                                                    # T(n) = n*[(c2/2) + (c3/2) + (c4/2)] + (c1 + c2 + c5)
                                                    # T(n) = a*n + b = O(n)

# len(S) --> N
def _isPalindrome(s):                                #Cost    Times
    ispal, index = True, 0                          #c1        1
    while ispal and index < len(s)//2:              #c2        2
        ispal = s[index] == s[len(s)-(index+1)]     #c3       1
        index+=1                                    #c4       1
    return ispal                                    #c5        1
                                                    # T(n) = c1 + 2*c2 + c3 + c4 + c5
                                                    # T(n) = b
                                                    # T(n) = b = Ω(1)
def main():
    line = stdin.readline().strip()
    while line != '':
        print(isPalindrome(line))
        line = stdin.readline().strip()
main()


