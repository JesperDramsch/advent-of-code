from util import Day
from aocd import submit
from scipy.signal import convolve
import numpy as np


def numpyfy(row):
    # L = Empty, # = Occupied, . = Floor
    row = row.replace(".", "0 ").replace("#", "1 ").split()
    return np.array(row).astype(bool)


def count_neighbours(data):
    kernel = np.ones([3] * data.ndim)
    kernel[tuple([1] * data.ndim)] = 0
    sums = convolve(data, kernel, mode="same", method="direct").astype(int)

    keep_act = sums == 2  # No need to keep 3 active, gets activated anyways
    activate = sums == 3

    out = (data * keep_act) + activate

    return out.astype(bool)


def convergence(data, timesteps=6):
    for _ in range(timesteps):
        # print(data[data.shape[0]//2, ...].astype(int))
        data = count_neighbours(data)
    return data


def main(day, part=1):
    time_steps = 6
    day.apply(numpyfy)
    day.data = np.expand_dims(day.data, 0)
    print(day.data)
    if part == 2:
        day.data = np.expand_dims(day.data, 0)  # Fourth Dimension
    day.data = np.pad(day.data, time_steps + 1)
    return np.sum(convergence(day.data, time_steps))


if __name__ == "__main__":
    day = Day(17)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=17, year=2020)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=17, year=2020)
