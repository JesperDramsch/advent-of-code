from util import Day
from aocd import submit
import numpy as np
import re
def parse_input(data):
    out = []
    for line in data:
        r = re.match(r'(on|off) x=(-*\d+)..(-*\d+),y=(-*\d+)..(-*\d+),z=(-*\d+)..(-*\d+)', line)
        on_off, x1, x2, y1, y2, z1, z2 = r.groups()
        out.append((on_off=="on", (int(x1), int(x2)), (int(y1), int(y2)), (int(z1), int(z2))))
    return out

def populate_grid(data):
    cubes = np.zeros((100, 100, 100), dtype=bool)
    for on_off, x, y, z in data:
        cubes[x[0]+50:x[1]+50+1, y[0]+50:y[1]+50+1, z[0]+50:z[1]+50+1] = on_off
    return cubes


def main(day, part=1):
    day.data = parse_input(day.data)
    if part == 1:
        return populate_grid(day.data).sum()
    if part == 2:
        pass

if __name__ == "__main__":
    day = Day(22)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=22, year=2021)

    # day.load(typing=str)
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=22, year=2021)
