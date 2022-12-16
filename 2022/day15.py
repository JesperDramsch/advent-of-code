from day import Day
from aocd import submit
import re
import cProfile

def manhattan(a, b):
    return int(abs(a[0]-b[0]) + abs(a[1]-b[1]))


def merge(a, b):
    if a[1] < b[0] or b[1] < a[0]:
        return a, b
    return (min(a[0], b[0]), max(a[1], b[1])), None

def merge_all_per_row(row):
    if len(row) == 1:
        return row
    row.sort()
    out = set()
    a, b, tmp = None, None, None
    for i in range(len(row)-1):
        a, b = (tmp or row[i]), row[i+1]
        a, b = merge(a, b)
        if b is None:
            tmp = a
        else:
            out.add(a)
            tmp = None
    if a:
        out.add(a)
    if b:
        out.add(b)
    return out

def merge_all(blocked):
    out = {}
    for row, ranges in blocked.items():
        out[row] = merge_all_per_row(list(ranges))
    return out

def clock(sensor, distance, blocked, y, part):
    left, right = sensor[1]-distance, sensor[1]+distance+1
    if part == 1 and not (left <= y[0] < right or left < y[1] <= right):
        return blocked
    for i in range(distance+1):
        if sensor[1] + i not in blocked:
            blocked[sensor[1] + i] = set()
        if sensor[1] - i not in blocked:
            blocked[sensor[1] - i] = set()
        blocked[sensor[1] - i].add((sensor[0] - distance + i, sensor[0]  + distance - i + 1))
        blocked[sensor[1] + i].add((sensor[0] - distance + i, sensor[0]  + distance - i + 1))
            
    return blocked

def all_clocks(data, y, part):
    blocked = {}
    for sensor, beacon in data:
        blocked = clock(sensor, manhattan(sensor, beacon), blocked, y, part)
    return blocked

def main(day, part=1, y=(2000000,2000001)):
    regex = re.compile(r"[Sa-z ]+x\=(-?\d+), y\=(-?\d+):[a-z ]+x\=(-?\d+), y\=(-?\d+)")
    day.parse_regex(regex, typing=int)
    day.data = [((a, b), (c, d)) for a, b, c, d in day.data]
    blocked = all_clocks(day.data, y, part)
    blocked = merge_all(blocked)
    if part == 1:
        return int(sum(end-start-1 for start, end in blocked[y[0]]))
    if part == 2:
        for row, ranges in blocked.items():
            if len(ranges) > 1:
                if y[0] <= sorted(ranges)[1][0] < y[1] and y[0] <= row < y[1]:
                    return sorted(ranges, key=lambda x: x[0])[0][1] * 4000000 + row

if __name__ == "__main__":
    day = Day(15)
    day.download()

    day.load()
    # p1 = main(day)
    # print(p1)
    # submit(p1, part="a", day=15, year=2022)


    # day.load(data)
    day.load()
    p2 = main(day, part=2, y=(0, 4_000_001))
    print(p2)
    submit(p2, part="b", day=15, year=2022)
