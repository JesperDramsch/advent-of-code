from util import Day
import re

def split_input(row):
    m = re.match(r'(?P<lower>[0-9]*)-(?P<upper>[0-9]*) (?P<char>[a-z]*): (?P<data>[a-z]*)', row)
    return m.group('data'), m.group('char'), int(m.group('lower')), int(m.group('upper'))


def pw_check(row):
    data, char, lower, upper = split_input(row)
    return lower <= data.count(char) <= upper


def pw_check_new(row):
    data, char, lower, upper = split_input(row)
    try:
        a = data[lower - 1] == char
    except IndexError:
        a = False
    try:
        b = data[upper - 1] == char
    except IndexError:
        b = False
    return a != b


def main(day, part=1):
    if part == 1:
        day.apply(pw_check)
        return sum(day.data)
    if part == 2:
        day.apply(pw_check_new)
        return sum(day.data)


if __name__ == "__main__":
    day = Day(2)

    day.load(typing=str)
    print(main(day))

    day.load(typing=str)
    print(main(day, 2))
