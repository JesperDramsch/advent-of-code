import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day23 import *

@pytest.fixture(scope="function")
def example():
    day = Day(23)
    data = "389125467"

    day.load(data, process=False)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(23)
    day.load(process=False)
    return day

def test_example(example):
    assert main(example, part=1) == "67384529"

def test_example_p2(example):
    assert main(example, part=2) == 149245887792

def test_part1(day):
    assert main(day, part=1) == "38756249"

def test_part2(day):
    assert main(day, part=2) == 21986479838
