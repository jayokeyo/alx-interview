#!/usr/bin/python3
'''
Create a function def island_perimeter(grid): that returns
the perimeter of the island described in grid:

grid is a list of list of integers:
0 represents water
1 represents land
Each cell is square, with a side length of 1
Cells are connected horizontally/vertically (not diagonally).
grid is rectangular, with its width and height not exceeding 100
The grid is completely surrounded by water
There is only one island (or nothing).
The island doesn’t have “lakes” (water inside that isn’t
connected to the water surrounding the island).
'''


def island_perimeter(grid):
    '''returns the perimeter of the island described in grid
    '''
    perimeter = 0
    if (len(grid) < 3 or len(grid[0]) < 3 or grid is None):
        return
    if (sum(grid[0]) != 0 or 
            sum(grid[len(grid) - 1]) != 0):
        return
    for i in range(len(grid)):
        if (grid[i][0] != 0 or grid[i][len(grid[i]) - 1] != 0):
            return
    for i in range(1, (len(grid) - 1)):
        for j in range(1, (len(grid[i]) - 1)):
            if (grid[i][j] == 0 and 
                    (grid[i - 1][j] == grid[i + 1][j] == 
                    grid[i][j - 1] == grid[i][j + 1] == 1)):
                return
            if (grid[i][j] == 1 and grid[i - 1][j] == 0):
                perimeter += 1
            if (grid[i][j] == 1 and grid[i][j - 1] == 0):
                perimeter += 1
            if (grid[i][j] == 1 and grid[i][j + 1] == 0):
                perimeter += 1
            if (grid[i][j] == 1 and grid[i + 1][j] == 0):
                perimeter += 1
    if (perimeter == 0):
        return
    return perimeter
