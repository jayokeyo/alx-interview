#!/usr/bin/python3
'''
The N queens puzzle is the challenge of placing N non-attacking queens 
on an N×N chessboard. Write a program that solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number of arguments, print 
Usage: nqueens N, followed by a new line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number, followed by a new line, 
and exit with the status 1
If N is smaller than 4, print N must be at least 4, followed by a new line, 
and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don’t have to print the solutions in a specific order
You are only allowed to import the sys module
'''

import sys


def nqueens(row):
    '''emulates a game of n-queens'''
    for i in range(1, n):
        for j in range (1, i + 1):
            if ((row[i] + 2) == row[i - j]):
                for k in range(1, i + 1):
                    row[i - k] += 1
                    if (row[i - k] >= n ):
                        row[i - k] -= n
            if (row[i] == row[i - j]):
                row[i] += 2
                if (row[i] >= n ):
                    row[i] -= n
            if ((row[i] - j) == row[i - j]
                    or (-(row[i] - j) == row[i - j]
                    and i != n - 1)):
                row[i] += 1
                if (row[i] >= n ):
                    row[i] -= n
    return row

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        exit(1)

    if n < 4:
        print('N must be at least 4')
        exit(1)

    solution1 = []
    solution2 = []
    row = [0] * n
    col = []

    for i in range(n):
        col.append(i)

    row = nqueens(row)

    for i in range(n):
        solution1.append([col[i], row[i]])
    for i in range(n):
        for value in solution1:
            if (value[1] == i):
                solution2.append([i, value[0]])
    print(solution1)
    print(solution2)
