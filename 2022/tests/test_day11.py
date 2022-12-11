import sys
import pytest

sys.path.insert(0, ".")
from day import Day
from day11 import *

@pytest.fixture(scope="function")
def example():
    day = Day(11)
    data = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

    day.load(data)
    return day

@pytest.fixture(scope="function")
def day():
    day = Day(11)
    day.load()
    return day

## Part 1
def test_example(example):
    assert main(example, part=1) == 10605

def test_part1(day):
    assert main(day, part=1) == 95472

## Part 2
def test_example_p2(example):
    assert main(example, part=2) == 2713310158

def test_part2(day):
    assert main(day, part=2) == 17926061332
