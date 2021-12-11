from util import Day
from aocd import submit
import numpy as np


def parse_input(data):
    return np.array([[int(x) for x in line] for line in data], dtype=np.uint8)


def border_filter(loc1, loc2):
    # build all neighbours
    loc1 = np.array([loc1 - 1, loc1, loc1 + 1] * 3, dtype=np.uint8)
    loc2 = np.array([loc2 - 1] * 3 + [loc2] * 3 + [loc2 + 1] * 3, dtype=np.uint8)
    # filter out neighbours that are not in the image
    loc1, loc2 = (
        loc1[(loc1 >= 0) & (loc1 <= 9) & (loc2 >= 0) & (loc2 <= 9)],
        loc2[(loc1 >= 0) & (loc1 <= 9) & (loc2 >= 0) & (loc2 <= 9)],
    )
    return loc1, loc2


def transfer_energy(data):
    visited = set()
    # 1. Increment data
    data += 1

    # 2. Flash and increment neighbours
    while True:
        # Find all octopuses that flashed this step
        flashing = set(zip(*np.where(data > 9)))

        # If there are no new octopuses that flashed, we're done
        if flashing == visited:
            break

        # Find all neighbours of all octopuses that flashed this step and increment their energy
        for x, y in flashing - visited:
            loc1, loc2 = border_filter(x, y)
            data[loc1, loc2] += 1

        # Mark all octopuses that flashed this step as visited
        visited.update(flashing)

    # 3. Set all octopuses that flashed to 0
    data[data > 9] = 0

    return data, len(visited)


def flashing_octopus(data, steps):
    num_flashes = 0
    for _ in range(steps):
        data, flashes = transfer_energy(data)
        num_flashes += flashes
    return num_flashes


def simultaneous_flashing(data):
    steps = 0
    while True:
        data, flashes = transfer_energy(data)

        steps += 1
        if np.sum(data) == 0:
            break
    return steps


def main(day, part=1):
    day.data = parse_input(day.data)
    if part == 1:
        return flashing_octopus(day.data, 100)
    if part == 2:
        return simultaneous_flashing(day.data)


if __name__ == "__main__":
    day = Day(11)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=11, year=2021)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=11, year=2021)
