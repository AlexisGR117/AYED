from sys import stdin




def merge(one, two):                                            # Cost      Times
    index_left, index_right = 0, 0                              # c1          1
    result_array = []                                           # c2          1
    while index_left < len(one) and index_right < len(two):     # c3        n + 1
        if one[index_left] < two[index_right]:                  # c4          n
            result_array.append(one[index_left])                # c5          n
            index_left += 1                                     # c6          n
        else:                                                   # c7          n
            result_array.append(two[index_right])               # c8          0
            index_right += 1                                    # c9          0
    if index_left < len(one):                                   # c10         1
        result_array += one[index_left:]                        # c11         0
    if index_right < len(two):                                  # c12         1
        result_array += two[index_right:]                       # c13         n
    return result_array                                         # c14         1
                                                                # T(n) = c1 + c2 + c3(n + 1) + c4(n) + c5(n) + c6(n)
                                                                #        c7(n) + c10 + c12 + c13(n) + c14
                                                                # T(n) = a(n) + b = O(n)


def main():
    one = list(map(int, stdin.readline().split()))
    two = list(map(int, stdin.readline().split()))
    print(merge(one, two))


main()
