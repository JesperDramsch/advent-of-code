import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day02 import *

@pytest.fixture(scope="function")
def example():
    day = Day(2)
    data = """A Y
B X
C Z"""

    day.load(data)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(2)
    day.load()
    return day

def test_example(example):
    assert main(example, part=1) == 15

def test_example_p2(example):
    assert main(example, part=2) == 12

def test_part1(day):
    assert main(day, part=1) == 12679

def test_part2(day):
    assert main(day, part=2) == 14470
