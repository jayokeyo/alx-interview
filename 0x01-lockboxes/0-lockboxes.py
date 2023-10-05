#!/usr/bin/python3
'''
You have n number of locked boxes in front of you. 
Each box is numbered sequentially from 0 to n - 1 
and each box may contain keys to the other boxes.

Write a method that determines if all the boxes can be opened.

Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False
'''

def canUnlockAll(boxes):
    '''method that determines if all the boxes can be opened.'''
    if (len(boxes) > 0):
        Opened_boxes = ["Locked"] * len(boxes)
        Opened_boxes[0] = "Unlocked"
        for i in range(0, len(boxes)):
            if (len(boxes[i]) > 0):
                for j in range(0, len(boxes[i])):
                    Opened_boxes[boxes[i][j]] = "Unlocked" if boxes[i][j] < len(boxes)
            else:
                break
        if "Locked" in Opened_boxes:
            return False
        else:
            return True
