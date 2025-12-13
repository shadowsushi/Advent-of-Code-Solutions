"""
Advent of Code 2025 - Day 5: Cafeteria
URL: https://adventofcode.com/2025/day/5

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
example = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32
'''
debug = False


from datetime import datetime


def read_input(input_file):
    if debug:
        parts = example.strip().split('\n\n')

        part1 = parts[0].splitlines()
        part2 = parts[1].splitlines()

        return part1, part2
    
    with open(input_file, 'r') as file:
        content = file.read()
        parts = content.split('\n\n') # Splits the file at line break

        part1 = parts[0].splitlines()
        part2 = parts[1].splitlines()

        print('Input retrieved')
        return part1, part2


# Oh you like IDs? Get every ID.
# def get_IDs_from_ranges(id_ranges: list):
#     IDs = []
#     print('Retrieving IDs', datetime.now())
#     for id_range in id_ranges:
#         start_id, end_id = id_range.split('-')
#         for id in range(int(start_id), int(end_id) + 1):
#             if id not in IDs:
#                 IDs.append(id)
#     print('IDs retrieved', datetime.now())
#     return IDs


def get_id_start_ends(id_ranges: list):
    id_start_ends = []
    # print('Retrieving IDs', datetime.now())
    for id_range in id_ranges:
        id_start_ends.append(id_range.split('-'))
    # print('IDs retrieved', datetime.now())
    return id_start_ends


def check_id_in_id_ranges(id: str, id_start_ends: list):
    for id_start_end in id_start_ends:
        if int(id_start_end[0]) <= int(id) <= int(id_start_end[1]):
            return True
    return False


# def get_id_count(id_start_ends: list):
#     count = 0
#     for id_start_end in id_start_ends:
#         # print(id_start_end)
#         count += (int(id_start_end[1]) - int(id_start_end[0]))
#     return count


def main():
    available_count = 0
    fresh_count = 0

    fresh_ID_ranges, available_IDs = read_input('2025/5_cafeteria/5_input.txt')
    # fresh_ID_ranges, available_IDs = read_input(example)

    fresh_ID_start_ends = get_id_start_ends(fresh_ID_ranges)

    for id in available_IDs:
        if check_id_in_id_ranges(id, fresh_ID_start_ends):
            available_count += 1

    # fresh_count = get_id_count(fresh_ID_start_ends)

    print(f'Number of available fresh ingredients: {available_count}')
    # print(f'Total number of fresh ingredients: {fresh_count}')




if __name__ == '__main__':
    main()