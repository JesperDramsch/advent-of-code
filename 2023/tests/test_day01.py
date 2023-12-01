import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day01 import *


@pytest.fixture(scope="function")
def example():
    day = Day(1)
    data = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

    day.load(data, typing=str)
    return day


@pytest.fixture(scope="function")
def example_2():
    day = Day(1)
    data = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

    day.load(data, typing=str)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(1)
    day.load(typing=str)
    return day


## Part 1
def test_example(example):
    assert main(example, part=1) == 142


def test_part1(day):
    assert main(day, part=1) == 54159


## Part 2
def test_example_p2(example_2):
    assert main(example_2, part=2) == 281


def test_part2(day):
    assert main(day, part=2) == 53866
