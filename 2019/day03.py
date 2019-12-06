from util import Day


def path(directions: list) -> dict:
    index = {k: i for i, k in enumerate("RLUD")}

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    x, y = 0, 0
    steps = 0

    out = {}

    for direction in directions:
        rlud = direction[0]
        num = int(direction[1:])

        for _ in range(num):
            steps += 1
            x += dx[index[rlud]]
            y += dy[index[rlud]]
            if (x, y) not in out:
                out[(x, y)] = steps
            # out[(x,y)] = 1  Part 1, you served me well
    return out


def intersect(pathA: dict, pathB: dict) -> list:
    return list(set(pathA.keys()) & set(pathB.keys()))


if __name__ == "__main__":
    ## Part One
    part1 = Day(3, 1)
    part2 = Day(3, 2)

    part1.load()

    part1.load(data={0: part1.data[0].split(","), 1: part1.data[1].split(",")})
    part2.data = part1.data

    pathA = path(part1.data[0])
    pathB = path(part1.data[1])
    union = intersect(pathA, pathB)

    print(part1.answer(min(abs(coord[0]) + abs(coord[1]) for coord in union)))

    print(part2.answer(min(pathA[coord] + pathB[coord] for coord in union)))

