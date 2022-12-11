from day import Day
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
    # Prepare the cardinal directions for view distance
    cardinals, out = [
    #   (lat_a,   lat_z,     lon_a,   lon_z,    direction)
        (lat,     lat + 1,   lon + 1, len(grid[0]), 1), # right
        (lat,     lat - 1,   lon - 1, -1,          -1), # left
        (lat + 1, len(grid), lon,     lon + 1,      1), # down
        (lat - 1, -1,        lon,     lon - 1,     -1), # up
    ], []

    # Iterate through the cardinal directions (up, down, right, left)
    for lat_a, lat_z, lon_a, lon_z, direction in cardinals:
        # Iterate through latitude then Iterate through longitude
        for i, lat_i in enumerate(range(lat_a, lat_z, direction), 1):
            for ii, lon_i in enumerate(range(lon_a, lon_z, direction), 1):
                # If the tree is higher, add the distance to the output
                if grid[lat_i][lon_i] >= grid[lat][lon]:
                    out.append(i * ii)
                    break
            # Break out of nested loop if we found a higher tree
            else: continue
            break
        else:
            # If we didn't find a higher tree, add the max distance
            out.extend(direction * (z + -1 * a) for a, z in ((lat_a, lat_z), (lon_a, lon_z)))

    return scenic_score(out)


def check_trees(grid):
    for i in range(len(grid)):
        for ii in range(len(grid[0])):
            yield viewing_distance(grid, i, ii)


def main(day, part=1):
    day.parse_list_of_lists(sep="\n", sep2="", typing=int)
    if part == 1:
        return sum(sum(x) for x in check_visibility(day.data))
    if part == 2:
        return max(check_trees(day.data))


if __name__ == "__main__":
    day = Day(8)
    day.download()

    day.load()
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=8, year=2022)

    day.load()
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=8, year=2022)
