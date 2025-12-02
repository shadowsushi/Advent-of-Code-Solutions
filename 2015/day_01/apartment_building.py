def get_floor(input_file):
    with open(input_file, 'r') as file:
        floor = 0
        for char in file.read().strip():
            if char == '(':
                floor += 1
            elif char == ')':
                floor -= 1
        return floor





if __name__ == "__main__":
    input_file = '2015/day_01/input.txt'
    result = get_floor(input_file)
    print(f"The final floor is: {result}")