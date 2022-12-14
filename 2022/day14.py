from day import Day
from aocd import submit

def create_grid(data):
    grid = {}
    max_depth = 0
    for line in data:
        for (a, b), (x, y) in zip(line, line[1:]):
            for i in range(min(a,x), max(a,x) + 1):
                for ii in range(min(b,y), max(b,y) + 1):
                    grid[(i, ii)] = True
                    max_depth = max(max_depth, ii)
    return grid, max_depth + 1

def find_top(x, grid, max_depth):
    for i in range(max_depth):
        if (x, i) in grid:
            return i

def sand_grain(grid, max_depth, start=(500, 0)):
    x, y = start

    while y < max_depth+1:
        if (x, y+1) in grid:
            if (x-1, y+1) in grid:
                if (x+1, y+1) in grid:
                    grid[(x, y)] = False
                    return grid
                else:
                    x += 1
            else:
                x -= 1
        else:
            y += 1
    return False

def grain_rain(grid, max_depth, start=(500, 0)):
    grains = 0
    while grid:
        grains += 1
        grid = sand_grain(grid, max_depth, start=start)
    return grains
        


def main(day, part=1):
    day.parse_list_of_lists(sep="\n", sep2=" -> ")
    day.apply(str.split, sep=",")
    day.apply(int)
    if part == 1:
        grid, max_depth = create_grid(day.data)
        return grain_rain(sand_grain(grid, max_depth), max_depth)
    if part == 2:
        pass

if __name__ == "__main__":
    day = Day(14)
    day.download()


    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=14, year=2022)

    data = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9"""
    day.load(data)
    
    # day.load()
    p2 = main(day, part=2)
    print(p2)
    # submit(p2, part="b", day=14, year=2022)
