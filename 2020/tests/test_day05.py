import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day05 import *


@pytest.fixture(scope="function")
def day():
    day = Day(5)
    day.load(typing=str)
    return day


def test_example(day):
    data = "FBFBBFFRLR\nBFFFBBFRRR\nFFFBBBFRRR\nBBFFBBFRLL"
    day.load(data, typing=str)
    day.apply(seat_id)
    assert day.data == [357, 567, 119, 820]
    day.load(data, typing=str)
    assert main(day, part=1) == 820


def test_part1(day):
    assert main(day, part=1) == 938


def test_part2(day):
    assert main(day, part=2) == 696
