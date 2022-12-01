from util import Day
from aocd import submit
import re


def probe_trajectory(trajectory, target):
    x, y, y_max = 0, 0, 0
    x_vel, y_vel = trajectory
    while y > target[2]:
        x += x_vel
        y += y_vel
        if x_vel > 0:
            x_vel -= 1
        y_vel -= 1

        if y > y_max:
            y_max = y

        if target[0] <= x <= target[1] and target[2] <= y <= target[3]:
            return x_vel, y_vel, y_max


def find_trajectories(target):
    y_maxes, velocities = [] , []
    for y_vel in range(target[2], -target[2] + 1):
        for x_vel in range(target[1] + 1):
            hit_or_miss = probe_trajectory((x_vel, y_vel), target)
            if hit_or_miss is not None:
                y_maxes.append(hit_or_miss[2])
                velocities.append(hit_or_miss[:2])
    return velocities, y_maxes


def parse_target(target):
    x1, x2, y1, y2 = map(int, re.findall(r"(-*\d+)", target))
    x_min, x_max = min(x1, x2), max(x1, x2)
    y_min, y_max = min(y1, y2), max(y1, y2)
    return x_min, x_max, y_min, y_max


def main(day, part=1):
    day.data = parse_target(day.data[0])
    velocities, y_maxes = find_trajectories(day.data)
    if part == 1:
        return max(y_maxes)
    if part == 2:
        return len(velocities)


if __name__ == "__main__":
    day = Day(17)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=17, year=2021)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=17, year=2021)
