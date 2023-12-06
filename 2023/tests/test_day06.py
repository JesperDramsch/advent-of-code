import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day06 import *


@pytest.fixture(scope="function")
def example():
    day = Day(6)
    data = """Time:      7  15   30
Distance:  9  40  200"""

    day.load(data)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(6)
    day.load()
    return day


## Part 1
def test_example(example):
    assert main(example, part=1) == 288


def test_part1(day):
    assert main(day, part=1) == 220320


## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 71503


def test_part2(day):
    assert main(day, part=2) == 34454850
