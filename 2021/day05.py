from util import Day
from aocd import submit
from collections import Counter


def parse_input(input_str):
    coords = []
    for line in input_str:
        # Split start and end
        start, end = line.split(" -> ")
        # Append complex coords to list
        coords.append((complex(start.replace(",", "+") + "j"), complex(end.replace(",", "+") + "j")))
    return coords


def fill_lines(coords, diagonal=False):
    vents = Counter()
    # Iterate over all coords
    for coord in coords:
        # Get offset from coord 0 to coord 1
        offset = coord[1] - coord[0]

        # Straight lines
        if (offset.real == 0) or (offset.imag == 0):
            # Calculate straight increment and number of steps
            increment = offset / abs(offset)
            steps = int(abs(offset)) + 1
        # Diagonal lines when diagonal is True
        elif diagonal:
            # Calculate diagonal increment and number of steps
            increment = complex(offset.real / abs(offset.real), offset.imag / abs(offset.imag))
            steps = int(abs(coord[1].real - coord[0].real)) + 1
        # Otherwise, skip
        else:
            continue

        # Iterate over steps and add to counter using increment
        for i in range(steps):
            vents[coord[0] + i * increment] += 1

    return vents


def get_intersections(lines):
    return {key: value for key, value in lines.items() if value > 1}


def main(day, part=1):
    coords = parse_input(day.data)
    lines = fill_lines(coords, diagonal=bool(part == 2))
    intersections = get_intersections(lines)
    return len(intersections)


if __name__ == "__main__":
    day = Day(5)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=5, year=2021)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=5, year=2021)
