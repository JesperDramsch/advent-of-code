from util import Day
from aocd import submit
import numpy as np


def preprocess(row):
    return row[:1], int(row[1:].strip())


class Vessel:
    def __init__(self, wp=None):
        self.x = 0
        self.y = 0
        if wp is None:
            self.wp_x, self.wp_y = (0, 0)
        else:
            self.wp_x, self.wp_y = wp

        self.orientation = 0  # Define East as 0°

    def turn(self, direction="R", degree=90):
        if direction == "L":
            self.orientation = (self.orientation - degree) % 360
        elif direction == "R":
            self.orientation = (self.orientation + degree) % 360

    def move(self, direction, distance):
        if "N" in direction:
            self.y += distance
        if "E" in direction:
            self.x += distance
        if "S" in direction:
            self.y -= distance
        if "W" in direction:
            self.x -= distance
        if "F" in direction:
            rad = np.deg2rad(self.orientation)
            self.x += distance * np.cos(rad)
            self.y -= distance * np.sin(rad)

    def instruct(self, command):
        comm, num = command
        if comm in "RL":
            self.turn(comm, num)
        else:
            self.move(comm, num)
        # print(command, self.x, self.y, self.orientation)

    def distance(self):
        return abs(self.x) + abs(self.y)


def main(day, part=1):
    day.apply(preprocess)
    if part == 1:
        ferry = Vessel()
        for inst in day.data:
            ferry.instruct(inst)
        out = int(ferry.distance())
    if part == 2:
        out=-1
    return out


if __name__ == "__main__":
    day = Day(12)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=12, year=2020)

    # day.load(typing=str)
    # 2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=12, year=2020)
