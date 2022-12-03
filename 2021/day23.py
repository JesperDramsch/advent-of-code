from util import Day
from aocd import submit



def main(day, part=1):
    if part == 1:
        pass
    if part == 2:
        pass

if __name__ == "__main__":
    day = Day(23)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    # submit(p1, part="a", day=23, year=2021)

    # day.load(typing=str)
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=23, year=2021)
