from day import Day
from aocd import submit

def main(day, part=1):
    if part == 1:
        pass
    if part == 2:
        pass

if __name__ == "__main__":
    day = Day(1)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    # submit(p1, part="a", day=1, year=2023)

    # day.load()
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=1, year=2023)
