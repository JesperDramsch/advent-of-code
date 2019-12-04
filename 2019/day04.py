from util import Day
from itertools import groupby

def check_password(password: str) -> bool:
    six  = len(password) == 6
    doub = not sorted(set(password)) == sorted(password)
    sort = ''.join(sorted(password)) == password
    return six and doub and sort

def check_groups(password: str) -> bool:
    groups = []
    for _, g in groupby(password):
        if len(list(g)) == 2:
            return True and  check_password(password)
    return False



if __name__ == "__main__":
    part1 = Day(4,1)

    part1.load(typing=int,sep="-")
    part1.load(list(range(part1.data[0],part1.data[1]+1)))

    part1.apply(str)

    part1.apply(check_password)

    print(part1.answer(sum(part1.data)))

    part2 = Day(4,2)

    part2.load(typing=int,sep="-")
    part2.load(list(range(part2.data[0],part2.data[1]+1)))

    part2.apply(str)

    part2.apply(check_groups)

    print(part2.answer(part2.sum()))



