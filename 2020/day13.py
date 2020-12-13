from util import Day
from aocd import submit
import numpy as np
from itertools import count
from sympy.ntheory.modular import crt

def preprocess(data):
    start_time, ids = data.strip().split("\n")
    return (
        int(start_time),
        np.array([int(x) for x in ids.split(",") if not x == "x"]),
        np.array([i for i, x in enumerate(ids.split(",")) if not x == "x"]),
    )


def schedule(start_time, ids):
    for minutes in range(max(ids)):
        periodicity = (start_time + minutes) % ids == 0
        if any(periodicity):
            return int(ids[periodicity]), minutes



def main(day, part=1):
    start_time, bus_ids, tolerance = preprocess(day.data)
    if part == 1:
        bus_id, minutes = schedule(start_time, bus_ids)
        out = bus_id * minutes
    if part == 2:
        smort = crt(bus_ids, tolerance)
        out = smort[1] - smort[0]
    return out


if __name__ == "__main__":
    day = Day(13)
    day.download()

    day.load(typing=str, process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=13, year=2020)

    day.load(typing=str, process=False)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=13, year=2020)
