from util import Day
from aocd import submit
import numpy as np
import re
from collections import Counter


def parse_input(data):
    out = []
    for line in data:
        r = re.match(r"(on|off) x=(-*\d+)..(-*\d+),y=(-*\d+)..(-*\d+),z=(-*\d+)..(-*\d+)", line)
        on_off = r.groups()[0] == "on"
        x1, x2, y1, y2, z1, z2 = map(int, r.groups()[1:])
        out.append((on_off, (x1, x2), (y1, y2), (z1, z2)))
    return out


def populate_grid(data):
    cubes = np.zeros((100, 100, 100), dtype=bool)
    for on_off, x, y, z in data:
        cubes[x[0] + 50 : x[1] + 50 + 1, y[0] + 50 : y[1] + 50 + 1, z[0] + 50 : z[1] + 50 + 1] = on_off
    return cubes


def process_all_cubes(instructions):
    cubes = Counter()
    for on_off, x_next, y_next, z_next in instructions:
        for (x, y, z), val in cubes.copy().items():
            ix = max(x[0], x_next[0]), min(x[1], x_next[1])
            iy = max(y[0], y_next[0]), min(y[1], y_next[1])
            iz = max(z[0], z_next[0]), min(z[1], z_next[1])

            # Remove empty cubes
            if val == 0:
                cubes.pop((x, y, z))
                continue
            # New cube is contained in existing positive cube
            elif (
                on_off
                and val > 0
                and x_next[0] >= x[0]
                and x_next[1] <= x[1]
                and y_next[0] >= y[0]
                and y_next[1] <= y[1]
                and z_next[0] >= z[0]
                and z_next[1] <= z[1]
            ):
                break
            # Existing cube item is contained in new cube
            elif (
                on_off
                and x[0] >= x_next[0]
                and x[1] <= x_next[1]
                and y[0] >= y_next[0]
                and y[1] <= y_next[1]
                and z[0] >= z_next[0]
                and z[1] <= z_next[1]
            ):
                cubes.pop((x, y, z))

            # Reset overlapping value 
            elif ix[0] <= ix[1] and iy[0] <= iy[1] and iz[0] <= iz[1]:
                cubes[ix, iy, iz] -= val
        else:
            # Add new cube
            if on_off:
                cubes[x_next, y_next, z_next] += 1

    return cubes


def count_lights(cubes):
    return sum((x[1] - x[0] + 1) * (y[1] - y[0] + 1) * (z[1] - z[0] + 1) * val for (x, y, z), val in cubes.items())


def main(day, part=1):
    day.data = parse_input(day.data)
    if part == 1:
        return populate_grid(day.data).sum()
    if part == 2:
        cubes = process_all_cubes(day.data)
        return count_lights(cubes)


if __name__ == "__main__":
    day = Day(22)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=22, year=2021)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=22, year=2021)
