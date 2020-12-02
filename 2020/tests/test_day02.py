import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day02 import *


@pytest.fixture(scope="function")
def day():
    day = Day(2)
    day.load(typing=str)
    return day

def test_example(day):
    data = "1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc"
    day.load(data=data, typing=str)
    assert main(day) == 2
    
def test_example_2(day):
    data = "1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc"
    day.load(data=data, typing=str)
    assert main(day, 2) == 1

def test_part1(day):
    assert main(day) == 424

def test_part2(day):
    assert main(day, 2) == 747
