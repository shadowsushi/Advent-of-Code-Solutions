import pandas as pd


invalid_ids_sum = 0
file_path = '2025/2_id_database/input.txt'


def read_id_database(file_path):
    df = pd.read_csv(file_path)
    list_of_start_and_end_points = [] # List to hold start and end of ID ranges
    for column in df.columns:
        list_of_start_and_end_points.append(column.split('-'))
    return list_of_start_and_end_points # Returns list of [start, end] ID ranges


def get_IDs_in_range(start_id, end_id):
    IDs = []
    for i in range(start_id, end_id + 1):
        IDs.append(i)
    return IDs


def get_all_IDs(list_of_start_and_end_points):
    all_IDs = []
    for start_end in list_of_start_and_end_points:
        start_id = int(start_end[0])
        end_id = int(start_end[1])
        ids_in_range = get_IDs_in_range(start_id, end_id)
        all_IDs.extend(ids_in_range)
    return all_IDs


def check_single_duplicate_portion(id_string):
    first_portion = id_string[0:len(id_string)//2]
    second_portion = id_string[len(id_string)//2:]
    if first_portion == second_portion:
        return id_string
    else:
        return


def invalid_ids_sum_part_one():
    list_of_start_and_end_points = read_id_database(file_path)
    all_IDs = get_all_IDs(list_of_start_and_end_points)
    for ID in all_IDs:
        global invalid_ids_sum
        if check_single_duplicate_portion(str(ID)):
            invalid_ids_sum += ID
    return invalid_ids_sum


def invalid_ids_sum_part_two():
    return


def main():
    print(f'The sum of the invalid IDs with single duplicates is: {invalid_ids_sum_part_one()}')
    print(f'The sum of the invalid IDs with multiple duplicates is: {invalid_ids_sum_part_two()}')


if __name__ == '__main__':
    main()