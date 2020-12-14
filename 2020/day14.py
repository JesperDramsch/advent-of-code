from util import Day
from aocd import submit


def preprocess(data):
    mem = {}
    for row in data:
        target, data = row.split(" = ")
        if "mask" in target:
            mask = data
        else:
            num = int(target[:-1].split("[")[1])
            mem[num] = int(data)
    return mask, mem


# used enumerate before but this from @sophiebits is so much better
def edit(mask, row):
    row |= int(mask.replace("X", "0"), 2)
    row &= int(mask.replace("X", "1"), 2)
    return row


def batch(data):
    # generate sublist
    split_list = []
    sub_list = None
    for x in data:
        if "mask" in x:
            if sub_list:
                split_list.append(preprocess(sub_list))
            sub_list = []
        sub_list.append(x)
    split_list.append(preprocess(sub_list))
    return split_list


# Need to practice recursion, so let's solve part 2 with recursion by solving it with recursion
# Enumerate from part 1 would break my brains


def get_masks(data):
    # Transcode to the "old" v1 mask
    if not data:
        yield ""
        return
    for mask in get_masks(data[1:]):
        # leave unchanged
        if data[0] == "0":
            yield "X" + mask
        # replace with 1
        elif data[0] == "1":
            yield "1" + mask
        # "floating" replace with 1 and 0
        elif data[0] == "X":
            yield "0" + mask
            yield "1" + mask


def v1(split_list):
    t = {}
    for mask, mem in split_list:
        for k, v in mem.items():
            t[k] = edit(mask, v)
    return t


def v2(split_list):
    t = {}
    for mask, mem in split_list:
        for m in get_masks(mask):
            for k, v in mem.items():
                t[edit(m, k)] = v
    return t


def main(day, part=1):
    day.data = batch(day.data)
    if part == 1:
        edited = v1(day.data)
        out = sum(edited.values())
    if part == 2:
        edited = v2(day.data)
        out = sum(edited.values())
    return out


if __name__ == "__main__":
    day = Day(14)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=14, year=2020)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=14, year=2020)
