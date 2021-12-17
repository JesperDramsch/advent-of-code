import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day17 import *

@pytest.fixture(scope="function")
def example():
    day = Day(17)
    data = """target area: x=20..30, y=-10..-5"""

    day.load(data, typing=str)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(17)
    day.load(typing=str)
    return day

def test_example(example):
    assert main(example, part=1) == 45

def test_example_p2(example):
    assert main(example, part=2) == 112

def test_part1(day):
    assert main(day, part=1) == 7626

def test_part2(day):
    assert main(day, part=2) == 2032
