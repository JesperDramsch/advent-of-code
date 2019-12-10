from util import Day


def process_map(data):
    out_data = {}
    for i, el in enumerate(data):
        for j, val in enumerate(el.strip()):
            if val == "#":
                out_data[(j, i)] = True
    return out_data


def shadow(data, center: tuple, obj: tuple):

    cx, cy = center
    ox, oy = obj

    masks = data.copy()
    if center == obj:
        masks.pop((cx, cy), None)
        return masks

    ix, iy = ox - cx, oy - cy

    # Find the greatest common denominator
    for ii in range(10, 1, -1):
        if ix % ii == 0 and iy % ii == 0:
            ix = ix // ii
            iy = iy // ii

    x, y = zip(*data.keys())
    max_x, max_y = max(x), max(y)

    dx = ox + ix
    dy = oy + iy

    while 0 <= dx <= max_x and 0 <= dy <= max_y:
        masks.pop((dx, dy), None)
        dx += ix
        dy += iy
    return masks


def all_shadows(data, center, asteroids):

    masks = data.copy()

    for asteroid in asteroids:
        masks = shadow(masks, center, asteroid)

    return masks


def count_visible(data):

    star_map = data.copy()
    # print(data)

    for asteroid in data.keys():
        star_map[asteroid] = len(all_shadows(data, asteroid, data.keys()))

    new_base = max(star_map, key=star_map.get)

    return star_map[new_base], new_base, star_map


def wazer_wifle(data, center, num):
    from math import atan2

    cx, cy = center

    seen = all_shadows(data, center, data.keys())

    # rotate = [(x, 0) for x in range(cx, max_x)] # center x out at y=0
    # rotate.extend([(max_x-1, y) for y in range(1,max_y)]) # down y
    # rotate.extend([(x, max_y-1) for x in range(max_x-2, -1, -1)]) # back in x
    # rotate.extend([(0, y) for y in range(max_y-2, -1, -1)]) # up y
    # rotate.extend([(x,0) for x in range(1, cx)]) # back to start

    # Nice idea, if it sampled everything. Let's go polar!

    return sorted(((atan2((x - cx), (y - cy)), (x, y)) for x, y in seen.keys()), reverse=True)[
        num - 1
    ][1]


if __name__ == "__main__":

    part2 = Day(10, 2)
    raw_data = """.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....X...###..
..#.#.....#....##""".split(
        "\n"
    )
    part2.load(raw_data, sep="\n")
    part2.data = process_map(part2.data)
    print(wazer_wifle(part2.data, (8, 4), 3))

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
###.##.####.##.#..##""".split(
        "\n"
    )

    part2.load(raw_data, sep="\n")
    part2.data = process_map(part2.data)

    shtuff = [1, 2, 3, 10, 20, 50, 100, 199, 200, 201]

    for el in shtuff:
        print(f"The {el} asteroid to be  vaporized is at: ", wazer_wifle(part2.data, (11, 13), el))

    part2.load(sep="\n")

    part2.data = process_map(part2.data)

    station = count_visible(part2.data)[1]
    print(station)
    part2.answer(wazer_wifle(part2.data, station, 200), v=2)

    print(part2.result[0] * 100 + part2.result[1])

#     part1 = Day(10, 1)

#     raw_data = """.#..#
# .....
# #####
# ....#
# ...##""".split()

#     part1.load(raw_data, sep="\n")

#     part1.data = process_map(part1.data)

#     #print(part1.data)

#     print(all_shadows(part1.data, (0, 1), part1.data.keys()))


#     print(shadow(part1.data, (0, 1), (0,2)))

#     part1.answer(count_visible(part1.data)[0], v=1)

#     raw_data = """......#.#.
# #..#.#....
# ..#######.
# .#.#.###..
# .#..#.....
# ..#....#.#
# #..#....#.
# .##.#..###
# ##...#..#.
# .#....####""".split()

#     part1.load(raw_data, sep="\n")

#     part1.data = process_map(part1.data)

#     part1.answer(count_visible(part1.data)[0], v=1)

#     raw_data = """#.#...#.#.
# .###....#.
# .#....#...
# ##.#.#.#.#
# ....#.#.#.
# .##..###.#
# ..#...##..
# ..##....##
# ......#...
# .####.###.""".split()

#     part1.load(raw_data, sep="\n")

#     part1.data = process_map(part1.data)

#     part1.answer(count_visible(part1.data)[0], v=1)

#     raw_data = """.#..#..###
# ####.###.#
# ....###.#.
# ..###.##.#
# ##.##.#.#.
# ....###..#
# ..#.#..#.#
# #..#.#.###
# .##...##.#
# .....#.#..""".split()

#     part1.load(raw_data, sep="\n")

#     part1.data = process_map(part1.data)

#     part1.answer(count_visible(part1.data)[0], v=1)


#     raw_data = """.#..##.###...#######
# ##.############..##.
# .#.######.########.#
# .###.#######.####.#.
# #####.##.#.##.###.##
# ..#####..#.#########
# ####################
# #.####....###.#.#.##
# ##.#################
# #####.##.###..####..
# ..######..##.#######
# ####.##.####...##..#
# .#####..#.######.###
# ##...#.##########...
# #.##########.#######
# .####.#.###.###.#.##
# ....##.##.###..#####
# .#.#.###########.###
# #.#.#.#####.####.###
# ###.##.####.##.#..##""".split()

# part1.load(raw_data, sep="\n")

# part1.data = process_map(part1.data)

# part1.answer(count_visible(part1.data)[0], v=1)

# part1.load(sep="\n")

# part1.data = process_map(part1.data)

# part1.answer(count_visible(part1.data)[0], v=1)

