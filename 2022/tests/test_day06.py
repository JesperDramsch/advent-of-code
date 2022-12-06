import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day06 import *

@pytest.fixture(scope="function")
def example():
    day = Day(6)
    data = """mjqjpqmgbljsphdztnvjfqwrcgsmlb"""

    day.load(data, process=False)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(6)
    day.load(process=False)
    return day

def test_example(example):
    assert main(example, part=1) == 7

def test_example_p2(example):
    assert main(example, part=2) == 19

def test_part1(day):
    assert main(day, part=1) == 1175

def test_part2(day):
    assert main(day, part=2) == 3217
