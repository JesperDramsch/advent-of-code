from util import Day
from aocd import submit
import numpy as np
from itertools import product, combinations


def preprocess(data):
    out = {}
    for x in data.replace("#", "1").replace(".", "0").split("\n\n"):
        k, v = x.split(":\n")
        out[int(k.split()[-1])] = v.split("\n")
    return out


def get_hash(data):
    check = {}
    for k, arr in data.items():
        tmp_arr = [arr[0], arr[-1], "".join([x[0] for x in arr]), "".join([x[-1] for x in arr])]  # get all edges
        tmp_arr += [x[::-1] for x in tmp_arr]  # turn them all around
        check[k] = set([int(x, 2) for x in tmp_arr])  # convert to decimal
    return check


def match_cells(data):
    out = {}
    for (k, v), (x, y) in combinations(data.items(), r=2):
        z = v.intersection(y)
        if z:
            out[k] = out.get(k, []) + [x]
            out[x] = out.get(x, []) + [k]
    return {k: set(v) for k, v in out.items()}


def find_corner(cells):
    out = []
    smol = []
    for k, cell in cells.items():
        if len(cell) == 2:
            smol.append(cell)
            out.append(k)
    return out, smol


def neighbours(x, y):
    out = []
    if 0 <= x - 1:
        out.append((x - 1, y))
    if 0 <= y - 1:
        out.append((x, y - 1))
    return np.array(out)


def grow_image(corners, cells):
    one_corner = corners[0][0]
    border = int(np.sqrt(len(cells)))
    arr = np.zeros((border, border), dtype=int)
    arr[0, 0] = one_corner
    i = 1
    while np.count_nonzero(arr == 0) != 0:
        i += 1
        next_diagonal = np.zeros((border, border))
        # get the next diagonal row
        next_diagonal[0:i, 0:i] = np.rot90(np.eye(i))[:border, :border]
        # get the indices
        r = np.transpose(np.nonzero(next_diagonal)).tolist()
        # rotate list by one
        r.append(r.pop(0))
        for x, y in r:
            # brute force get the assigned cells
            assigned = set(np.unique(arr))
            # got top neighbour cells
            neighbour = neighbours(x, y)
            # get the value from the first neighbour
            val = cells[arr[tuple(neighbour[0])]]
            # if there's another neighbour, get the intersection with that one
            if len(neighbour) > 1:
                val = val.intersection(cells[arr[tuple(neighbour[1])]])
            # remove assigned cell to make sure
            val = val - assigned

            # get the integer value from the set
            arr[x, y] = int(val.pop())

            # print(arr) # <-- loooks cool.
    return arr


def numpyfy(arr):
    out = np.zeros((10, 10), dtype=int)
    for i, row in enumerate(arr):
        out[i, :] = [int(x) for x in row]
    return out


def match_first_corner(a, b, c):
    for k in range(8):
        # all flip configurations
        a = np.fliplr(a)
        if k in [2, 4, 6]:
            b = np.fliplr(b)
        if k == 5:
            c = np.fliplr(c)
        for i, j, m in product(range(4), repeat=3):
            a = np.rot90(a, i)
            b = np.rot90(b, j)
            c = np.rot90(c, m)
            if all(a[:, -1] == b[:, 0]) and all(a[-1, :] == c[0, :]):
                return a, b, c


def match_arrs(a, left=None, top=None):
    le = left is None
    t = top is None
    for _ in range(2):
        a = np.fliplr(a)
        for i in range(4):
            a = np.rot90(a, i)
            if left is not None and all(left[:, -1] == a[:, 0]):
                le = True
            if top is not None and all(top[-1, :] == a[0, :]):
                t = True
            if le and t:
                return a


def build_arr(idx_arr, data):
    # build the image arrays
    arr = np.zeros([8 * idx_arr.shape[0]] * 2, dtype=int)

    # match first to get orientation
    # hash_match = set(hashes[idx_arr[0, 0]]).intersection(set(hashes[idx_arr[0, 1]]))
    a = numpyfy(data[idx_arr[0, 0]])
    b = numpyfy(data[idx_arr[0, 1]])
    c = numpyfy(data[idx_arr[1, 0]])

    data[idx_arr[0, 0]], data[idx_arr[0, 1]], data[idx_arr[1, 0]] = match_first_corner(a, b, c)

    for a, b in np.ndindex(idx_arr.shape):
        idx = idx_arr[a, b]
        if isinstance(data[idx], np.ndarray):
            arr[a * 8 : (a + 1) * 8, b * 8 : (b + 1) * 8] = data[idx][1:-1, 1:-1]
            continue

        to_match = numpyfy(data[idx])

        # match_arrs(a, left=None, top=None)
        neighbour = neighbours(a, b)
        if len(neighbour) == 2:
            matched = match_arrs(
                to_match, left=data[idx_arr[tuple(neighbour[1])]], top=data[idx_arr[tuple(neighbour[0])]]
            )
        elif a == 0:
            matched = match_arrs(to_match, left=data[idx_arr[tuple(neighbour[0])]])
        elif b == 0:
            matched = match_arrs(to_match, top=data[idx_arr[tuple(neighbour[0])]])
        # print(data)
        data[idx] = matched
        arr[a * 8 : (a + 1) * 8, b * 8 : (b + 1) * 8] = matched[1:-1, 1:-1]
    return arr


def find_snek(data):
    snek = """                  # 
#    ##    ##    ###
 #  #  #  #  #  #   """
    snek = snek.replace(" ", "0 ").replace("#", "1 ").split("\n")

    # cbb
    snek = np.array([[int(x) for x in s.strip().split(" ")] for s in snek])
    snek_len = np.sum(snek)

    snekies = []
    for i in range(4):
        t = np.rot90(snek, i)
        snekies.append(t)
        snekies.append(np.flip(t, 0))
        snekies.append(np.flip(t, 1))

    sneks = 0
    while sneks == 0:
        snek = snekies.pop()
        snek_y, snek_x = snek.shape
        for y, x in np.ndindex(data.shape):
            x -= snek_x // 2 - 1
            y -= snek_y // 2
            sub_arr = data[y : y + snek_y, x : x + snek_x].copy()
            if not sub_arr.shape == snek.shape:
                continue
            sub_arr *= snek

            if np.sum(sub_arr) == snek_len:
                sneks += 1
                data[y : y + snek_y, x : x + snek_x] -= snek
    return data


def main(day, part=1):
    data = preprocess(day.data)
    hashed = get_hash(data)
    cells = match_cells(hashed)
    corners = find_corner(cells)
    if part == 1:
        out = int(np.prod(corners[0], dtype=np.int64))
    if part == 2:
        idx_arr = grow_image(corners, cells)
        arr = build_arr(idx_arr, data)
        desnaked = find_snek(arr)
        out = np.sum(desnaked)
    return out


if __name__ == "__main__":
    day = Day(20)
    day.download()

    day.load(process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=20, year=2020)

    day.load(process=False)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=20, year=2020)

