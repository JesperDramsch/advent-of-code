# Test Working solutions to Build a nice Day Class
import sys

sys.path.insert(0, ".")
from util import Day


def test_reset():
    day = Day(1, 1)
    day.load()

    test = day.data[0]

    day.data[0] = None

    assert day.data[0] is None

    day.reset()
    assert day.data[0] == test


def test_bake():
    day = Day(1, 1)
    day.load([1, 2, 3])

    day.data = [0]

    assert day.data == [0]
    day.bake()
    assert len(day.raw_data) == 2

    day.data = [1]
    assert day.data == [1]
    day.reset()
    assert day.data == [0]
    day.hist()
    day.reset(0)
    assert len(day.raw_data) == 1
    assert type(day.raw_data) == list


def test_hist():
    day = Day(1, 1)
    day.load([1, 2, 3])

    day.hist()


def test_summary():
    day = Day(1, 1)
    day.load([1, 2, 3])

    day.summary()

    day.answer(7)

    day.summary()


def test_opcode_three_in_1():
    day = Day(5, 2)
    day.load(typing=int, sep=",")

    day.input(5)

    day.execute_opcode()

    assert day.diagnostic == 14340395


def test_opcode_three_in_2():
    day = Day(5, 1)
    day.load(typing=int, sep=",")
    day.input(1)
    day.execute_opcode()

    assert day.diagnostic == 7692125


if __name__ == "__main__":
    test_summary()
