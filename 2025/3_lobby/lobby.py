import pandas as pd
import numpy as np


'''
1. Read battery bank names from a file and store them in a list.
2. Find the largest joltage in the bank and store it as the 10s digit.
3. Find the largest joltage that occurs after the first largest joltage and store it as the 1s digit.
4. Do this for all rows in input file.
5. Sum total output joltage.
'''


def read_banks_from_file(input_file):
    banks = []
    with open(input_file, 'r') as file:
        for line in file:
            banks.append(line.strip())
        return banks


def find_largest_joltage_value(bank):
    '''
    Takes a single battery bank and outputs the total joltage for that bank.
    
    :param bank: Single bank of batteries as a string
    '''
    # Need to find joltage value for first digit and get sub-joltage values for second digit
    joltage_values = [int(x) for x in bank.strip()]
    max_joltage = max(joltage_values[:-1]) # First digit cannot be the last joltage in the bank
    max_index = joltage_values.index(max_joltage)

    # Get sub-joltage values after the max joltage index
    sub_joltage_values = joltage_values[max_index + 1:]
    second_max_joltage = max(sub_joltage_values)

    total_joltage = (max_joltage * 10) + second_max_joltage
    return total_joltage


def main():
    input_file = '2025/3_lobby/input.txt'
    banks = read_banks_from_file(input_file)
    total_joltage = 0
    for bank in banks:
        total_joltage += find_largest_joltage_value(bank)
    print(f'The total output joltage is: {total_joltage}')
    # print(find_largest_joltage_value('987654321111111'), 'Expected: 98')


if __name__ == "__main__":
    main()