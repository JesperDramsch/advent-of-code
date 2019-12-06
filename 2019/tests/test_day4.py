import sys

sys.path.insert(0, ".")
from util import Day
from day04 import *


def test_given_1():
    test = Day(4, 1)
    test.load(["111111"], sep="-")

    test.apply(check_password)
    test.answer(sum(test.data))

    assert test.result == 1


def test_given_2():
    test = Day(4, 1)
    test.load(["223450"], sep="-")

    test.apply(check_password)
    test.answer(sum(test.data))

    assert test.result == 0


def test_given_3():
    test = Day(4, 1)
    test.load(["123789"], sep="-")

    test.apply(check_password)
    test.answer(sum(test.data))

    assert test.result == 0


def test_part1():
    test = Day(4, 1)
    test.load(typing=int, sep="-")
    test.load(list(range(test.data[0], test.data[1] + 1)))

    test.apply(str)

    test.apply(check_password)

    test.answer(test.sum())

    assert test.result == 495


def test_given_4():
    test = Day(4, 1)
    test.load(["112233"], sep="-")

    test.apply(check_password, limit_groups=True)
    test.answer(test.sum())

    assert test.result == 1


def test_given_5():
    test = Day(4, 1)
    test.load(["123444"], sep="-")

    test.apply(check_password, limit_groups=True)
    test.answer(test.sum())

    assert test.result == 0


def test_given_6():
    test = Day(4, 1)
    test.load(["111122"], sep="-")

    test.apply(check_password, limit_groups=True)
    test.answer(test.sum())

    assert test.result == 1


def test_part2():
    part2 = Day(4, 2)

    part2.load(typing=int, sep="-")
    part2.load(list(range(part2.data[0], part2.data[1] + 1)))

    part2.apply(str)

    part2.apply(check_password, limit_groups=True)
    part2.answer(part2.sum())

    assert part2.result == 305
