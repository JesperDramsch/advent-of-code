from util import Day
from aocd import submit


def steer_sub(data, part=1):
    hor, ver, aim = 0, 0, 0
    for instruction in data:
        direction, value = instruction.split(" ")
        if direction == "forward":
            hor += int(value)
            ver += int(aim) * int(value)
        elif direction == "down":
            aim += int(value)
        elif direction == "up":
            aim -= int(value)

    if part == 1:
        aim, ver = ver, aim

    return hor * ver


def main(day, part=1):
    return steer_sub(day.data, part)


if __name__ == "__main__":
    day = Day(2)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=2, year=2021)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=2, year=2021)
