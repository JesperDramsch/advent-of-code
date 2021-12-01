import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day01 import *


@pytest.fixture(scope="function")
def example():
    day = Day(1)
    data = """199
    200
    208
    210
    200
    207
    240
    269
    260
    263"""

    day.load(data, typing=int)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(1)
    day.load(typing=int)
    return day


def test_example(example):
    assert main(example, part=1) == 7


def test_example_p2(example):
    assert main(example, part=2) == 5


def test_part1(day):
    assert main(day, part=1) == 1195


def test_part2(day):
    assert main(day, part=2) == 1235
