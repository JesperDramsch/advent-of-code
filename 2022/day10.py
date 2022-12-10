from util import Day
from aocd import submit

def run_program(instructions, checks):
    cycles, X = 0, 1
    check = 20
    for line in instructions:
        add = 0
        match line.split(" "):
            case "noop",:
                inc = 1
            case "addx", add:
                inc = 2
                add = int(add)
        if cycles < check <= cycles+inc:
            checks[check] = X
            check += 40
        X += add
        cycles += inc
    return checks


def main(day, part=1):
    if part == 1:
        checks = {20+n*40:None for n in range(6)}
        checks = run_program(day.data, checks)
        return sum(cycle*X for cycle, X in checks.items())
    if part == 2:
        pass

if __name__ == "__main__":
    day = Day(10)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=10, year=2022)

    # day.load(typing=str)
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=10, year=2022)
