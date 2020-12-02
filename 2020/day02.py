from util import Day


def split_input(row):
    req, data = row.split(": ")
    num, char = req.split(" ")
    lower, upper = num.split("-")
    return data, char, int(lower), int(upper)


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
