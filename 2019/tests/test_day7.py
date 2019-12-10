import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day07 import *


@pytest.mark.parametrize(
    "result,phase,data",
    [
        (43210, [4, 3, 2, 1, 0], "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"),
        (
            54321,
            [0, 1, 2, 3, 4],
            "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0",
        ),
        (
            65210,
            [1, 0, 4, 3, 2],
            "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0",
        ),
    ],
)
def test_given(data, phase, result):
    amp_a = Day(7, 1)
    amp_b = Day(7, 1)
    amp_c = Day(7, 1)
    amp_d = Day(7, 1)
    amp_e = Day(7, 1)

    amps = [amp_a, amp_b, amp_c, amp_d, amp_e]

    load_all(amps, data.split(","))
    assert amp_chain(amps, phase)[0] == result


def test_part_1():
    amp_a = Day(7, 1)
    amp_b = Day(7, 1)
    amp_c = Day(7, 1)
    amp_d = Day(7, 1)
    amp_e = Day(7, 1)

    amps = [amp_a, amp_b, amp_c, amp_d, amp_e]

    load_all(amps)
    amp_e.answer(max(amp_chain(amps, num) for num in permutations(range(5))), v=True)
    assert amp_e.result[0] == 79723


@pytest.mark.parametrize(
    "result,phase,data",
    [
        (
            139629729,
            [9, 8, 7, 6, 5],
            "3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5",
        ),
        (
            18216,
            [9, 7, 8, 5, 6],
            "3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10",
        ),
    ],
)
def test_given_2(data, phase, result):
    amp_a = Day(7, 2)
    amp_b = Day(7, 2)
    amp_c = Day(7, 2)
    amp_d = Day(7, 2)
    amp_e = Day(7, 2)

    amps = [amp_a, amp_b, amp_c, amp_d, amp_e]

    for amp in amps:
        amp.debug = False
        amp.concurrent = True

    load_all(amps, data.split(","))
    feedback(amps, phase)
    assert amp_e.result == result

    # Having these together guarantees good reset

    for amp in amps:
        amp.reset(1)  # Reset all amps to state after loading and int conversion

    load_all(amps, data.split(","))
    feedback(amps, phase)
    assert amp_e.result == result


def test_part2():
    amp_a = Day(7, 2)
    amp_b = Day(7, 2)
    amp_c = Day(7, 2)
    amp_d = Day(7, 2)
    amp_e = Day(7, 2)

    amps = [amp_a, amp_b, amp_c, amp_d, amp_e]

    for amp in amps:
        amp.concurrent = True

    load_all(amps)
    amp_e.answer(max(feedback(amps, num) for num in permutations(range(5, 10))), v=True)

    assert amp_e.result == 70602018
