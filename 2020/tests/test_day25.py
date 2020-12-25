import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day25 import *


@pytest.fixture(scope="function")
def example():
    day = Day(25)
    data = "5764801\n17807724"

    day.load(data, typing=str)
    return day


@pytest.fixture(scope="function")
def day():
    day = Day(25)
    day.load(typing=str)
    return day


def test_example(example):
    assert main(example, part=1) == 14897079


def test_part1(day):
    assert main(day, part=1) == 18293391

