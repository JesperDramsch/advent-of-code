from util import Day
from aocd import submit


def parse(data):
    """Parse a square grid of single digit integers

    123
    456
    789
    becomes
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    Parameters
    ----------
    data : list(str)
        _description_

    Returns
    -------
    list(list(int))
        list of lists of integers of trees
    """
    return [[int(x) for x in y] for y in data]


def check_visibility(grid, visible=None):
    if visible is None:
        visible = [[False for _ in row] for row in grid]

    for reverser in [False, True]:
        max_height_row = [-1 for _ in grid[0]]
        max_height_col = [-1 for _ in range(len(grid))]

        for q in range(len(grid)):
            for qq in range(len(grid[0])):
                if reverser:
                    i = len(grid) - q - 1
                    ii = len(grid[0]) - qq - 1
                else:
                    i, ii = q, qq
                cell = grid[i][ii]
                if cell > max_height_row[ii]:
                    visible[i][ii] = True
                    max_height_row[ii] = cell
                if cell > max_height_col[i]:
                    visible[i][ii] = True
                    max_height_col[i] = cell
    return visible

def scenic_score(scores):
    x = 1
    for i in scores:
        x *= i
    return x

def viewing_distance(grid, lat, lon):
    """Find the distance from a cell to the nearest cell with a higher score

    Parameters
    ----------
    grid : list(list(int))
        list of lists of integers of trees
    lat : int
        latitude of cell
    lon : int
        longitude of cell

    Returns
    -------
    list(int)
        distances to nearest higher cell
    """
    out = []

    for i, right in enumerate(range(lon+1, len(grid[0]))):
        if grid[lat][right] >= grid[lat][lon]:
            out.append(i+1)
            break
    else:
        out.append(len(grid[0]) - lon - 1)
    for i, left in enumerate(range(lon-1, -1, -1)):
        if grid[lat][left] >= grid[lat][lon]:
            out.append(i+1)
            break
    else:
        out.append(lon)
    for i, down in enumerate(range(lat+1, len(grid))):
        if grid[down][lon] >= grid[lat][lon]:
            out.append(i+1)
            break
    else:
        out.append(len(grid) - lat - 1)
    for i, up in enumerate(range(lat-1, -1, -1)):
        if grid[up][lon] >= grid[lat][lon]:
            out.append(i+1)
            break
    else:
        out.append(lat)
    
    return scenic_score(out)

def check_trees(grid):
    for i in range(len(grid)):
        for ii in range(len(grid[0])):
            yield viewing_distance(grid, i, ii)

def main(day, part=1):
    grid = parse(day.data)
    if part == 1:
        visible = check_visibility(grid)
        return sum(sum(x) for x in visible)
    if part == 2:
        return max(check_trees(grid))


if __name__ == "__main__":
    day = Day(8)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=8, year=2022)

    # day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=8, year=2022)
