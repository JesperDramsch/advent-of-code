# Test Working solutions to Build a nice Day Class
import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day02 import *


def test_part1():
    part1 = Day(2, 1)
    part1.load(typing=int, sep=",")

    part1.data[1] = 12
    part1.data[2] = 2
    assert compute(part1.data)[0] == 3101878


def test_part2():
    part2 = Day(2, 2)
    part2.load(typing=int, sep=",")

    part2.data[1] = 84
    part2.data[2] = 44
    assert compute(part2.data)[0] == 19690720


@pytest.mark.parametrize(
    "data,index,result",
    [
        ([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], 0, 3500),
        ([1, 0, 0, 0, 99, 0, 0, 0, 99], 0, 2),
        ([2, 4, 4, 5, 99, 0], 5, 9801),
        ([1, 1, 1, 4, 99, 5, 6, 0, 99], 0, 30),
    ],
)
def test_given(data, index, result):
    part1_obj = Day(2, 1)
    part1_obj.load(data)
    part1_obj.execute_opcode()
    print(part1_obj.answer(part1_obj.data[index]))
    assert part1_obj.result == result
