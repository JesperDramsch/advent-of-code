from util import Day


def preprocess(data):
    out = []
    for dat in data.replace("\n\n", "\t").replace("\n", " ").strip().split("\t"):
        out.append(set(dat.replace(" ", "")))
    return out

def preprocess2(data):
    out = []
    for dat in data.replace("\n\n", "\t").replace("\n", " ").strip().split("\t"):
        x = [set(y) for y in dat.split(" ")]
        out.append(set.intersection(*x))
    return out

def main(day, part=1):
    if part == 1:
        day.data = preprocess(day.data)
        out = 0
        for x in day.data:
            out += len(x)
    if part == 2:
        day.data = preprocess2(day.data)
        out = 0
        for x in day.data:
            out += len(x)
    return out

if __name__ == "__main__":
    day = Day(6)
    day.load(typing=str, process=False)
    print(main(day))
    day.load(typing=str, process=False)
    print(main(day, part=2))
