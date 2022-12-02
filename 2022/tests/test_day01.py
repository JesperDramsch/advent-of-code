import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day01 import *

@pytest.fixture(scope="function")
def example():
    day = Day(1)
    data = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000"""

    day.load(data, typing=str)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(1)
    day.load(typing=str)
    return day

def test_example(example):
    assert main(example, part=1) == 24_000

def test_example_p2(example):
    assert main(example, part=2) == 45_000

def test_part1(day):
    assert main(day, part=1) == 72_602

def test_part2(day):
    assert main(day, part=2) == 207_410
