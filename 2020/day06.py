from util import Day
from aocd import submit

def preprocess(data):
    return data.replace("\n\n", "\t").replace("\n", " ").strip().split("\t")


def part1(row):
    return len(set(row.replace(" ", "")))


def part2(row):
    return len(set.intersection(*map(set, row.split(" "))))


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
    day.download()
    day.load(typing=str, process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=6, year=2020)
    day.load(typing=str, process=False)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=6, year=2020)
    
