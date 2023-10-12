#!/usr/bin/env python3
'''
In a text file, there is a single character H. 
Your text editor can execute only two operations in this file: Copy All and Paste. 
Given a number n, write a method that calculates the fewest number of operations 
needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
Example:

n = 9

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

Number of operations: 6
'''


def minOperations(n):
    '''
    calculates the fewest number of operations needed to result in exactly 
    n H characters in the file.
    '''
    count = 0
    copied = 0
    characters = 1

    while (characters < n):
        if (n % characters == 0):
            copied = characters
            characters *= 2
            count += 2
        else:
            characters += copied
            count += 1
    return count
