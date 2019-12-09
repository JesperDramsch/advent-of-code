import sys

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

def test_part_1():
    part1 = Day(9, 1)
    part1.load(typing=int, sep=",")

    part1.input(1)
    part1.execute_opcode()
    assert part1.result == 3989758265


def test_part_2():
    part1 = Day(9, 2)
    part1.load(typing=int, sep=",")

    part1.input(2)
    part1.execute_opcode()
    assert part1.result == 76791