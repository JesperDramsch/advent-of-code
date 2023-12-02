import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day02 import *


@pytest.fixture(scope="function")
def example():
    day = Day(2)
    data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

    day.load(data, typing=str)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(2)
    day.load(typing=str)
    return day


## Part 1
def test_example(example):
    assert main(example, part=1) == 8


def test_part1(day):
    assert main(day, part=1) == 3035


## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 2286


def test_part2(day):
    assert main(day, part=2) == 66027
