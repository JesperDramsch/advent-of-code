import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day05 import *


def test_given_0():
    test = Day(4, 1)
    test.load([1002, 4, 3, 4, 33], sep=",")

    test.execute_opcode()
    print(test.answer(test.data[4]))
    assert test.result == 99


def test_part1(monkeypatch):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    monkeypatch.setattr("builtins.input", lambda x: "1")

    part1 = Day(5, 1)
    part1.load(typing=int, sep=",").execute_opcode()

    assert part1.diagnostic == 7692125


@pytest.mark.parametrize(
    "part1_in,part2_in,data",
    [
        ("8", "11", [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]),
        ("-1", "8", [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]),
        ("8", "88", [3, 3, 1108, -1, 8, 3, 4, 3, 99]),
        ("7", "8", [3, 3, 1107, -1, 8, 3, 4, 3, 99]),
    ],
)
def test_given_jump(monkeypatch, data, part1_in, part2_in):
    part1 = Day(5, 2)
    part1.load(data, sep=",")

    monkeypatch.setattr("builtins.input", lambda x: part1_in)
    part1.execute_opcode()
    assert part1.diagnostic == 1

    part1.reset()
    monkeypatch.setattr("builtins.input", lambda x: part2_in)
    part1.execute_opcode()
    assert part1.diagnostic == 0


@pytest.mark.parametrize(
    "part1_in,part2_in,data",
    [
        ("0", "1", [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]),
        ("0", "1", [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]),
    ],
)
def test_given_1(monkeypatch, data, part1_in, part2_in):
    part1 = Day(5, 2)
    part1.load(data, sep=",")

    monkeypatch.setattr("builtins.input", lambda x: part1_in)
    part1.execute_opcode()
    assert part1.diagnostic == 0

    part1.reset()
    monkeypatch.setattr("builtins.input", lambda x: part2_in)
    part1.execute_opcode()
    assert part1.diagnostic == 1


@pytest.mark.parametrize(
    "type_in,result", [("0", 999), ("8", 1000), ("9", 1001),],
)
def test_given_long(monkeypatch, type_in, result):
    part1 = Day(5, 2)
    part1.load(
        [
            3,
            21,
            1008,
            21,
            8,
            20,
            1005,
            20,
            22,
            107,
            8,
            21,
            20,
            1006,
            20,
            31,
            1106,
            0,
            36,
            98,
            0,
            0,
            1002,
            21,
            125,
            20,
            4,
            20,
            1105,
            1,
            46,
            104,
            999,
            1105,
            1,
            46,
            1101,
            1000,
            1,
            20,
            4,
            20,
            1105,
            1,
            46,
            98,
            99,
        ],
        sep=",",
    )

    monkeypatch.setattr("builtins.input", lambda x: type_in)
    part1.execute_opcode()
    assert part1.diagnostic == result


def test_part2(monkeypatch):

    # monkeypatch the "input" function, so that it returns "Mark".
    # This simulates the user entering "Mark" in the terminal:
    monkeypatch.setattr("builtins.input", lambda x: "5")

    part2 = Day(5, 2)
    part2.load(typing=int, sep=",").execute_opcode()

    assert part2.diagnostic == 14340395
