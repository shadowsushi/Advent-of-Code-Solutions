# Initialize variables
initial_knob_position = 50
list_of_rotations = []


def read_rotations_from_file(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            if line[0] == 'R':
                rotation = int(line[1:].strip())
                list_of_rotations.append(rotation)
            if line[0] == 'L':
                rotation = -int(line[1:].strip())
                list_of_rotations.append(rotation)


def calculate_times_at_zero(initial_position, list_of_rotations):
    position = initial_position
    times_at_zero = 0
    for rotation in list_of_rotations:
        position = (position + rotation) % 100
        if position == 0:
            times_at_zero += 1
    return times_at_zero


def calculate_anytime_at_zero(initial_position, list_of_rotations):
    position = initial_position
    times_at_zero = 0
    for rotation in list_of_rotations:
        position += rotation
        if abs(position) // 100 > 0 and position != 0:
            times_at_zero = times_at_zero + (abs(position) // 100)
            position = position % 100
    return times_at_zero


if __name__ == "__main__":
    read_rotations_from_file('2025/1_secret_entrance/input.txt')
    # print(f'The password is: {calculate_times_at_zero(initial_knob_position, list_of_rotations)}')
    print(f'The method 0x434C49434B password is: {calculate_anytime_at_zero(initial_knob_position, list_of_rotations)}')