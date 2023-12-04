import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day04 import *


@pytest.fixture(scope="function")
def example():
    day = Day(4)
    data = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

    day.load(data)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(4)
    day.load()
    return day


## Part 1
def test_example(example):
    assert main(example, part=1) == 13


def test_part1(day):
    assert main(day, part=1) == 23235


## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 30


def test_part2(day):
    assert main(day, part=2) == 5920640
