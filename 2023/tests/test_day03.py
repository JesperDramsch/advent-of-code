import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day03 import *


@pytest.fixture(scope="function")
def example():
    day = Day(3)
    data = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

    day.load(data)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(3)
    day.load()
    return day


## Part 1
def test_example(example):
    assert main(example, part=1) == 4361


def test_part1(day):
    assert main(day, part=1) == 525911


## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 467835


def test_part2(day):
    assert main(day, part=2) == 75805607
