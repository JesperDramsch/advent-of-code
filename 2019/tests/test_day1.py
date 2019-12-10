# Test Working solutions to Build a nice Day Class
import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day01 import *


def test_part1():
    part1 = Day(1, 1)
    part1.load(typing=int)
    assert sum(part1.apply(fuel)) == 3279287


@pytest.mark.parametrize("data,result", [(12, 2), (14, 2), (1969, 654), (100756, 33583)])
def test_part1_given(data, result):
    part1 = Day(1, 1)
    part1.load(typing=int, data=[data])
    part1.answer(sum(part1.apply(fuel)))
    assert part1.result == result


def test_part2():
    part2 = Day(1, 2)
    part2.load(typing=int)
    assert sum(part2.apply(fuelchain)) == 4916076


@pytest.mark.parametrize("data,result", [(12, 2), (1969, 966), (100756, 50346)])
def test_part2_given(data, result):
    part2 = Day(1, 2)
    part2.load(typing=int, data=[data])
    part2.answer(sum(part2.apply(fuelchain)))
    assert part2.result == result
