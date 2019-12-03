from util import Day

def path(directions: list):
    index = {k:i for i, k in enumerate("RLUD")}
    
    dx = [1, -1, 0,  0]
    dy = [0,  0, 1, -1]
    
    x, y = 0, 0
    length = 0

    out = {}

    for direction in directions:
        rlud = direction[0]
        num = int(direction[1:])

        for _ in range(num):
            length += 1
            x += dx[index[rlud]]
            y += dy[index[rlud]]
            if (x,y) not in out:
                out[(x,y)] = length
    return out


if __name__ == "__main__":
    ## Part One
    part1 = Day(3,1)
    part1.load(str)
    
    part1.data = {0: part1.data[0].split(","),
                  1: part1.data[1].split(",")}

    #print(part1.data[0])
    pathA = path(part1.data[0])
    pathB = path(part1.data[1])

    union = set(pathA.keys()) & set(pathB.keys())

    part2 = Day(3,2)

    print(part1.answer(min([abs(x)+abs(y) for (x,y) in union])))
    print(part2.answer(min([pathA[p]+pathB[p] for p in union])))


