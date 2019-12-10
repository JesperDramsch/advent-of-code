import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day04 import *


@pytest.mark.parametrize(
    "data,result,limit",
    [
        ("111111", 1, False),
        ("223450", 0, False),
        ("123789", 0, False),
        ("112233", 1, True),
        ("123444", 0, True),
        ("111122", 1, True),
    ],
)
def test_given(data, result, limit):
    test = Day(4, 1)
    test.load([data], sep="-")

    test.apply(check_password, limit_groups=limit)
    test.answer(sum(test.data))

    assert test.result == result


@pytest.mark.parametrize(
    "result,limit", [(495, False), (305, True),],
)
def test_part(result, limit):
    test = Day(4, 1)
    test.load(typing=int, sep="-")
    test.load(list(range(test.data[0], test.data[1] + 1)))

    test.apply(str)

    test.apply(check_password, limit_groups=limit)

    test.answer(test.sum())

    assert test.result == result
