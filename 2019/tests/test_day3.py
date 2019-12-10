import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day03 import *


def test_part_result():
    part1 = Day(3, 1)
    part2 = Day(3, 2)

    part1.load()

    part1.load(data={0: part1.data[0].split(","), 1: part1.data[1].split(",")})

    pathA = path(part1.data[0])
    pathB = path(part1.data[1])
    union = intersect(pathA, pathB)

    part1.answer(min(abs(coord[0]) + abs(coord[1]) for coord in union))
    part2.answer(min(pathA[coord] + pathB[coord] for coord in union))

    assert part1.result == 260
    assert part2.result == 15612


@pytest.mark.parametrize(
    "data,a1,a2",
    [
        (
            {
                0: "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(","),
                1: "U62,R66,U55,R34,D71,R55,D58,R83".split(","),
            },
            159,
            610,
        ),
        (
            {
                0: "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(","),
                1: "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(","),
            },
            135,
            410,
        ),
    ],
)
def test_given(data, a1, a2):
    part1 = Day(3, 1)
    part2 = Day(3, 2)

    part1.load(data)
    part2.load(part1.data)

    pathA = path(part1.data[0])
    pathB = path(part1.data[1])
    union = intersect(pathA, pathB)

    part1.answer(min(abs(coord[0]) + abs(coord[1]) for coord in union))
    part2.answer(min(pathA[coord] + pathB[coord] for coord in union))

    assert part1.result == a1
    assert part2.result == a2
