import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day24 import *

@pytest.fixture(scope="function")
def example():
    day = Day(24)
    data = """"""

    day.load(data, typing=str)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(24)
    day.load(typing=str)
    return day

def test_example(example):
    assert main(example, part=1) == False

def test_example_p2(example):
    assert main(example, part=2) == False

def test_part1(day):
    assert main(day, part=1) == False

def test_part2(day):
    assert main(day, part=2) == False
