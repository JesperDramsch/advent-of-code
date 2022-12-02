from util import Day
from aocd import submit

def parse_elves(data):
    elves = []
    calories = 0
    data.append("")
    for line in data:
        if line == "":
            elves.append(calories)
            calories = 0
        else:
            calories += int(line)
    return elves

def main(day, part=1):
    day.data = parse_elves(day.data)
    if part == 1:
        return max(day.data)
    if part == 2:
        return sum(sorted(day.data, reverse=True)[:3])

if __name__ == "__main__":
    day = Day(1)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=1, year=2022)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=1, year=2022)
