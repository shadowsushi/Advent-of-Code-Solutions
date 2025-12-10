'''
1.  Read shelves and store as list
2.  For a given shelf, get shelf above and shelf below
3.  For a given position, get number of rolls of paper
    at each of the 8 adjacent positions (up, down, left, right, and diagonals)
4.  If number of papers is less than or equal to 3, add it to the roll count
'''

example = [
    '..@@.@@@@.',
    '@@@.@.@.@@',
    '@@@@@.@.@@',
    '@.@@@@..@.',
    '@@.@@@@.@@',
    '.@@@@@@@.@',
    '.@.@.@.@@@',
    '@.@@@.@@@@',
    '.@@@@@@@@.',
    '@.@.@@@.@.',
] # Answer is 13


def read_shelves_from_file(input_file):
    shelves = []
    with open(input_file, 'r') as file:
        for line in file:
            shelves.append(line.strip())
        return shelves


def get_shelf_comparisons(shelves: list):
    '''
    Docstring for count_accessible_rolls
    
    :param shelves: Shelves as an array of strings
    :param paper_limit: Maximum number of adjacent rolls such that the roll is still accessible by forklift
    '''
    # Create a list for all the comparisons between previous shelf and next shelf
    list_of_shelf_comparisons = []

    for i in range(len(shelves)):
        # Get previous, current, and next shelf
        previous_shelf = shelves[i - 1] if i > 0 else None
        current_shelf = shelves[i]
        next_shelf = shelves[i + 1] if i < len(shelves) - 1 else None

        # Append shelves to current comparison
        current_shelf_comparison = []
        current_shelf_comparison.append(previous_shelf)
        current_shelf_comparison.append(current_shelf)
        current_shelf_comparison.append(next_shelf)

        # Append current comparison to list of comparisons
        list_of_shelf_comparisons.append(current_shelf_comparison)
    
    return list_of_shelf_comparisons


def get_slot_comparisons(shelf_comparison: list):
    list_of_slot_comparisons = []

    if len(shelf_comparison) != 3:
        raise ValueError(f'Expected 3 shelves, got {len(shelf_comparison)}')
    
    for i in range(len(shelf_comparison[1])): # Iterate over the length of the current shelf
        if shelf_comparison[1][i] == '@':
            previous_shelf = shelf_comparison[0]
            current_shelf = shelf_comparison[1]
            next_shelf = shelf_comparison[2]

            # Use helper function to get adjacent slots
            slot_comparison = []
            top_three_slots = get_adjacent_slots(previous_shelf, i) if previous_shelf else []
            middle_three_slots = get_adjacent_slots(current_shelf, i)
            bottom_three_slots = get_adjacent_slots(next_shelf, i) if next_shelf else []

            # Combine all adjacent slots into a single list
            slot_comparison.extend(top_three_slots)
            slot_comparison.extend(middle_three_slots)
            slot_comparison.extend(bottom_three_slots)

            # Append the slot comparison to the list
            list_of_slot_comparisons.append(slot_comparison)

    return list_of_slot_comparisons


def get_adjacent_slots(shelf: list, index: int):
    adjacent_slots = []

    # Get the three adjacent slots (left, center, right) for the given index on the shelf
    for i in range(index - 1, index + 2):
        if i < 0 or i >= len(shelf):
            continue
        adjacent_slots.append(shelf[i])
    
    return adjacent_slots


def main():
    # print(get_shelf_comparisons(example))
    count_accessible_rolls = 0
    input_file = '2025/4_printing_department/input.txt'
    shelves = read_shelves_from_file(input_file)

    list_of_shelf_comparisons = get_shelf_comparisons(shelves)

    for shelf_comparison in list_of_shelf_comparisons:
        list_of_slot_comparisons = get_slot_comparisons(shelf_comparison)
        for slot_comparison in list_of_slot_comparisons:
            roll_count = slot_comparison.count('@')
            if roll_count <= 4:
                count_accessible_rolls += 1

    print(count_accessible_rolls)

if __name__ == '__main__':
    main()