from math import floor


def main():
    with open('input.txt') as f:
        text = f.read()

    # Split into numbers
    numbers = [int(x) for x in text.split(',')]

    numbers[1] = 12
    numbers[2] = 2
    end_result = handle_numbers(numbers)
    print(end_result[0])


def handle_numbers(numbers):
    pointer = 0

    while True:
        # What operation to do
        operation_id = numbers[pointer]

        if operation_id == 99:
            return numbers

        x_index = numbers[pointer + 1]
        y_index = numbers[pointer + 2]
        if operation_id == 1:
            result = numbers[x_index] + numbers[y_index]
        elif operation_id == 2:
            result = numbers[x_index] * numbers[y_index]

        # Store result at specified index
        store_index = numbers[pointer + 3]
        numbers[store_index] = result

        pointer += 4

def handle_mass(x):
    return floor(x / 3) - 2


if __name__ == '__main__':
    main()
