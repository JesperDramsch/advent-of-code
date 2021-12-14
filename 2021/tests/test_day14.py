import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day14 import *

@pytest.fixture(scope="function")
def example():
    day = Day(14)
    data = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C"""

    day.load(data, typing=str)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(14)
    day.load(typing=str)
    return day

def test_example(example):
    assert main(example, part=1) == 1588

def test_example_p2(example):
    assert main(example, part=2) == 2188189693529

def test_part1(day):
    assert main(day, part=1) == 3411

def test_part2(day):
    assert main(day, part=2) == False
