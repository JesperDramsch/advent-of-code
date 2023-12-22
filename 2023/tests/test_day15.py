import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day15 import *


@pytest.fixture(scope="function")
def example():
    day = Day(15)
    data = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

    day.load(data, process=False)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(15)
    day.load(process=False)
    return day


## Part 1
def test_example(example):
    assert main(example, part=1) == 1320


def test_part1(day):
    assert main(day, part=1) == 514025


## Part 2
def test_example_p2(example):
    assert main(example, part=2) == False


def test_part2(day):
    assert main(day, part=2) == False
