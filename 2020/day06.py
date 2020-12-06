from util import Day


def preprocess(data):
    return data.replace("\n\n", "\t").replace("\n", " ").strip().split("\t")


def part1(row):
    return len(set(row.replace(" ", "")))


def part2(row):
    return len(set.intersection(*[set(y) for y in row.split(" ")]))


def main(day, part=1):
    day.data = preprocess(day.data)
    if part == 1:
        day.apply(part1)
        out = sum(day.data)
    if part == 2:
        day.apply(part2)
        out = sum(day.data)
    return out


if __name__ == "__main__":
    day = Day(6)
    day.load(typing=str, process=False)
    print(main(day))
    day.load(typing=str, process=False)
    print(main(day, part=2))
