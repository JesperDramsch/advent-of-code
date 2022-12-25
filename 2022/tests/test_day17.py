import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day17 import *

@pytest.fixture(scope="function")
def example():
    day = Day(17)
    data = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

    day.load(data)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(17)
    day.load()
    return day

## Part 1
def test_example(example):
    assert main(example, part=1) == 3068

def test_part1(day):
    assert main(day, part=1) == 3124

## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 1514285714288

def test_part2(day):
    assert main(day, part=2) == 1561176470569
