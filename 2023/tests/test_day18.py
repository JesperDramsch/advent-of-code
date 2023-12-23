import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day18 import *


@pytest.fixture(scope="function")
def example():
    day = Day(18)
    data = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)"""

    day.load(data)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(18)
    day.load()
    return day


## Part 1
def test_example(example):
    assert main(example, part=1) == 62


def test_part1(day):
    assert main(day, part=1) == 52055


## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 952408144115


def test_part2(day):
    assert main(day, part=2) == 67622758357096
