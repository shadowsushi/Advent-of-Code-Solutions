"""
Advent of Code 2025 - Day 6: Trash Compactor
URL: https://adventofcode.com/2025/day/6

Goal: 
    Using a list of ranges of fresh ingredient IDs,
    determine available fresh ingredients

Input: 
    Ingredient IDs as a range (int-int)
    Ingredient IDs (int)

Approach:
    1. Get list of fresh ingredient IDs
    2. Check if available IDs is in fresh IDs
    3. Sum available fresh IDs
"""

myList = [0, 1, 2, 3]
myItem = 42

myList.insert(0, myItem)
print(myList)
