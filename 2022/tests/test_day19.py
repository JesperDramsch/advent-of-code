import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day19 import *

@pytest.fixture(scope="function")
def example():
    day = Day(19)
    data = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian."""

    day.load(data)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(19)
    day.load()
    return day

## Part 1
def test_example(example):
    assert main(example, part=1) == 33

def test_part1(day):
    assert main(day, part=1) == False

## Part 2
def test_example_p2(example):
    assert main(example, part=2) == False

def test_part2(day):
    assert main(day, part=2) == False
