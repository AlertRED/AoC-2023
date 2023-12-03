WORDS = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}


def get_first_digit(line: str, is_reversed: bool = False):
    rnge = range(len(line) - 1, -1, -1) if is_reversed else range(len(line))
    for idx in rnge:
        if line[idx].isdigit():
            return line[idx]
        for word, number in WORDS.items():
            if line[idx:idx + len(word)] == word:
                return number


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
