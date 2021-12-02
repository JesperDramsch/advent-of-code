import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day02 import *

@pytest.fixture(scope="function")
def example():
    day = Day(2)
    data = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

    day.load(data, typing=str)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(2)
    day.load(typing=str)
    return day

def test_example(example):
    assert main(example, part=1) == 150

def test_example_p2(example):
    assert main(example, part=2) == 900

def test_part1(day):
    assert main(day, part=1) == 2147104

def test_part2(day):
    assert main(day, part=2) == 2044620088
