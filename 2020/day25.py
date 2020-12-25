from util import Day
from aocd import submit


def transform(value=1, subject=7, loop_size=1):
    for _ in range(loop_size):
        value = (value * subject) % 20201227
    return value


def find_loopsize(expectation):
    i = 0
    val = 1
    while val != expectation:
        val = transform(val, subject=7, loop_size=1)
        i += 1
    return i


def get_encryption_key(public_key, loop_size):
    return transform(subject=public_key, loop_size=loop_size)


def main(day, part=1):
    card, door = day.data
    print(card, door)
    if part == 1:
        ls_card = find_loopsize(card)
        ls_door = find_loopsize(door)
        enc_card = get_encryption_key(door, ls_card)
        enc_door = get_encryption_key(card, ls_door)
        if enc_card == enc_door:
            out = enc_card
    if part == 2:
        pass
    return out


if __name__ == "__main__":
    day = Day(25)
    day.download()

    day.load(typing=int)
    p1 = main(day)
    print(p1)
    submit(p1, part="a", day=25, year=2020)

