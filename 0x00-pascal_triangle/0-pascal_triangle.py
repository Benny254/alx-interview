#!/usr/bin/python3
'''The module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''To create a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = []
    if type(n) is not int or n <= 0:
        return triangle
    for w in range(n):
        line = []
        for j in range(w + 1):
            if r == 0 or r == w:
                line.append(1)
            elif w > 0 and r > 0:
                line.append(triangle[w - 1][r - 1] + triangle[w - 1][r])
        triangle.append(line)
    return triangle
