from util import Day
from aocd import submit

def parse(data):
    directions = {"R": 1+0j, "L": -1 + 0, "U": 0 + 1j, "D": 0-1j}
    for line in data:
        direction, steps = line.split()
        yield directions[direction], int(steps)

def movement(head, tail, direction, steps, visited=set()):
    for _ in range(steps):
        head += direction
        diff = tail-head
        if abs(diff) >= 2:
            if diff.imag == 0:
                tail = tail.real - (diff.real / abs(diff.real)) + tail.imag * 1j
            elif diff.real == 0:
                tail = tail.real + (tail.imag - (diff.imag / abs(diff.imag))) * 1j
            else:
                tail = tail.real - (diff.real / abs(diff.real)) + (tail.imag - (diff.imag / abs(diff.imag))) * 1j
            visited.add(tail)
    return head, tail
    
def wiggle(data):
    head, tail = 0j, 0j
    visited = set([0])
    for direction, steps in data:
        head, tail = movement(head, tail, direction, steps, visited)
        visited.add(tail)
    return visited


def main(day, part=1):
    day.data = parse(day.data)
    if part == 1:
        return len(wiggle(day.data))
    if part == 2:
        pass

if __name__ == "__main__":
    day = Day(9)
    day.download()

#     data = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2"""

#     day.load(data, typing=str)

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=9, year=2022)

    # day.load(typing=str)
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=9, year=2022)
