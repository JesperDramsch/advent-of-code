from util import Day
from aocd import submit
import numpy as np
from scipy.ndimage import label


def parse_input(input_str):
    return np.array([[int(i) for i in line] for line in input_str])


def find_local_minima(data):
    data = np.pad(data, 1, "constant", constant_values=10)

    # Iterate through rows and columns of numpy array data
    local_minima = []
    for i in range(1, len(data) - 1):
        for ii in range(1, len(data[0]) - 1):
            # Check if current value is less than all adjacent values
            if (
                data[i][ii] < data[i - 1][ii]
                and data[i][ii] < data[i + 1][ii]
                and data[i][ii] < data[i][ii - 1]
                and data[i][ii] < data[i][ii + 1]
            ):
                local_minima.append((i - 1, ii - 1))
    return tuple(zip(*local_minima))


def calculate_risk_level(data, locations):
    return sum(data[locations] + 1)


def poor_watershed(data):
    labels, num_regions = label(data != 9)
    basin_sizes = sorted(np.sum(labels == i + 1) for i in range(num_regions))
    return np.prod(basin_sizes[-3:])


def main(day, part=1):
    day.data = parse_input(day.data)
    locations = find_local_minima(day.data)
    if part == 1:
        return calculate_risk_level(day.data, locations)
    if part == 2:
        return poor_watershed(day.data)


if __name__ == "__main__":
    day = Day(9)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=9, year=2021)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=9, year=2021)
