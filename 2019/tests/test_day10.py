import sys
import pytest

sys.path.insert(0, ".")
from util import Day
from day10 import *


# @pytest.mark.parametrize(
#     "center,obj,mask",
#     [
#         ([3, 2], [3, 2], [(3, 2)]),
#         ([1, 2], [2, 2], [(3, 2), (4, 2)]),
#         ([0, 0], [1, 1], [(2, 2), (3, 3), (4, 4)]),
#         ([0, 0], [3, 3], [(4, 4)]),
#         ([0, 0], [2, 2], [(3, 3), (4, 4)]),
#         ([2, 2], [1, 1], [(0, 0)]),
#         ([4, 4], [3, 2], [(2, 0)]),
#     ],
# )
# def test_shadow_masks(center, obj, mask):
#     part1 = Day(10, 1)

#     raw_data = """.#..#
# .....
# #####
# ....#
# ...##""".split()

#     part1.load(raw_data, sep="\n")

#     part1.data = process_map(part1.data)

#     comp_data = part1.data.copy()
#     for keys in mask:
#         comp_data.pop(keys, None)

#     assert comp_data == shadow(part1.data, center, obj)


@pytest.mark.parametrize(
    "center,obj,mask",
    [([3, 2], [[3, 2]], [(3, 2)]), ([1, 2], [[1, 2], [2, 2]], [(1, 2), (3, 2), (4, 2)]),],
)
def test_shadow_all(center, obj, mask):
    part1 = Day(10, 1)

    raw_data = """.#..#
.....
#####
....#
...##""".split()

    part1.load(raw_data, sep="\n")

    part1.data = process_map(part1.data)

    comp_data = part1.data.copy()
    for keys in mask:
        comp_data.discard(keys)
    assert comp_data == all_shadows(part1.data, center, obj)


@pytest.mark.parametrize(
    "result,data",
    [
        (
            8,
            """.#..#
.....
#####
....#
...##""",
        ),
        (
            33,
            """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####""",
        ),
        (
            35,
            """#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.""",
        ),
        (
            41,
            """.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..""",
        ),
        (
            210,
            """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""",
        ),
    ],
)
def test_starcounts(data, result):
    part1 = Day(10, 1)

    raw_data = data.split()

    part1.load(raw_data, sep="\n")

    part1.data = process_map(part1.data)

    print(part1.data)

    print(count_visible(part1.data)[0])

    part1.answer(count_visible(part1.data)[0], v=1)

    assert part1.result == result


def test_part1():
    part1 = Day(10, 1)

    part1.load(sep="\n")

    part1.data = process_map(part1.data)

    part1.answer(count_visible(part1.data)[0], v=1)

    assert part1.result == 334

def test_given_part2():
    part2 = Day(10, 2)
    raw_data = """.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....X...###..
..#.#.....#....##""".split("\n")
    part2.load(raw_data, sep="\n")
    part2.data = process_map(part2.data)
    assert wazer_wifle(part2.data, (8,4), 3) == (9, 1)

    raw_data = """.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""".split("\n")
    
    part2.load(raw_data, sep="\n")
    part2.data = process_map(part2.data)

    shtuff = [1, 2, 3, 10, 20, 50, 100, 199, 200, 201]
    solved = [(11, 12), (12, 1), (12, 2), (12, 8), (16, 0), (16, 9), (10, 16), (9, 6), (8, 2), (10, 9)]
    for i, el in enumerate(shtuff):
        data = wazer_wifle(part2.data, (11, 13), el)
        print(f"The {el} asteroid to be  vaporized is at: ", data)
        assert data == solved[i]

def test_part2():
    part2 = Day(10, 2)
    part2.load(sep="\n")

    part2.data = process_map(part2.data)

    part2.answer(wazer_wifle(part2.data, (23, 20), 200), v=2)

    assert part2.result[0]*100 + part2.result[1] == 1119