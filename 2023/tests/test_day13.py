import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day13 import *


@pytest.fixture(scope="function")
def example():
    day = Day(13)
    data = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

    day.load(data, process=False)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(13)
    day.load(process=False)
    return day


## Part 1
def test_example(example):
    assert main(example, part=1) == 405


def test_part1(day):
    assert main(day, part=1) == 37975


## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 400


def test_part2(day):
    assert main(day, part=2) == 32497
