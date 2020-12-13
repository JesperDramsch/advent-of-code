import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day12 import *


@pytest.fixture(scope="function")
def day():
    day = Day(12)
    day.load(typing=str)
    return day


def test_example(day):
    data = """F10
N3
F7
R90
F11"""
    day.load(data, typing=str)
    assert main(day, part=1) == 25


def test_example_p2(day):
    data = """F10
N3
F7
R90
F11"""
    day.load(data, typing=str)
    assert main(day, part=2) == 286


def test_part1(day):
    assert main(day, part=1) == 636


def test_part2(day):
    assert main(day, part=2) == 26841
