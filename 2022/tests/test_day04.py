import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day04 import *

@pytest.fixture(scope="function")
def example():
    day = Day(4)
    data = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8"""

    day.load(data)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(4)
    day.load()
    return day

def test_example(example):
    assert main(example, part=1) == 2

def test_example_p2(example):
    assert main(example, part=2) == 4

def test_part1(day):
    assert main(day, part=1) == 576

def test_part2(day):
    assert main(day, part=2) == 905
