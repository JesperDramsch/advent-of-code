import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day09 import *


@pytest.fixture(scope="function")
def example():
    day = Day(9)
    data = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45"""

    day.load(data, process=False)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(9)
    day.load(process=False)
    return day


## Part 1
def test_example(example):
    assert main(example, part=1) == 114


def test_part1(day):
    assert main(day, part=1) == 1974232246


## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 2


def test_part2(day):
    assert main(day, part=2) == 928
