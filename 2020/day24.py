from util import Day
from aocd import submit
from collections import Counter

# east, southeast, southwest, west, northwest, and northeast
# e, se, sw, w, nw, and ne
# pointy hex


def preprocess(row):
    return row.replace("", " ").strip().replace("n ", "n").replace("s ", "s").split(" ")

directions = {
    "ne": 1 + 0.5j,
    "e": 1j,
    "se": -1 + 0.5j,
    "sw": -1 - 0.5j,
    "w": -1j,
    "nw": 1 - 0.5j,
}


def flip(row):
    return sum((directions[char] for char in row))


def get_neighbours(tile):
    return [tile + val for val in directions.values()]


def möve(state):
    new_state = set()

    around = Counter()
    for tile in state:
        neighbours = get_neighbours(tile)
        count = 0
        for n in neighbours:
            if n in state:
                count += 1   # neighbour black of this black tile
            else:
                around[n] += 1  # counts up one for the neighbouring tiles if white
        # Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
        if 0 < count < 3:
            new_state.add(tile)

    # Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.
    for k, v in around.items():
        if v == 2:
            new_state.add(k)

    return new_state


def hex_of_lyfe(state, moves):
    for i in range(moves):
        state = möve(state)
        print(f"Move {i+1}: {len(state)}")
    return len(state)


def main(day, part=1):
    day.apply(preprocess)
    day.apply(flip)
    count = Counter(day.data)
    if part == 1:
        out = sum((1 for _, v in count.items() if (v % 2)))
    if part == 2:
        start = set((k for k, v in count.items() if (v % 2)))
        out = hex_of_lyfe(start, 100)
    return out


if __name__ == "__main__":
    day = Day(24)
    day.download()

    day.load(typing=str)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=24, year=2020)

    day.load(typing=str)
    p2 = main(day, part=2)
    print(p2)
    submit(p2, part="b", day=24, year=2020)
