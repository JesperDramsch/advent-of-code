import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day08 import *

def test_given_1():
    part1 = Day(9, 1)

    quine = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]

    part1.load(quine.copy())
    part1.execute_opcode()
    
    assert part1[:len(quine)] == quine

def test_given_2():    
    part1 = Day(9, 1)
    part1.load([1102,34915192,34915192,7,4,7,99,0])
    part1.execute_opcode()

    assert len(str(part1.result)) == 16
    
    
def test_given_3():
    part1 = Day(9, 1)
    middle = [104,1125899906842624,99]
    part1.load(middle.copy())
    out = part1.execute_opcode()

    assert middle[1] == part1.result

@pytest.mark.parametrize(
    "tty,result",
    [
        (1,3989758265),
        (2,76791),
    ],
)
def test_parts(tty, result):
    day = Day(9, 1)
    day.load(typing=int, sep=",")

    day.input(tty)
    day.execute_opcode()
    assert day.result == result