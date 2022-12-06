from util import Day
from aocd import submit


def find_marker(data, length):
    for x in range(length - 1, len(data)):
        items = set(data[x - i] for i in range(length))
        if len(items) == length:
            return x + 1


def find_start_marker(data):
    return find_marker(data, 4)


def find_message_marker(data):
    return find_marker(data, 14)


def main(day, part=1):

    if part == 1:
        return find_start_marker(day.data)
    if part == 2:
        return find_message_marker(day.data)


if __name__ == "__main__":
    day = Day(6)
    day.download()

    day.load(process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=6, year=2022)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=6, year=2022)
