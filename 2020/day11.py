from util import Day
from aocd import submit
from scipy.signal import convolve2d
import numpy as np
from itertools import product


def numpyfy(row):
    # L = Empty, # = Occupied, . = Floor
    row = row.replace("L", "0 ").replace("#", "1 ").replace(".", "-1 ").split()
    return np.array(row).astype(int)


def masks(arr):
    floor_mask = arr != -1
    seats = np.zeros_like(floor_mask)
    return seats, floor_mask


def fill_empty(seats, floor):
    empty_seats = ~seats + ~floor
    new_seats = convolve2d(empty_seats, np.ones((3, 3)), mode="same", fillvalue=1) == 9
    new_empty = convolve2d(empty_seats, np.ones((3, 3)), mode="same", fillvalue=1) >= 5
    return floor * (seats + new_seats) * new_empty


def convergence(seats, floor):
    old_seats = np.ones_like(seats)
    while not np.array_equal(old_seats, seats):
        old_seats = seats.copy()
        seats = fill_empty(seats, floor)
    return seats


def convergence_2(seats, graph):
    old_seats = np.ones_like(seats)
    while not np.array_equal(old_seats, seats):
        old_seats = seats.copy()
        seats = traverse_graph(seats, graph)
    return seats


def build_graph(in_arr):
    graph = {}
    rows, cols = in_arr.shape
    # Pad the outside one layer with zeros to build the graph
    arr = np.pad(in_arr, 1, constant_values=0)
    # ok let's play
    # Go through each row and column of the array
    for c in range(1, cols + 1):
        for r in range(1, rows + 1):
            # Skip if it's an empty space
            if arr[r, c] == -1:
                continue
            # In each direction search for the first chair
            local_list = []
            for i, j in product([1, 0, -1], repeat=2):
                # Skip (0, 0)
                if i == j == 0:
                    continue
                # Start with the assumption of no chair
                thingy = -1
                k = 0
                while thingy == -1:
                    # Go into the direction of i,j in steps of +1 until it's a chair
                    k += 1
                    r_, c_ = r + i * k - 1, c + j * k - 1
                    thingy = arr[r_ + 1, c_ + 1]
                # Ignore the padding
                if (0 <= r_ < rows) and (0 <= c_ < cols):
                    local_list.append((r_, c_))
            # Build graph
            graph[(r - 1, c - 1)] = local_list
    return graph


def traverse_graph(arr, graph):
    new = arr.copy()
    rows, cols = arr.shape
    for c in range(cols):
        for r in range(rows):
            if new[r, c] == -1:
                continue
            full_seats = 0
            for coord in graph[(r, c)]:
                full_seats += arr[coord]
            if full_seats == 0:
                new[r, c] = 1
            if full_seats >= 5:
                new[r, c] = 0
    # printable(new)
    return new


def printable(arr):
    print("Next Iteration")
    arr = arr.astype(str)
    arr[arr == "-1"] = "."
    arr[arr == "0"] = "L"
    arr[arr == "1"] = "#"
    print(arr)


def main(day, part=1):
    day.apply(numpyfy)
    day.data = np.array(day.data)
    seats, floor_mask = masks(day.data)
    if part == 1:
        out = np.sum(convergence(seats, floor_mask))
    if part == 2:
        print("Building Graph")
        graph = build_graph(day.data)
        print("Everyday I'm Shuffling")
        seats = convergence_2(day.data, graph)
        out = np.sum(seats == 1)
    return out


if __name__ == "__main__":
    day = Day(11)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=11, year=2020)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=11, year=2020)
