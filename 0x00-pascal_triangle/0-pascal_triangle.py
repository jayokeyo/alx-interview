#!/usr/bin/python3
'''
function def pascal_triangle(n): that returns a list of lists of integers
representing the Pascal’s triangle of n:

Returns an empty list if n <= 0
'''

def pascal_triangle(n):
    '''function for creating Pascal triangle'''
    if (n <= 0):
        return []
    k = 0
    List = []
    for i in range(0, n):
        if k == 0:
            List.append([1,])
            k += 1
            continue
        elif k == 0:
            List.append([1, 1])
            k += 1
            continue
        else:
            List.append([1,])
            for j in range(1, k):
                List[i].append(List[i - 1][j]+List[i - 1][j - 1])
            List[i].append(1)
            k += 1
    return List
