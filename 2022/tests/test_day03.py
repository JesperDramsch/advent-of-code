import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day03 import *

@pytest.fixture(scope="function")
def example():
    day = Day(3)
    data = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw"""

    day.load(data)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(3)
    day.load()
    return day

def test_example(example):
    assert main(example, part=1) == 157

def test_example_p2(example):
    assert main(example, part=2) == 70

def test_part1(day):
    assert main(day, part=1) == 7691

def test_part2(day):
    assert main(day, part=2) == 2508
