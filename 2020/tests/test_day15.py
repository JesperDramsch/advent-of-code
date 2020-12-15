import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day15 import *

@pytest.fixture(scope="function")
def day():
    day = Day(15)
    day.load(sep=",")
    return day

def test_example(day):
    data = "0,3,6"
    day.load(data, sep=",")
    assert main(day, part=1) == 436
    data = "1,3,2"
    day.load(data, sep=",")
    assert main(day, part=1) == 1
    data = "2,1,3"
    day.load(data, sep=",")
    assert main(day, part=1) == 10
    data = "1,2,3"
    day.load(data, sep=",")
    assert main(day, part=1) == 27
    data = "2,3,1"
    day.load(data, sep=",")
    assert main(day, part=1) == 78
    data = "3,2,1"
    day.load(data, sep=",")
    assert main(day, part=1) == 438
    data = "3,1,2"
    day.load(data, sep=",")
    assert main(day, part=1) == 1836

def test_example_p2(day):
    data = "0,3,6"
    day.load(data, sep=",")
    assert main(day, part=2) == 175594
    data = "1,3,2"
    day.load(data, sep=",")
    assert main(day, part=2) == 2578
    data = "2,1,3"
    day.load(data, sep=",")
    assert main(day, part=2) == 3544142
    data = "1,2,3"
    day.load(data, sep=",")
    assert main(day, part=2) == 261214
    data = "2,3,1"
    day.load(data, sep=",")
    assert main(day, part=2) == 6895259
    data = "3,2,1"
    day.load(data, sep=",")
    assert main(day, part=2) == 18
    data = "3,1,2"
    day.load(data, sep=",")
    assert main(day, part=2) == 362

def test_part1(day):
    assert main(day, part=1) == 447

def test_part2(day):
    assert main(day, part=2) == 11721679
