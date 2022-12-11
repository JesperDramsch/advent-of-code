import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day{number:02d} import *

@pytest.fixture(scope="function")
def example():
    day = Day({number})
    data = """"""

    day.load(data)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day({number})
    day.load()
    return day

## Part 1
def test_example(example):
    assert main(example, part=1) == False

def test_part1(day):
    assert main(day, part=1) == False

## Part 2
def test_example_p2(example):
    assert main(example, part=2) == False

def test_part2(day):
    assert main(day, part=2) == False
