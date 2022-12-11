from day import Day
from aocd import submit

def parse_elves(day):
    day.parse_list_of_lists(typing = int)
    day.data = [sum(elf) for elf in day.data]
    return day

def main(day, part=1):
    day = parse_elves(day)
    if part == 1:
        return max(day.data)
    if part == 2:
        return sum(sorted(day.data, reverse=True)[:3])

if __name__ == "__main__":
    day = Day(1)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=1, year=2022)

    day.load()
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=1, year=2022)
