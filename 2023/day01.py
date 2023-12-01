from day import Day
from aocd import submit

map_digits = dict(one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9)


def filter(line, part=1):
    if part == 2:
        for key in map_digits.keys():
            line = line.replace(key, f"{key}{map_digits[key]}{key}")
    return [a for a in line if a.isdigit()]


def main(day, part=1):
    data = []
    filtered = []
    for line in day.data:
        filtered.append(filter(line, part=part))
    for line in filtered:
        data.append(int(line[0]) * 10 + int(line[-1]))
    return sum(data)


if __name__ == "__main__":
    day = Day(1)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=1, year=2023)

    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=1, year=2023)
