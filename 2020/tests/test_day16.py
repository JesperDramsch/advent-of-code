import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day16 import *


@pytest.fixture(scope="function")
def day():
    day = Day(16)
    day.load(process=False)
    return day


def test_example(day):
    data = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
    day.load(data, process=False)
    assert main(day, part=1) == 71


def test_part1(day):
    assert main(day, part=1) == 26026


def test_part2(day):
    assert main(day, part=2) == 1305243193339
