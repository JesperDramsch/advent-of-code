from day import Day
from aocd import submit
import re
from collections import Counter

regex = re.compile(r"(\w+)([=-])(\d?)")


def reindeer_hash(data, val=0):
    if len(data) == 0:
        return val
    val += ord(data[0])
    val *= 17
    val %= 256
    return reindeer_hash(data[1:], val)


def focal(data):
    boxes = {}
    for d in data:
        matched = regex.match(d)
        label, operator, value = matched.groups()
        if value.isdigit():
            value = int(value)

        if operator == "=":
            boxes[label] = value
        elif operator == "-":
            if label in boxes:
                del boxes[label]

    out = []

    box_slots = Counter()
    for k, v in boxes.items():
        box = reindeer_hash(k) + 1
        box_slots[box] += 1
        out.append(box * box_slots[box] * v)

    return out


def main(day, part=1):
    data = day.data.split(",")
    if part == 1:
        return sum(reindeer_hash(d) for d in data)
    if part == 2:
        return sum(focal(data))


if __name__ == "__main__":
    day = Day(15)
    day.download()

    day.load(process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=15, year=2023)

    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=15, year=2023)
