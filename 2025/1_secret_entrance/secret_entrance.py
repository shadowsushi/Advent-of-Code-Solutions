# Initialize variables
initial_knob_position = 50
list_of_rotations = []
input_file = '2025/1_secret_entrance/input.txt'


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
    current_position = initial_position
    times_at_zero = 0
    for rotation in list_of_rotations:
        new_position = current_position + rotation
        # print('---')
        # print(f'{current_position} moving {rotation} to {new_position}')
        if current_position == 0:
            times_at_zero += abs(new_position) // 100
        else:
            if new_position <= 0:
                times_at_zero += (abs(new_position) // 100) + 1
            elif new_position // 100 > 0:
                times_at_zero += abs(new_position) // 100
        current_position = new_position % 100 # Convert new position to real dial position
        # print(f'new dial position: {current_position}')
        # print(f'current times at zero: {times_at_zero}')
    return times_at_zero


def main():
    read_rotations_from_file(input_file)
    print(f'The password is: {calculate_times_at_zero(initial_knob_position, list_of_rotations)}')
    print(f'The method 0x434C49434B password is: {calculate_anytime_at_zero(initial_knob_position, list_of_rotations)}')


if __name__ == "__main__":
    main()