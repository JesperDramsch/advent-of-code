import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day07 import *

@pytest.fixture(scope="function")
def example():
    day = Day(7)
    data = """16,1,2,0,4,2,7,1,2,14"""

    day.load(data, sep=",", typing=int)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(7)
    day.load(sep=",", typing=int)
    return day

def test_example(example):
    assert main(example, part=1) == 37

def test_example_p2(example):
    assert main(example, part=2) == 168

def test_part1(day):
    assert main(day, part=1) == 352707

def test_part2(day):
    assert main(day, part=2) == 95519693
