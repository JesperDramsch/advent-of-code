from util import Day
from aocd import submit
import numpy as np
import re
from itertools import combinations



def parse_scan_log(log):
    out = {}
    for line in log:
        if "" == line:
            continue
        elif line.startswith("---"):
            name = int(re.search("--- scanner (\d*) ---", line).groups()[0])
            out[name] = set()
        else:
            out[name].add(tuple(map(int, line.split(","))))
    return out


def rotate_coordinates(a, b, c):
    out = (
        (a, b, c),
        (a, c, -b),
        (a, -b, -c),
        (a, -c, b),
        (b, -a, c),
        (b, c, a),
        (b, a, -c),
        (b, -c, -a),
        (-a, -b, c),
        (-a, -c, -b),
        (-a, b, -c),
        (-a, c, b),
        (-b, a, c),
        (-b, -c, a),
        (-b, -a, -c),
        (-b, c, -a),
        (c, b, -a),
        (c, a, b),
        (c, -b, a),
        (c, -a, -b),
        (-c, -b, -a),
        (-c, -a, b),
        (-c, b, a),
        (-c, a, -b),
    )
    return out


def shift_intertial_coords(beacons):
    # Shift each coordinate to inertial system for beacon
    centered_beacons = []
    for new_intertial in beacons:
        shifted_beacons = set()
        for beacon in beacons:
            if beacon != new_intertial:
                shifted_beacons.add(tuple(np.subtract(beacon, new_intertial)))
        centered_beacons.append(shifted_beacons)
    return centered_beacons


def propagate_coords(coords):
    # Generate all rotations
    rotations = [[] for _ in range(24)]
    for coord in coords:
        for i, rotated in enumerate(rotate_coordinates(*coord)):
            rotations[i].append(rotated)
    return np.array(rotations)


def match_beacons(beacon_a, beacon_b):
    # Match two beacons based on rotated coordinates of beacon_b
    # Beacon a is a set of coordinates
    for coord_b in propagate_coords(beacon_b): # already propagated
        if len(set.intersection(beacon_a,coord_b)) > 3: # Maybe 3?
            return True
    return False


def identify_beacons(scanners):
    beacons = dict(((0, i), [(0, i)]) for i in range(len(scanners[0][0])))
    for name, rotations in scanners.items():
        if name == 0:
            continue
        for i in range(len(rotations[1])):
            rotations
            break
    return beacons


def main(day, part=1):
    day.data = parse_scan_log(day.data)
    scanners_with_beacons = {name: propagate_coords(coords) for name, coords in day.data.items()} 
    #shifted_beacons = {name: propagate_coords(coords) for name, coords in scanners_with_beacons} 
    # return set(map(tuple, scanners_with_beacons[0][0].tolist()))
    if part == 1:
        beacons = identify_beacons(scanners_with_beacons)
        print(beacons)
        return len(beacons)
    if part == 2:
        pass


if __name__ == "__main__":
    day = Day(19)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    # submit(p1, part="a", day=19, year=2021)

    # day.load(typing=str)
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=19, year=2021)
