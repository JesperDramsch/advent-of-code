import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day19 import *


@pytest.fixture(scope="function")
def day():
    day = Day(19)
    day.load(process=False)
    return day


def test_part1(day):
    assert main(day, part=1) == 220


def test_part2(day):
    assert main(day, part=2) == 439
