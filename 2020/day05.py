from util import Day


def row(string):
    return int(string[:7].replace("F", "0").replace("B", "1"), 2)


def seat(string):
    return int(string[7:].replace("L", "0").replace("R", "1"), 2)


def seat_id(string):
    return row(string) * 8 + seat(string)


def main(day, part=1):
    if part == 1:
        day.apply(seat_id)
        out = max(day.data)
    if part == 2:
        day.apply(seat_id)
        day.data = sorted(day.data)
        for x, y in zip(day.data[:-1], day.data[1:]):
            if y-x == 2:
                out = x+1
    return out


if __name__ == "__main__":
    day = Day(5)
    day.load(typing=str)
    print(main(day))
    day.load(typing=str)
    print(main(day, part=2))
