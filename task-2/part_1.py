from pprint import pprint

AVAILABLE_COUBS = {'red': 12, 'green': 13, 'blue': 14}


def parse_text_to_dict(text: str):
    result = {}
    group_number = 0
    for line in text:
        line = line[line.index(':') + 2:]
        group_number += 1
        for group in line.split(';'):
            for items in group.split(','):
                item = (items.strip().split(' '))
                result.setdefault(group_number, []).append((int(item[0]), item[1]))
    return result


def main():
    result = 0
    with open('task-2/assets/example-part-1.txt', 'r') as file:
        games = parse_text_to_dict(file.readlines())
        for game_num, tries in games.items():
            for count, color_name in tries:
                if count > AVAILABLE_COUBS[color_name]:
                    break
            else:
                result += game_num
    return result


if __name__ == '__main__':
    print(main())
