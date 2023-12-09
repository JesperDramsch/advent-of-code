import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day08 import *


@pytest.fixture(scope="function")
def example():
    day = Day(8)
    data = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""

    day.load(data, process=False)
    return day


@pytest.fixture(scope="function")
def example2():
    day = Day(8)
    data = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)"""

    day.load(data, process=False)
    return day


@pytest.fixture(scope="function")
def example3():
    day = Day(8)
    data = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

    day.load(data, process=False)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(8)
    day.load(process=False)
    return day


## Part 1
def test_example(example):
    assert main(example, part=1) == 2


def test_example2(example2):
    assert main(example2, part=1) == 6


def test_part1(day):
    assert main(day, part=1) == 13207


## Part 2
def test_example_p2(example2):
    assert main(example2, part=2) == 6


def test_part2(day):
    assert main(day, part=2) == 12324145107121
