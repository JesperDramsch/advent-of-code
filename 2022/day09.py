from day import Day
from aocd import submit


def parse(data):
    directions = {"R": 1 + 0j, "L": -1 + 0, "U": 0 + 1j, "D": 0 - 1j}
    return directions[data[0]], data[1]


def movement(rope, direction, steps, visited=set()):
    for _ in range(steps):
        rope[0] += direction
        for i in range(len(rope) - 1):
            head, tail = rope[i], rope[i + 1]
            diff = tail - head
            if abs(diff) >= 2:
                if diff.real != 0:
                    tail = tail.real - (diff.real / abs(diff.real)) + tail.imag * 1j
                if diff.imag != 0:
                    tail = tail.real + (tail.imag - (diff.imag / abs(diff.imag))) * 1j
            rope[i + 1] = tail
        visited.add(rope[-1])
    return rope


def wiggle(data, rope_length):
    rope = [0j] * rope_length
    visited = set([0])
    for direction, steps in data:
        rope = movement(rope, direction, steps, visited)
        visited.add(rope[-1])
    return visited


def main(day, part=1):
    day.parse_list_of_lists(sep2=" ", sep="\n", typing=(str, int))
    day.apply(parse)
    if part == 1:
        return len(wiggle(day.data, rope_length=2))
    if part == 2:
        return len(wiggle(day.data, rope_length=10))


if __name__ == "__main__":
    day = Day(9)
    day.download()

    data = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

    # day.load(data)
    day.load()

    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=9, year=2022)

    data = """R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

    # day.load(data)
    day.load()

    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=9, year=2022)
