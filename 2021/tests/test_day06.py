import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day06 import *

@pytest.fixture(scope="function")
def example():
    day = Day(6)
    data = """3,4,3,1,2"""

    day.load(data, sep=",", typing=int)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(6)
    day.load(sep=",", typing=int)
    return day

def test_example(example):
    assert main(example, part=1) == 5934

def test_example_p2(example):
    assert main(example, part=2) == 26984457539

def test_part1(day):
    assert main(day, part=1) == 383160

def test_part2(day):
    assert main(day, part=2) == 1721148811504
