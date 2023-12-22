from day import Day
from aocd import submit


def reindeer_hash(data, val=0):
    if len(data) == 0:
        return val
    val += ord(data[0])
    val *= 17
    val %= 256
    return reindeer_hash(data[1:], val)


def main(day, part=1):
    data = day.data.split(",")
    if part == 1:
        return sum(reindeer_hash(d) for d in data)
    if part == 2:
        pass


if __name__ == "__main__":
    day = Day(15)
    day.download()

    day.load(process=False)
    # data = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"""

    # day.load(data, process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=15, year=2023)

    # day.load()
    # p2 = main(day, part=2)
    # print(p2)
    # submit(p2, part="b", day=15, year=2023)
