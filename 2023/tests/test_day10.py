import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day10 import *


@pytest.fixture(scope="function")
def example():
    day = Day(10)
    data = """.....
.S-7.
.|.|.
.L-J.
....."""

    day.load(data, process=False)
    return day


@pytest.fixture(scope="function")
def example_hard():
    day = Day(10)
    data = """..F7.
.FJ|.
SJ.L7
|F--J
LJ..."""

    day.load(data, process=False)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(10)
    day.load(process=False)
    return day


## Part 1
def test_example(example):
    assert main(example, part=1) == 4


def test_example_hard(example_hard):
    assert main(example_hard, part=1) == 8


def test_part1(day):
    assert main(day, part=1) == 6909


def test_part2(day):
    assert main(day, part=2) == 461
