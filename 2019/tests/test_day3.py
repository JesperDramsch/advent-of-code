import sys
sys.path.insert(0, '.')
from util import Day
from day03 import *

def test_part1():
    part1 = Day(3,1)
    part2 = Day(3,2)

    part1.load()
    
    part1.load(data = {0: part1.data[0].split(","),
                       1: part1.data[1].split(",")})
    
    pathA = path(part1.data[0])
    pathB = path(part1.data[1])
    union = intersect(pathA, pathB)

    part1.answer(min(abs(coord[0])+abs(coord[1]) for coord in union))
    part2.answer(min(pathA[coord]+pathB[coord] for coord in union))

    assert part1.result == 260
    assert part2.result == 15612

def minway(kablemap,val,direction,cy,cx):
    minsteps = np.inf
    for z in np.argwhere(kablemap==3):
        steps = 0
        # print(z[0],z[1])
        for j in range(val.shape[0]):
            x, y = cy, cx
            cont = True
            # print(j)
            for i in range(val[j].size):
                for _ in range(val[j][i]):
                    if   direction[j][i] == 'L':
                        x -= 1
                    elif direction[j][i] == 'R':
                        x += 1
                    elif direction[j][i] == 'U':
                        y -= 1
                    elif direction[j][i] == 'D':
                        y += 1
                    else:
                        return None
                    steps += 1
                    if z[0] == y and z[1] == x:
                        cont = False
                        break
                if not cont:
                    break
        # print(steps)
        if steps < minsteps:
            minsteps = steps
    return minsteps