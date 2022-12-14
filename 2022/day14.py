from day import Day
from aocd import submit


def create_grid(data):
    grid = set()
    max_depth = 0
    for line in data:
        for (a, b), (x, y) in zip(line, line[1:]):
            for i in range(min(a, x), max(a, x) + 1):
                for ii in range(min(b, y), max(b, y) + 1):
                    grid.add(i + ii*1j)
                    max_depth = max(max_depth, ii)
    return grid, max_depth + 1


def sand_grain(grid, max_depth, floor=None):
    loc = complex(500)

    if floor is not None:
        max_depth = floor

    while loc.imag < max_depth + 1:
        if loc.imag + 1 == floor:
            grid.add(loc)
            return grid
        elif loc + 1j not in grid:
            loc += 1j
        elif loc -1 + 1j not in grid:
            loc += -1 +1j
        elif loc + 1 + 1j not in grid:
            loc += 1 + 1j
        else:
            grid.add(loc)
            return grid
    return False


def grain_rain(grid, max_depth, floor=None):
    grains = 0
    while grid:
        grid = sand_grain(grid, max_depth, floor=floor)
        if not grid or complex(500) in grid:
            return grains
        grains += 1
    return grains


def main(day, part=1):
    day.parse_list_of_lists(sep="\n", sep2=" -> ")
    day.apply(str.split, sep=",")
    day.apply(int)
    grid, max_depth = create_grid(day.data)
    if part == 1:
        return grain_rain(grid, max_depth)
    if part == 2:
        return grain_rain(grid, max_depth, floor=max_depth + 1) + 1


if __name__ == "__main__":
    day = Day(14)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=14, year=2022)

    #     data = """498,4 -> 498,6 -> 496,6
    # 503,4 -> 502,4 -> 502,9 -> 494,9"""
    #     day.load(data)

    day.load()
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=14, year=2022)
