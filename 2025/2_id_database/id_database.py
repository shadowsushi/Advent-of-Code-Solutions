import pandas as pd


invalid_ids_sum = 0
file_path = 'input.txt'


def read_id_database(file_path):
    df = pd.read_csv(file_path)
    list_of_start_and_end_points = [] # List to hold start and end of ID ranges
    for column in df.columns:
        list_of_start_and_end_points.append(column.split('-'))
    return list_of_start_and_end_points # Returns list of [start, end] ID ranges


def get_ids_in_range(start_id, end_id):
    IDs = []
    for i in range(start_id, end_id + 1):
        IDs.append(i)
    return IDs


def the_function_that_takes_the_list_of_start_and_end_points(list_of_start_and_end_points):
    all_IDs = []
    for start_end in list_of_start_and_end_points:
        start_id = int(start_end[0])
        end_id = int(start_end[1])
        ids_in_range = get_ids_in_range(start_id, end_id)
        all_IDs.extend(ids_in_range)
    return all_IDs


def check_duplicate_portion(id_string):
    first_portion = id_string[0:len(id_string)//2]
    second_portion = id_string[len(id_string)//2:]
    if first_portion == second_portion:
        return id_string
    else:
        return


def main():
    list_of_start_and_end_points = read_id_database(file_path)
    all_IDs = the_function_that_takes_the_list_of_start_and_end_points(list_of_start_and_end_points)
    for ID in all_IDs:
        global invalid_ids_sum
        if check_duplicate_portion(str(ID)):
            invalid_ids_sum += ID
    print(invalid_ids_sum)


if __name__ == '__main__':
    main()