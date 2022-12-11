from day import Day
from aocd import submit
from itertools import chain

def parse_input(data):
    return [((x for x in line[:len(line)//2]), (x for x in line[len(line)//2:])) for line in data]

def match_compartments(comp1, comp2):
    return set(comp1) & set(comp2)

def prioritize(item):
    offset = 96 if item == item.lower() else 38
    return ord(item) - offset

def group_badges(data):
    badges = []
    for i, item in enumerate(data + [""]):
        if i % 3 == 0:
            if i != 0:
                badges.append("".join(set.intersection(*rucksacks)))
            rucksacks = [set(), set(), set()]
        rucksacks[i%3] = set(x for x in item)
    return badges

def main(day, part=1):
    day.parse_list()
    if part == 1:
        day.data = parse_input(day.data)
        items = [match_compartments(*rucksack) for rucksack in day.data]
        return sum(sum(map(prioritize, item)) for item in items)
    if part == 2:
        return sum(prioritize(item) for item in group_badges(day.data))

if __name__ == "__main__":
    day = Day(3)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=3, year=2022)

    day.load()
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=3, year=2022)
