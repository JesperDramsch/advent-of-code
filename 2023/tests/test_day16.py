import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day16 import *


@pytest.fixture(scope="function")
def example():
    day = Day(16)
    data = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|...."""

    day.load(data)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(16)
    day.load()
    return day


## Part 1
def test_example(example):
    assert main(example, part=1) == 46


def test_part1(day):
    assert main(day, part=1) == 6921


## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 51


def test_part2(day):
    assert main(day, part=2) == 7594
