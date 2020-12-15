from util import Day
from aocd import submit

## Python's recursion limit is 1000, so we'll use iterations
def game(starting_numbers, max_num):
    numbers = {k: i + 1 for i, k in enumerate(starting_numbers[:-1])}
    next_num = starting_numbers[-1]
    for i in range(len(starting_numbers), max_num):
        idx = numbers.get(next_num, i)
        # print(numbers, "spoken", next_num, "next", i-idx) # Good ol' print debugging
        numbers[next_num] = i
        next_num = i - idx
    return next_num


def main(day, part=1):
    if part == 1:
        return game(day.data, 2020)
    if part == 2:
        return game(day.data, 30000000)


if __name__ == "__main__":
    day = Day(15)
    day.download()

    day.load(sep=",")
    # day.load(data, sep=",")
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=15, year=2020)

    day.load(sep=",")
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=15, year=2020)
