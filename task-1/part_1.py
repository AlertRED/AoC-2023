def get_first_digit(line: str, is_reversed: bool = False):
    for idx in range(len(line) - 1, -1, -1) if is_reversed else range(len(line)):
        if line[idx].isdigit():
            return line[idx]


def main():
    numbers = []
    with open('task-1/assets/input', 'r') as file:
        while line := file.readline().rstrip():
            numbers.append(
                int(
                    get_first_digit(line)
                    + get_first_digit(line, is_reversed=True)
                ),
            )
    return sum(numbers)


if __name__ == '__main__':
    print(main())
