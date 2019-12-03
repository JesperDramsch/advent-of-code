import sys
sys.path.insert(0, '.')
from util import Day
from day03 import *

def test_part1():
    part1 = Day(3,1)
    part2 = Day(3,2)

    part1.load()
    
    part1.load(data = {0: part1.data[0].split(","),
                       1: part1.data[1].split(",")})
    
    pathA = path(part1.data[0])
    pathB = path(part1.data[1])
    union = intersect(pathA, pathB)

    part1.answer(min(abs(coord[0])+abs(coord[1]) for coord in union))
    part2.answer(min(pathA[coord]+pathB[coord] for coord in union))

    assert part1.result == 260
    assert part2.result == 15612