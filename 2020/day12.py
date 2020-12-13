from util import Day
from aocd import submit
import numpy as np
from collections import deque


def preprocess(row):
    return row[:1], int(row[1:].strip())


class Vessel:
    def __init__(self, wp=None):

        self.q = deque()
        self.orientation = 0  # Define East as 0°
        self.x, self.y = 0, 0
        self.wp = wp
        if wp is None:
            self.wpx, self.wpy = 0, 0
        else:
            self.wpx, self.wpy = wp

    def turn(self, direction="R", degree=90):
        degree *= [1, -1][direction == "R"]
        self.orientation = (self.orientation - degree) % 360

        if self.wp is not None:
            rad = np.deg2rad(degree)
            self.wpx, self.wpy = (
                round(self.wpx * np.cos(rad) - self.wpy * np.sin(rad)),
                round(self.wpx * np.sin(rad) + self.wpy * np.cos(rad)),
            )

    def move(self, direction, distance):
        if "N" in direction:
            self.wpy += distance
        elif "E" in direction:
            self.wpx += distance
        elif "S" in direction:
            self.wpy -= distance
        elif "W" in direction:
            self.wpx -= distance

        if "F" in direction:
            rad = np.deg2rad(self.orientation)
            if self.wp is None:
                self.wpx += distance * np.cos(rad)
                self.wpy += distance * -np.sin(rad)
                self.x = self.wpx
                self.y = self.wpy
            else:
                self.x += self.wpx * distance
                self.y += self.wpy * distance

    def queue(self, inp):
        self.q.extend(inp)

    def route(self):
        for inst in self.q:
            self.instruct(inst)

    def instruct(self, command):
        comm, num = command
        if comm in "RL":
            self.turn(comm, num)
        else:
            self.move(comm, num)

    def distance(self):
        return int(abs(self.x) + abs(self.y))


def main(day, part=1):
    day.apply(preprocess)
    if part == 1:
        ferry = Vessel()
    if part == 2:
        ferry = Vessel((10, 1))
    ferry.queue(day.data)
    ferry.route()
    return ferry.distance()


if __name__ == "__main__":
    day = Day(12)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=12, year=2020)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=12, year=2020)
