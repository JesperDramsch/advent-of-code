import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day18 import *

@pytest.fixture(scope="function")
def example():
    day = Day(18)
    data = "2 * 3 + (4 * 5)"

    day.load(data, typing=str)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(18)
    day.load(typing=str)
    return day

def test_example(example):
    assert main(example, part=1) == 26

def test_example_p2(example):
    assert main(example, part=2) == 46

def test_part1(day):
    assert main(day, part=1) == 67800526776934

def test_part2(day):
    assert main(day, part=2) == 340789638435483
