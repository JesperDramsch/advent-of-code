from util import Day
from aocd import submit


def preprocess(data):
    data = [int(x) for x in data]
    data_max = len(data)
    out = {}
    for i, cup in enumerate(data):
        out[cup] = data[(i + 1) % data_max]
    return out


def show_cups(cups, start):
    # show_cups = f"{start}"
    show_cups = [start]
    for _ in cups.items():
        show_cups.append(cups[show_cups[-1]])
    return "".join(map(str, show_cups))


def cüps(cups, moves=10, verbose=None):
    out, current = (cups, next(iter(cups.keys())))
    num_cups = len(cups)
    for i in range(moves):
        if verbose:
            print(f"\nMove {i+1}")
        out, current = cüps_möve(out, current, num_cups, verbose=verbose)
    return out


def cüps_möve(cups, current, num_cups, verbose=None):
    if verbose:
        the_sequence = show_cups(cups, current)
    # take cups
    taken = (cups[current], cups[cups[current]], cups[cups[cups[current]]])
    cups[current] = cups[taken[2]]

    # find destination
    destination = current - 1
    if destination == 0:
        destination = num_cups
    while destination in taken:
        if destination == 1:
            destination = num_cups
        else:
            destination -= 1
        

    # insert taken
    cups[destination], cups[taken[2]] = taken[0], cups[destination]
    if verbose:
        print("Cups, before\t", the_sequence[:25])
        print("Cups, after\t", show_cups(cups, current)[:25])
        print("Current\t\t", current)
        print("Taken\t\t", taken)
        print("Destination\t", destination)

    current = cups[current]
    return cups, current


def main(day, part=1):
    if part == 1:
        day.data = preprocess(day.data)
        game = cüps(day.data, 100, verbose=True)
        out = show_cups(game, 1)[1:-1]
    if part == 2:
        day.data = [int(x) for x in day.data] + [x for x in range(10, 1000001)]
        day.data = preprocess(day.data)
        game = cüps(day.data, 10000000)
        first = game[1]
        second = game[first]
        out = first * second
    return out


if __name__ == "__main__":
    day = Day(23)
    day.download()

    day.load(process=False)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=23, year=2020)

    day.load(process=False)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=23, year=2020)
