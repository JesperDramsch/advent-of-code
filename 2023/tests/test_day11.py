import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day11 import *


@pytest.fixture(scope="function")
def example():
    day = Day(11)
    data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#....."""

    day.load(data)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(11)
    day.load()
    return day


## Part 1
def test_example(example):
    assert main(example, part=1) == 374


def test_part1(day):
    assert main(day, part=1) == 9543156


## Part 2
def test_example_p2(example):
    assert main(example, part=2, space=10) == 1030
    assert main(example, part=2, space=100) == 8410


def test_part2(day):
    assert main(day, part=2) == 625243292686
