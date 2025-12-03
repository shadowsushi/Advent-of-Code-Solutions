import pandas as pd


invalid_ids_sum_part_one = 0
invalid_ids_sum_part_two = 0
file_path = '2025/2_gift_shop/input.txt'


def read_id_database(file_path):
    '''Reads the ID database from a CSV file and returns a list of start and end ID ranges.'''
    df = pd.read_csv(file_path)
    list_of_start_and_end_points = [] # List to hold start and end of ID ranges
    for column in df.columns:
        list_of_start_and_end_points.append(column.split('-'))
    return list_of_start_and_end_points # Returns list of [start, end] ID ranges


def get_IDs_in_range(start_id, end_id):
    '''Returns a list of IDs in the given range from start_id to end_id (inclusive).'''
    IDs = []
    for i in range(start_id, end_id + 1):
        IDs.append(i)
    return IDs


def get_all_IDs(list_of_start_and_end_points):
    '''Returns a list of all IDs from the given list of start and end ID ranges.'''
    all_IDs = []
    for start_end in list_of_start_and_end_points:
        start_id = int(start_end[0])
        end_id = int(start_end[1])
        ids_in_range = get_IDs_in_range(start_id, end_id)
        all_IDs.extend(ids_in_range)
    return all_IDs


def check_single_duplicate_substring(id_string):
    '''Checks if the given ID string consists of two identical halves.'''
    first_substring = id_string[:len(id_string)//2]
    second_substring = id_string[len(id_string)//2:]
    if first_substring == second_substring:
        return id_string


# This was my initial attempt which was more verbose and less efficient and didn't work.

# def check_multi_duplicate_substring(id_string):
#     '''Checks if the given ID string consists of multiple identical substrings.'''
#     assumed_substring_length = len(id_string)//2
#     for length in range(assumed_substring_length, 1, -1):
#         if len(id_string) % length == 0:
#             substring_1 = id_string[:length]
#             substring_2 = id_string[length:length*2]
#             substring_end = id_string[-length:]
#             # print('substrings are', substring_1, substring_2, substring_end) if debug else None

#             if substring_1 == substring_2 == substring_end:
#                 if id_string.count(substring_1) == len(id_string) // length:
#                     # print(f'Checked with {length} length for {id_string}. Repeating sequences: Yes') if debug else None
#                     return id_string
#                 # else:
#             #         print(f'Checked with {length} length for {id_string}. Repeating sequences: No') if debug else None
#             # else:
#             #     print(f'Checked with {length} length for {id_string}. Repeating sequences: No') if debug else None
#     return None


def check_multi_duplicate_substring(id_string):
    '''Checks if the given ID string consists of multiple identical substrings.'''
    assumed_substring_length = len(id_string)//2
    for length in range(assumed_substring_length, 0, -1):
        if len(id_string) % length == 0: # Check if the length divides the string evenly
            substring = id_string[:length] # Get the substring of the current length
            if substring * (len(id_string) // length) == id_string: # Check if repeating the substring reconstructs the original string
                return id_string
    return None


def calculate_invalid_ids_part_one():
    '''Calculates the sum of invalid IDs with single duplicate substrings.'''
    list_of_start_and_end_points = read_id_database(file_path)
    all_IDs = get_all_IDs(list_of_start_and_end_points)
    for ID in all_IDs:
        global invalid_ids_sum_part_one
        if check_single_duplicate_substring(str(ID)):
            invalid_ids_sum_part_one += ID
    return invalid_ids_sum_part_one


def calculate_invalid_ids_part_two():
    '''Calculates the sum of invalid IDs with multiple duplicate substrings.'''
    list_of_start_and_end_points = read_id_database(file_path)
    all_IDs = get_all_IDs(list_of_start_and_end_points)
    for ID in all_IDs:
        global invalid_ids_sum_part_two
        if check_multi_duplicate_substring(str(ID)):
            invalid_ids_sum_part_two += ID
    return invalid_ids_sum_part_two


def main():
    print(f'The sum of the invalid IDs with single duplicates is: {calculate_invalid_ids_part_one()}')
    print(f'The sum of the invalid IDs with multiple duplicates is: {calculate_invalid_ids_part_two()}')


if __name__ == '__main__':
    main()